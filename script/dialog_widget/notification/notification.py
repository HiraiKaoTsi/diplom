from PyQt5 import QtCore, QtWidgets

# interface
from .notification_ui import Ui_DialogNotification


class DialogNotification(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_DialogNotification()
        self.ui.setupUi(self)

        self.ui.pushButton_ok.clicked.connect(self.onOk)

    def OpenDialog(self, text_for_message: str):
        """
        Открытия диалогового окна
        :param text_for_message: текст для диалогового окна
        """
        self.ui.label_main_text.setText(f"{text_for_message}")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.exec()

    def onOk(self):
        self.close()
    