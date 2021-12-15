import numpy as np
import json
from src.model import Model
from orm.data import add_data


class Interface:
    def __init__(self):
        self.m = Model()

    def on_train(self):
        response = {}
        try:
            self.m.train_model()
            loss, accuracy = self.m.get_metrics()
            data = {'loss': loss, 'accuracy': accuracy}
        except Exception as e:
            response = {'success': 'KO', 'message': str(e)}
        else:
            response = {'success': 'OK', 'message': 'Model trained successfully', 'data': json.dumps(data)}
        return response

    def on_add(self, x, y, use):
        response = {}
        try:
            x = float(x)
            y = float(y)
            train = bool(use == 'train')

            add_data(x, y, train)
            self.m.load_data()
            self.m.preprocess_data()
        except Exception as e:
            response = {'success': 'KO', 'message': str(e)}
        else:
            response = {'success': 'OK', 'message': '<{0} : {1}> added to {2} dataset'
                        .format(x, y, ['TEST', 'TRAIN'][train])}
        return response

    def on_list(self):
        response = {}
        try:
            data_train = self.m.data_train.to_dict()
            data_test = self.m.data_test.to_dict()
            l_test = len(data_test["x"])
            l_train = len(data_train["x"])

            t = [{'x': data_test["x"][i], 'y': data_test["y"][i], 'train': False} for i in range(l_test)] + \
                [{'x': data_train["x"][i], 'y': data_train["y"][i], 'train': True} for i in range(l_train)]
        except Exception as e:
            response = {'success': 'KO', 'message': str(e)}
        else:
            response = {'success': 'OK', 'message': 'null', 'data': json.dumps(t)}
        return response

    def on_infer(self, x):
        response = {}
        try:
            x = float(x)
            y = self.m.predict(np.array([x, ]))
        except Exception as e:
            response = {'success': 'KO', 'message': str(e)}
        else:
            response = {'success': 'OK', 'message': 'null', 'data': str(y)}
        return response
