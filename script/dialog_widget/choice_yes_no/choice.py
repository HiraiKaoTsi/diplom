# built - in Module
from PyQt5 import QtCore, QtGui, QtWidgets

# interface
from .ui_choice import Ui_DialogYesNo


class DialogChoiceYesOrNo(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_DialogYesNo()
        self.ui.setupUi(self)

        self.ui.pushButton_yes.clicked.connect(self.onYes)
        self.ui.pushButton_no.clicked.connect(self.onNo)

        self.info_choice = False

    def OpenDialog(self, text_for_message: str):
        self.ui.label_main_text.setText(f"{text_for_message}")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.exec()
        return self.info_choice

    def onYes(self):
        self.info_choice = True
        self.close()
    
    def onNo(self):
        self.close()