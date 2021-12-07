from src.model import Model
import numpy as np

class Interface:
    def __init__(self):
        self.m = Model()
        pass

    def on_train(self):
        try:
            self.m.train_model()
        except Exception as e:
            print(e)

    def on_add(self, x, y, train):
        response = {}
        try:
            x = float(x)
            y = float(y)
            train = bool(train)
        except Exception as e:
            response = {'success': 'KO', 'message': e}
        else:
            response = {'success': 'OK', 'message': '<{0}, {1}> added to {2} dataset'
                        .format(x, y, ['test', 'train'][train])}
        finally:
            return response

    def on_list(self):
        pass

    def on_infer(self, x):
        response = {}
        try:
            x = float(x)
            y = self.m.predict(np.array([x, ]))
        except Exception as e:
            response = {'success': 'KO', 'message': e}
        else:
            response = {'success': 'OK', 'message': str(y)}
        finally:
            return response
