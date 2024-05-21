from PyQt5 import QtCore, QtGui, QtWidgets
from sys import argv, exit

from script.dialog_widget import *
from app import FunctionalMainWindow


if __name__ == "__main__":
    app_login = QtWidgets.QApplication(argv)
    dialog_login = AuthorizationAdmin()
    info_login = dialog_login.OpenDialog()
    
    if info_login:
        app = QtWidgets.QApplication(argv)
        myapp = FunctionalMainWindow()
        myapp.show()
        exit(app.exec_())
