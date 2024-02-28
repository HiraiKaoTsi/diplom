from os import listdir

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
        
        # Launch method
        self.EditSyleSheet()
        self.CreateUserForInfo(())

        self.ui.pushButton_back_info_user.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        self.ui.tabWidget.setCurrentIndex(4)
        self.ui.stackedWidget.setCurrentIndex(1)

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
        
    def EditSyleSheet(self) -> None:
        """
        Данный метод считывает файлы .qss в катологе style и применяет их к приложению 
        """
        style = ""
        for qss_file in listdir("style"):
            with open(f"style/{qss_file}", mode="r", encoding="utf-8") as qss:
                style += qss.read()

        self.setStyleSheet(style)
        QtWidgets.qApp.setStyleSheet(style)


    def EdimMainInfo(self):
        """
        Данный метод отображает информацию из базы данных на галвном экране
        """
        self.ui.label_total_number_books.setText(f"{CountBook()}")
        self.ui.label_how_many_given_book.setText(f"{IssuedBookAll()}")
        self.ui.label__how_many_given_book_today.setText(f"{CountIssuedBookToday()}")
        self.ui.label_how_many_debtors.setText(f"{CountQuantityDebtors()}") 
        self.ui.label_how_many_return_today.setText(f"{CountReturnBookToday()}")


    def onCreateReport(self):
        """
        Данный метод создает docx файл и заполняет его информацией с главного окна
        """
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

    
    def DetailedInformationAboutUser(self, id_user):
        """
        Подробная информация о пользователе
        """
        data = GetAboutUser(id_user)
        self.ui.lineEdit_fio_info_user.setText(f"{data['FIO']}")
        self.ui.lineEdit_number_group.setText(f"{data['number_group']}")
        self.ui.lineEdit_student_id_number.setText(f"{data['student_id_number']}")

        self.ui.lineEdit_phone.setText(f"{'' if data['number_phone'] is None else data['number_phone']}")
        self.ui.lineEdit_mail.setText(f"{'' if data['email'] is None else data['email']}")
        self.ui.lineEdit_telegram.setText(f"{'' if data['vk'] is None else data['vk']}")
        self.ui.lineEdit_vk.setText(f"{'' if data['telegram'] is None else data['telegram']}")


        self.ui.stackedWidget.setCurrentIndex(0)

    def CreateUserForInfo(self, data_info_user: tuple[dict, ...]):
        # if len(data_info_user) == 0:
        #     return
        data_info_user = GetAllUser()
        for element in data_info_user:
            widget = CreateUser(self.DetailedInformationAboutUser, *element)
            self.ui.verticalLayout_all_user.addWidget(widget)

        # self.ClearLayoutFromFrame(self.ui.verticalLayout_all_user)

    def ClearLayoutFromFrame(self, layout: QtWidgets.QVBoxLayout):
        #  verticalLayout_all_user - пользователи
        #  verticalLayout_all_message - сообщение пользователям

        # verticalLayout_books - книги 
        print(type(layout))
        if layout is not None:
            for i in range(layout.count()):
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())


    def OpenAllInfoUser(self, id_user, fio, number_group, student_id_number):
        self.ui.label_fio_info_user.setText(f"{fio}")
        self.ui.label_number_group.setText(f"{number_group}")
        self.ui.label_student_id_number.setText(f"{student_id_number}")
        self.ui.stackedWidget.setCurrentIndex(0)
        print(id_user)
            


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
