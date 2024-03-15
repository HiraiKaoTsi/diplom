# built - in Module
from PyQt5 import QtCore, QtGui, QtWidgets

# interface
from .edit_ui import Ui_DialogEdit


class DialogEditInfo(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_DialogEdit()
        self.ui.setupUi(self)

        self.ui.pushButton_edit.clicked.connect(self.onEdit)
        self.ui.pushButton_cancel.clicked.connect(self.onCancel)

        self.info_choice = False

    def OpenDialog(self, text_for_message: str):
        
        


        self.ui.label_main_text.setText(f"{text_for_message}")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.exec()
        return self.info_choice

    def onEdit(self):
        self.info_choice = True
        self.close()
    
    def onCancel(self):
        self.close()