from PyQt5 import QtGui, QtWidgets, QtCore

# interface
from .information_large_text_ui import Ui_Dialog


class DialogLargeText(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.resize(800, 600)

        self.data = {
            0: {
                "title": "Инструкция",
                "icon": ":/icons/main/manual.png",
                "file-text": "manual.html",
            },
            1: {
               "title": "Информация",
               "icon": ":/icons/main/info.png",
               "file-text": "information.html",
            },
            2: {
                "title": "Об аторе",
                "icon": ":/icons/users/author.png",
                "file-text": "author.html",
            }
        }

    def OpenDialog(self, info_for_open: int):
        """
        :param info_for_open: 0 - инструкция, 1 - информация, 2 - об авторе 
        """
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.data[info_for_open]["icon"]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        self.setWindowTitle(self.data[info_for_open]["title"])

        with open(f"datafiles\\info-for-user\\{self.data[info_for_open]['file-text']}", mode="r", encoding="UTF-8") as file:
            self.ui.label_main_text.setText(file.read())
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
