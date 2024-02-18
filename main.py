# built - in Module
from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets

from datetime import  date
from datetime import datetime


from script.module_db import *

# interface
from interface import Ui_MainWindow


class FunctionalMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # START TAB-MAIN-INFO
        self.ui.label_today_date.setText(f"Сегодняшняя дата - {datetime.strftime(date.today(), '%d.%m.%Y')}")
        self.ui.label_total_number_books.setText(f"{CountBook()}")
        self.ui.label_how_many_given_book.setText(f"{IssuedBookAll()}")
        self.ui.label__how_many_given_book_today.setText(f"{NumberBooksIssuedToday()}")
        self.ui.label_how_many_debtors.setText("") # Доделать
        # END TAB-MAIN-INFO

        # START TAB-ADD-BOOK
        self.ui.pushButton_add_new_book.clicked.connect(self.AddNewBook)
        # END TAB-ADD-BOOK

    def AddNewBook(self):
        
        meaning = \
        [
            self.ui.lineEdit_name_book_add.text().strip(), self.ui.lineEdit_author_add.text().strip(), 
            self.ui.lineEdit_isbn_add.text().strip(), self.ui.lineEdit_year_publication_add.text().strip(), 
            self.ui.lineEdit_quantity_book_add.text().strip()
        ]

        for value in meaning:
            if not value:
                print("Заполните данные")
                return
        
        if AddNewBook(*meaning):
            print("все ок")
            return
        print("не ок")
        
        




if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
