from model import Model


class Interface:
    def __init__(self):
        self.m = Model()

    def on_train(self):
        try:
            self.m.train_model()
        except Exception as e:
            print(e)

    def on_add(self, x, y):
        pass

    def on_list(self):
        pass

    def on_infer(self, x):
        pass
