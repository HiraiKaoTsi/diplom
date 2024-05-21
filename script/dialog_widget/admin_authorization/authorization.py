from PyQt5 import QtCore, QtWidgets
from os import listdir

from script.module_db.handler_admin import *
from script.dialog_widget import *

# interface
from .admin_ui import Ui_DialogLogin




class AuthorizationAdmin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_DialogLogin()
        self.ui.setupUi(self)

        self.EditStyleSheet()

        # Информация об авторизации
        self.info_login = False

        self.ui.pushButton_login.clicked.connect(self._OnLogin)
    
    def _OnLogin(self):
        login = self.ui.lineEdit_login.text().strip()
        password = self.ui.lineEdit_passsword.text().strip()
        if (not login) or (not password):
            return
        if CheckInfoAdmin(login, password):
            DialogNotification().OpenDialog("Авторизация успешна!")
            self.info_login = True
            self.close()
        else:
            DialogNotification().OpenDialog("Неверные данные!")
       

    def OpenDialog(self):
        """
        Открытия диалогового окна
        """
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.exec()
        return self.info_login


    def EditStyleSheet(self) -> None:
        """
        Данный метод считывает файлы .qss в каталоге style и применяет их к приложению
        """
        style = ""
        for qss_file in listdir("style"):
            with open(f"style/{qss_file}", mode="r", encoding="utf-8") as qss:
                style += qss.read()

        self.setStyleSheet(style)
        QtWidgets.qApp.setStyleSheet(style)