# built - in Module
from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets

from datetime import  date
from datetime import datetime


from script.module_db import *
from script.module_word import *

from script.create_ui_element import *



# interface
from interface import Ui_MainWindow


class FunctionalMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # START TAB-MAIN-INFO
        self.ui.label_today_date.setText(f"Сегодняшняя дата - {datetime.strftime(date.today(), '%d.%m.%Y')}")
        self.EdimMainInfo()
        self.ui.pushButton_create_report_main_info.clicked.connect(self.onCreateReport)
        # END TAB-MAIN-INFO

        # START TAB-ADD-BOOK
        # self.ui.pushButton_add_new_book.clicked.connect(self.AddNewBook)
        # END TAB-ADD-BOOK

        # START TAB-ADD-NEW-USER

        # END TAB-ADD-NEW-USER


        # START TAB-SEARCH-BOOK
        # self.ui.pushButton_search.clicked.connect(self.SearchBook)
        # END TAB-SEARCH-BOOK
        
    def EdimMainInfo(self):
        self.ui.label_total_number_books.setText(f"{CountBook()}")
        self.ui.label_how_many_given_book.setText(f"{IssuedBookAll()}")
        self.ui.label__how_many_given_book_today.setText(f"{NumberBooksIssuedToday()}")
        self.ui.label_how_many_debtors.setText(f"{QuantityDebtors()}") 
        self.ui.label_how_many_return_today.setText(f"{CountReturnBookToday()}")


    def onCreateReport(self):
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self,
                            "Сохранить файл",
                            ".",
                            "All Files(*.docx)")
        if not filename:
            return
        info = {
            "Общее количество книг:": self.ui.label_total_number_books.text(),
            "Сколько всего книг выдано:": self.ui.label_how_many_given_book.text(),
            "Выданно книг за сегодня:": self.ui.label__how_many_given_book_today.text(),
            "Сколько задолжников:": self.ui.label_how_many_debtors.text(),
            "Сколько книг за сегодня вернуто": self.ui.label_how_many_return_today.text()
        }
        if CreateReportMainInfo(filename, info):
            print("Файл создан!")

    # def AddNewBook(self):
        
    #     meaning = \
    #     [
    #         self.ui.lineEdit_name_book_add.text().strip(), self.ui.lineEdit_author_add.text().strip(), 
    #         self.ui.lineEdit_isbn_add.text().strip(), self.ui.lineEdit_year_publication_add.text().strip(), 
    #         self.ui.lineEdit_quantity_book_add.text().strip()
    #     ]

    #     for value in meaning:
    #         if not value:
    #             print("Заполните данные")
    #             return
        
    #     if AddNewBook(*meaning):
    #         print("все ок")
    #         return
    #     print("не ок")
        

    # def SearchBook(self):
    #     value_search = self.ui.lineEdit_search.text().strip()
    #     if not value_search:
    #         print("введите данные")
    #         return
            
    #     info = TakeInfoAboutBook(value_search)
    #     print(info)
    #     for element in info:
    #         print(element)
    #         have_or_no = CheckTheRemainedBook(element[0])
    #         print(have_or_no)
    #         print(*element)
    #         ui_frame = CreateFrameBook(*element, have_or_no)
    #         # print(ui_frame)
    #         self.ui.verticalLayout_6.addWidget(ui_frame)
            


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
