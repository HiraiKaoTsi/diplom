from os import listdir

# built - in Module
from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets

from datetime import date
from datetime import datetime

from script.module_db import *
from script.module_word import *

from script.create_ui_element import *

# interface
from interface_ui import Ui_MainWindow

# dialog
from script.dialog_widget import *


class FunctionalMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Launch method
        self.EditStyleSheet()

        self.CreateBookForInfo(GetAllBooks())
        self.CreateUserForInfo(GetAllUser())


        # init value
        # Id какого пользователя открыто в подробной инфорамации
        self.info_open_user = None

        self.ui.pushButton_back_info_user.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        self.ui.tabWidget.setCurrentIndex(3)
        self.ui.stackedWidget.setCurrentIndex(1)

        # START 1 TAB-MAIN-INFO
        self.ui.label_today_date.setText(f"Сегодняшняя дата - {datetime.strftime(date.today(), '%d.%m.%Y')}")
        self.EditMainInfo()
        self.ui.pushButton_create_report_main_info.clicked.connect(self.onCreateReport)
        # END 1 TAB-MAIN-INFO

        # START 2 TAB-ADD-BOOK
        self.ui.pushButton_add_new_book.clicked.connect(self.AddNewBook)
        # END 2 TAB-ADD-BOOK

        # START 3 TAB-ADD-NEW-USER
        self.ui.pushButton_add_user.clicked.connect(self.CreateNewUser)
        # END 3 TAB-ADD-NEW-USER

        # START 4 TAB-SEARCH-BOOK
        # self.ui.pushButton_search.clicked.connect(self.SearchBook)
        # END 4 TAB-SEARCH-BOOK

        # START 5 TAB-DEBTORS
        self.ui.pushButton_delete_user.clicked.connect(self.DeleteUser)
        self.ui.radioButton_all_users.setChecked(True)
        self.ui.pushButton_reset_user.hide()
        self.ui.label_dont_have_result_user.hide()
        self.ui.pushButton_reset_user.clicked.connect(self.ResetTabDebtors)
        self.ui.radioButton_all_users.clicked.connect(lambda: self.SearchStudent(1))
        self.ui.radioButton_user_take_book.clicked.connect(lambda: self.SearchStudent(2))
        self.ui.radioButton_debtors.clicked.connect(lambda: self.SearchStudent(3))
        self.ui.radioButton_suitable_delivery.clicked.connect(lambda: self.SearchStudent(4))
        self.ui.lineEdit_search_user.returnPressed.connect(lambda: self.SearchStudent(5))
        self.ui.pushButton_search_user.clicked.connect(lambda: self.SearchStudent(5))
        self.ui.pushButton_edit_info_user.clicked.connect(self.EditDataUser)
        # END 5 TAB-DEBTORS

    def ReturnBook(self, id_book: int, name_book: str):
        
        choice = DialogChoiceYesOrNo()
        info_choice = choice.OpenDialog(f"Подтвердите действие пользователь - '{self.info_open_user['FIO']}' вернул книгу - '{name_book}'")

        if info_choice is False:
            return

        if UpdateReturnBook(self.info_open_user["id"], id_book):
            notification = DialogNotification()
            notification.OpenDialog("Информация успешно обновилась!")

            self.DetailedInformationAboutUser(self.info_open_user["id"])
            self.ui.toolBox.setCurrentIndex(1)
            self.UpdateAllInfo()


    def AddNewBook(self):
        name = self.ui.lineEdit_name_book_add.text().strip()
        author = self.ui.lineEdit_author_add.text().strip()
        isbn = self.ui.lineEdit_isbn_add.text().strip()
        year = self.ui.dateEdit_year_publication_add.dateTime().toString("yyyy")
        quantity = self.ui.spinBox_quantity_add.value()

        if (not name) or (not author) or (not isbn) or (quantity == 0):
            notification = DialogNotification()
            notification.OpenDialog("Заполните всю информацию!")
            return
    
        status = InsertNewBooks((name, author, isbn, year, quantity))
        if status:
            notification = DialogNotification()
            notification.OpenDialog("Новая книга успешно добавлена!")

            self.ui.lineEdit_name_book_add.setText("")
            self.ui.lineEdit_author_add.setText("")
            self.ui.lineEdit_isbn_add.setText("")
            self.ui.dateEdit_year_publication_add.setDate(QtCore.QDate(2000, 1, 1))
            self.ui.spinBox_quantity_add.setValue(0)

            self.UpdateAllInfo()


    def CreateNewUser(self):
        fio = self.ui.lineEdit_fio_add_user.text().strip()
        number_group = self.ui.lineEdit_number_group_user.text().strip()
        student_id = self.ui.lineEdit_student_id_user.text().strip()
        number_phone = self.ui.lineEdit_phon_number_user.text().strip()
        email = self.ui.lineEdit_email_user.text().strip()
        telegram = self.ui.lineEdit_telegram_user.text().strip()
        vk = self.ui.lineEdit_vk_user.text().strip()

        if (not fio) or (not number_group) or (not student_id):
            notification = DialogNotification()
            notification.OpenDialog("Заполните основную информацию для создание пользователя\n(ФИО, номер группы, студенческий билет)")
            return

        status = InsertNewUser((fio, number_group, student_id, number_phone, email, telegram, vk))
        if status:
            notification = DialogNotification()
            notification.OpenDialog("Студент успешно зареегестрирован!")

            self.ui.lineEdit_fio_add_user.setText("")
            self.ui.lineEdit_number_group_user.setText("")
            self.ui.lineEdit_student_id_user.setText("")
            self.ui.lineEdit_phon_number_user.setText("")
            self.ui.lineEdit_email_user.setText("")
            self.ui.lineEdit_telegram_user.setText("")
            self.ui.lineEdit_vk_user.setText("")

            self.UpdateAllInfo()


    def EditDataUser(self):
        """
        Изменяет информацию о студенте
        """

        all_info = (
            self.ui.lineEdit_fio_info_user.text().strip(),
            self.ui.lineEdit_number_group.text().strip(),
            self.ui.lineEdit_student_id_number.text().strip(),
            self.ui.lineEdit_phone.text().strip(),
            self.ui.lineEdit_mail.text().strip(),
            self.ui.lineEdit_telegram.text().strip(),
            self.ui.lineEdit_vk.text().strip(),
        )

        info_edit = {}

        for key_dict, value_tuple in zip(tuple(self.info_open_user.keys())[1:], all_info):
            if self.info_open_user[key_dict] is None and value_tuple == "":
                continue
   
            elif (str(self.info_open_user[key_dict]) != value_tuple):
                info_edit[key_dict] = value_tuple
        
        if info_edit == {}:
            return
                
        ru_translete_key = {"FIO": "ФИО",
                            "number_group": "Номер группы",
                            "student_id_number": "Студенческий билет",
                            "number_phone": "Номер телефона",
                            "email": "Почта",
                            "telegram": "Telegram",
                            "vk": "Vk",
        }
        
        text_for_message = """
        <html>
        <head>
            <style>
                p {
                    line-height: 10px;
                }
            </style>
        </head>
        <body>
            <p>Изменить данные?</p>

        """
        element = ""
        for key in info_edit.keys():
            element += f"<p>{ru_translete_key[key]} с {'___' if self.info_open_user[key] is None else self.info_open_user[key]} изменить на {'___' if info_edit[key] == '' else info_edit[key]}</p>\n"
        
        text_for_message += element + "</body></html>"

        dialog = DialogEditInfo()
        choice = dialog.OpenDialog(text_for_message)

        if choice is False:
            return
        
        if EditDataUser(self.info_open_user["id"], info_edit):
            notification = DialogNotification()
            notification.OpenDialog("Данные изменены")
            self.DetailedInformationAboutUser(self.info_open_user["id"])
            self.UpdateAllInfo()
        
        
        

    def UpdateAllInfo(self):
        """
        Запускает все методы для обновление информации на экране
        """
        self.EditMainInfo()
        
        self.CreateBookForInfo(GetAllBooks())

        self.ResetTabDebtors()
        self.CreateUserForInfo(GetAllUser())


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
        if CreateReportMainInfo(filename, info):
            notification = DialogNotification()
            notification.OpenDialog("Файл успешно создан!")

    def DetailedInformationAboutUser(self, id_user: int):
        """
        Подробная информация о пользователе
        """
        # Получает информацию из базы данных 
        data = GetAboutUser(id_user)
        
        self.info_open_user = data

        # Заполняет первую страничку (информация о пользователе)
        self.ui.lineEdit_fio_info_user.setText(f"{data['FIO']}")
        self.ui.lineEdit_number_group.setText(f"{data['number_group']}")
        self.ui.lineEdit_student_id_number.setText(f"{data['student_id_number']}")
        self.ui.lineEdit_phone.setText(f"{'' if data['number_phone'] is None else data['number_phone']}")
        self.ui.lineEdit_mail.setText(f"{'' if data['email'] is None else data['email']}")
        self.ui.lineEdit_telegram.setText(f"{'' if data['telegram'] is None else data['telegram']}")
        self.ui.lineEdit_vk.setText(f"{'' if data['vk'] is None else data['vk']}")

        # Очистка старой информации
        self.ClearLayoutFromFrame(self.ui.verticalLayout_history_take_bok)
        self.ClearLayoutFromFrame(self.ui.verticalLayout_take_book)

        # Заполнение второй странички (взятые книги)
        data_taken_book = GetInfoBooksTakenUserById(id_user)
        if data_taken_book != ():
            for element in data_taken_book:
                widget = CreateGivedBook(*element, self.ReturnBook)
                self.ui.verticalLayout_take_book.addWidget(widget, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Заполнение третей странички (история взятых книг)
        data_history_take_book = GetInfoHistoryBooksTakenUserById(id_user)
        if data_history_take_book != ():
            for element in data_history_take_book:
                widget = CreateHistoryBook(*element)
                self.ui.verticalLayout_history_take_bok.addWidget(widget, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Переход на страничку
        self.ui.toolBox.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)


    def DeleteUser(self):
        choice = DialogChoiceYesOrNo()
        info_choice = choice.OpenDialog("Вы действительно хотите удалить пользователя?")
        if info_choice is False:
            return
        
        info_delete = DeleteUserById(self.info_open_user["id"])
        if info_delete:
            self.info_open_user = None
            notification = DialogNotification()
            notification.OpenDialog("Пользователь удален")
            self.UpdateAllInfo()
            self.ui.stackedWidget.setCurrentIndex(1)        

    def CreateBookForInfo(self, data_info_book: tuple[tuple, ...]):
        """
        Создает книги по полученной информации
        """

        self.ClearLayoutFromFrame(self.ui.verticalLayout_books)

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
        self.ClearLayoutFromFrame(self.ui.verticalLayout_all_user)

        if data_info_user == ():
            self.ui.label_dont_have_result_user.show()
            return
        
        self.ui.label_dont_have_result_user.hide()

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
        self.SearchStudent(1)
        self.ui.lineEdit_search_user.setText("")
        self.ui.radioButton_all_users.setChecked(True)
        self.ui.pushButton_reset_user.hide()
        self.ui.label_dont_have_result_user.hide()
        self.ui.frame_radioButton_users.show()


    def SearchStudent(self, info: int):
        match info:
            case 1:
                self.CreateUserForInfo(GetAllUser())
                self.ui.pushButton_reset_user.hide()
            case 2:
                self.CreateUserForInfo(GetUsersTakesBook())
                self.ui.pushButton_reset_user.show()
            case 3:
                self.CreateUserForInfo(GetUsersBookDebtors())
                self.ui.pushButton_reset_user.show()
            case 4:
                self.CreateUserForInfo(GetInfoTheyFitDelivery())
                self.ui.pushButton_reset_user.show()
            case 5:
                input_data_user = self.ui.lineEdit_search_user.text().strip()
                if not input_data_user:
                    return
                self.CreateUserForInfo(GetInfoByInputData(input_data_user))
                self.ui.pushButton_reset_user.show()
                self.ui.frame_radioButton_users.hide()
                self.ui.radioButton_all_users.setChecked(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
