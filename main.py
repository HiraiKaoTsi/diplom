from os import listdir

# built - in Module
from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets

from datetime import date
from datetime import datetime

from script.module_db import *
# from script.module_word import *

from script.create_ui_element import *

# interface
from interface_ui import Ui_MainWindow


class FunctionalMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Launch method
        self.EditStyleSheet()

        self.CreateBookForInfo(GetAllBooks())
        self.CreateUserForInfo(GetAllUser())

        self.ui.pushButton_back_info_user.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        self.ui.tabWidget.setCurrentIndex(3)
        self.ui.stackedWidget.setCurrentIndex(1)

        # START 1 TAB-MAIN-INFO
        self.ui.label_today_date.setText(f"Сегодняшняя дата - {datetime.strftime(date.today(), '%d.%m.%Y')}")
        self.EditMainInfo()
        self.ui.pushButton_create_report_main_info.clicked.connect(self.onCreateReport)
        # END 1 TAB-MAIN-INFO

        # START 2 TAB-ADD-BOOK
        # self.ui.pushButton_add_new_book.clicked.connect(self.AddNewBook)
        # END 2 TAB-ADD-BOOK

        # START 3 TAB-ADD-NEW-USER

        # END 3 TAB-ADD-NEW-USER

        # START 4 TAB-SEARCH-BOOK
        # self.ui.pushButton_search.clicked.connect(self.SearchBook)
        # END 4 TAB-SEARCH-BOOK

        # START 5 TAB-DEBTORS
        self.ui.pushButton_reset_user.hide()
        self.ui.pushButton_reset_user.clicked.connect(self.ResetTabDebtors)
        # self.ui.radioButton_debtors.clicked.connect(self.)
        # self.ui.radioButton_suitable_delivery.clicked.connect(self.)
        # END 5 TAB-DEBTORS

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

    def EditMainInfo(self) -> None:
        """
        Данный метод отображает информацию из базы данных на главном экране
        """
        self.ui.label_total_number_books.setText(f"{CountBook()}")
        self.ui.label_how_many_given_book.setText(f"{IssuedBookAll()}")
        self.ui.label__how_many_given_book_today.setText(f"{CountIssuedBookToday()}")
        self.ui.label_how_many_debtors.setText(f"{CountQuantityDebtors()}")
        self.ui.label_how_many_return_today.setText(f"{CountReturnBookToday()}")

    def onCreateReport(self) -> None:
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
            "Выдано книг за сегодня:": self.ui.label__how_many_given_book_today.text(),
            "Сколько задолжников:": self.ui.label_how_many_debtors.text(),
            "Сколько книг за сегодня вернуто": self.ui.label_how_many_return_today.text()
        }
        # if CreateReportMainInfo(filename, info):
        #     print("Файл создан!")

    def DetailedInformationAboutUser(self, id_user: int):
        """
        Подробная информация о пользователе
        """
        # Получает информацию из базы данных 
        data = GetAboutUser(id_user)

        # Заполняет первую страничку (информация о пользователе)
        self.ui.lineEdit_fio_info_user.setText(f"{data['FIO']}")
        self.ui.lineEdit_number_group.setText(f"{data['number_group']}")
        self.ui.lineEdit_student_id_number.setText(f"{data['student_id_number']}")
        self.ui.lineEdit_phone.setText(f"{'' if data['number_phone'] is None else data['number_phone']}")
        self.ui.lineEdit_mail.setText(f"{'' if data['email'] is None else data['email']}")
        self.ui.lineEdit_telegram.setText(f"{'' if data['vk'] is None else data['vk']}")
        self.ui.lineEdit_vk.setText(f"{'' if data['telegram'] is None else data['telegram']}")

        # Очистка старой информации
        self.ClearLayoutFromFrame(self.ui.verticalLayout_history_take_bok)
        self.ClearLayoutFromFrame(self.ui.verticalLayout_take_book)

        # Заполнение второй странички (взятые книги)
        data_taken_book = GetInfoBooksTakenUserById(id_user)
        if data_taken_book != ():
            for element in data_taken_book:
                widget = CreateGivedBook(*element)
                self.ui.verticalLayout_take_book.addWidget(widget, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Заполнение третей странички (история взятых книг)
        data_history_take_book = GetInfoHistoryBooksTakenUserById(id_user)
        if data_history_take_book != ():
            for element in data_history_take_book:
                widget = CreateHistoryBook(*element)
                self.ui.verticalLayout_history_take_bok.addWidget(widget, 0,
                                                                  QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Переход на страничку
        self.ui.toolBox.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)

    def CreateBookForInfo(self, data_info_book: tuple[tuple, ...]):
        """
        Создает книги по полученной информации
        """
        if len(data_info_book) == 0:
            return

        for element in data_info_book:
            quantity_issued = GetQuantityBookThatUserHaveById(element[0])
            widget = CreateBook(*element, quantity_issued)
            self.ui.verticalLayout_books.addWidget(widget)

    def CreateUserForInfo(self, data_info_user: tuple[tuple, ...]):
        """
        Создает пользователей по полученной информации
        """
        if len(data_info_user) == 0:
            return

        self.ClearLayoutFromFrame(self.ui.verticalLayout_all_user)

        for element in data_info_user:
            widget = CreateUser(self.DetailedInformationAboutUser, *element)
            self.ui.verticalLayout_all_user.addWidget(widget)


    def ClearLayoutFromFrame(self, layout: QtWidgets.QVBoxLayout):
        """
        Удаляет из введенного layout все виджеты
        """
        #  verticalLayout_all_user - пользователи
        #  verticalLayout_all_message - сообщение пользователям
        #   verticalLayout_books - книги
        if layout is not None:
            for i in range(layout.count()):
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())

    def ResetTabDebtors(self):
        self.ClearLayoutFromFrame(self.ui.verticalLayout_all_user)
        self.CreateUserForInfo(GetAllUser())
        self.ui.pushButton_reset_user.hide()

    def SearchStudent(self, info: int):
        match info:
            case 1:
                self.CreateUserForInfo(GetAllUser())
                self.ui.pushButton_reset_user.hide()
            case 2:
                self.CreateUserForInfo(GetUsersBookDebtors())
                self.ui.pushButton_reset_user.show()
            case 3:
                self.CreateUserForInfo(GetInfoTheyFitDelivery())
                self.ui.pushButton_reset_user.show()
            case 4:
                self.ui.lineEdit_search_user.text().strip()


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
