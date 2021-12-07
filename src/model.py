import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
from tensorflow.keras.losses import MSE
from tensorflow.keras.callbacks import EarlyStopping


class Model:
    def __init__(self):
        self.model = None
        self.data_train = None
        self.data_test = None
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None

        self.load_data(src='csv')
        self.preprocess_data()

        try:
            self.load_model()
        except Exception as e:
            self.build_model()
            self.train_model()
            self.save_model()

    def load_data(self, src='csv'):
        if src == 'csv':
            data_train = pd.read_csv('./data/train.csv')
            data_test = pd.read_csv('./data/test.csv')

            self.data_train = data_train.dropna()
            self.data_test = data_test.dropna()

            self.x_train = self.data_train['x']
            self.y_train = self.data_train['y']

            self.x_test = self.data_test['x']
            self.y_test = self.data_test['y']
        if src == 'sql':
            pass

    def preprocess_data(self):
        scaler = MinMaxScaler()
        self.x_train = np.array(self.x_train).reshape(-1, 1)
        self.x_train = scaler.fit_transform(self.x_train)

        self.x_test = np.array(self.x_test).reshape(-1, 1)
        self.x_test = scaler.fit_transform(self.x_test)

    def build_model(self):
        self.model = Sequential()
        self.model.add(Dense(1, input_shape=(1,), activation='relu'))
        self.model.compile(tf.keras.optimizers.SGD(
            learning_rate=0.1,
            name='SGD',
            nesterov=True
        ), loss=MSE)

    def train_model(self):
        early_stop = EarlyStopping(mode='min', monitor='val_loss', patience=50, verbose=1)
        self.model.fit(self.x_train, self.y_train, validation_data=(self.x_test, self.y_test), epochs=100, verbose=1,
                       callbacks=[early_stop])

    def predict(self, x=None):
        if x is None:
            x = self.x_test
        y_predict = self.model(x)
        y = tf.get_static_value(y_predict)
        return y[0][0]

    def save_model(self):
        self.model.save("./output/simple_model")

    def load_model(self):
        self.model = keras.models.load_model("./output/simple_model")

    def delete_model(self):
        pass


if __name__ == '__main__':
    tf.keras.backend.clear_session()
    m = Model()
    m.predict()
