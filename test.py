from PyQt5 import QtCore, QtGui, QtWidgets


class TriggerForMainClass:
    def __init__(self, main_class):
        self.main = main_class
        self.x = 3

    def TEST(self, input_funct=None):
        print(type(input_funct))
        print(input_funct)
        def output_func(*args):
            print("##########################")

            input_funct()
            print("##########################")
        return output_func


class TriggerForMainClass:
    def __init__(self, main_class):
        self.main = main_class

    def __call__(self, *args, **kwargs):
        self.main_class(*args, **kwargs)
        self.counter += 1
        print(f"Called {self.counter} times")