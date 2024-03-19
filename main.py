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

        self.ui.stackedWidget_book.setCurrentIndex(0)

        # Launch method
        self.EditStyleSheet()
        self.SearchStudent(1)
        self.SearchBook(1)

        # Информация открытого пользователя
        self.info_open_user = None
        # Информация открытой книги
        self.info_open_book = None

        # START 1 TAB-MAIN-INFO
        self.ui.label_today_date.setText(f"Сегодняшняя дата - {datetime.strftime(date.today(), '%d.%m.%Y')}")
        self.ui.pushButton_create_report_main_info.clicked.connect(self.onCreateReport)
        self.EditMainInfo()
        # END 1 TAB-MAIN-INFO

        # START 2 TAB-ADD-BOOK
        self.ui.pushButton_add_new_book.clicked.connect(self.AddNewBook)
        self.ui.pushButton_clear_add_new_book.clicked.connect(self.ClearValueAddBook)
        # END 2 TAB-ADD-BOOK

        # START 3 TAB-ADD-NEW-USER
        self.ui.pushButton_add_user.clicked.connect(self.AddNewUser)
        self.ui.pushButton_clear_add_user.clicked.connect(self.ClearValueAddUser)
        # END 3 TAB-ADD-NEW-USER

        # START 4 TAB-SEARCH-BOOK
        self.ui.pushButton_search_users_for_gb.clicked.connect(self.SearchUsersByGiveBook)
        self.ui.pushButton_reset_gb.hide()
        self.ui.pushButton_reset_gb.clicked.connect(self.ResetTabGiveBook)
        self.ui.label_dont_have_result_give_book.hide()
        self.ui.pushButton_delete_book.clicked.connect(self.DeleteBook)
        self.ui.pushButton_edit_info_book.clicked.connect(self.EditDataBook)
        self.ui.pushButton_back_info_book.clicked.connect(lambda: self.ui.stackedWidget_book.setCurrentIndex(0))
        self.ui.label_dont_have_result_book.hide()
        self.ui.pushButton_reset_book.hide()
        self.ui.radioButton_all_book.setChecked(True)
        self.ui.radioButton_all_book.clicked.connect(lambda: self.SearchBook(1))
        self.ui.radioButton_missing_all.clicked.connect(lambda: self.SearchBook(2))
        self.ui.radioButton_missing.clicked.connect(lambda: self.SearchBook(3))
        self.ui.pushButton_search_book.clicked.connect(lambda: self.SearchBook(4))
        self.ui.lineEdit_search_book.returnPressed.connect(lambda: self.SearchBook(4))
        self.ui.pushButton_reset_book.clicked.connect(self.ResetTabBook)
        # END 4 TAB-SEARCH-BOOK

        # START 5 TAB-DEBTORS
        self.ui.pushButton_back_info_user.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
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
        self.ui.pushButton_open_page_emit_message.clicked.connect(
            lambda: self.OpenPageEmitMessage(self.info_open_user['id'], 0))
        # END 5 TAB-DEBTORS

    def SearchUsersByGiveBook(self):
        input_data = self.ui.lineEdit_info_for_gb.text().strip()

        if not input_data:
            return

        search_data = GetInfoByInputDataUsers(input_data)

        self.ui.pushButton_reset_gb.show()

        if search_data == ():
            self.ui.label_dont_have_result_give_book.show()
            return

        for element in search_data:
            widget = CreateUserGiveBook(self.OpenPageFunctionalUser, self.NextStageGiveBook, *element[0:4])
            self.ui.verticalLayout_found_users.addWidget(widget, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def NextStageGiveBook(self, id_user: int):
        self.ui.stackedWidget_info_whom_givet.setCurrentIndex(1)

    def ResetTabGiveBook(self):
        self.ui.lineEdit_info_for_gb.setText("")
        self.ui.label_dont_have_result_give_book.hide()
        self.ClearLayoutFromFrame(self.ui.verticalLayout_found_users)

    # def GiveBookUser(self):

    def DeleteBook(self):

        choice = DialogChoiceYesOrNo()
        info_choice = choice.OpenDialog("Вы действительно хотите удалить книгу?")
        if info_choice is False:
            return

        info_delete = DeleteBookById(self.info_open_book["id"])
        if info_delete:
            self.info_open_user = None
            notification = DialogNotification()
            notification.OpenDialog("Книга удален")
            self.UpdateAllInfo()
            self.ui.stackedWidget_book.setCurrentIndex(0)

    def ClearValueAddUser(self):
        self.ui.lineEdit_fio_add_user.setText("")
        self.ui.lineEdit_number_group_user.setText("")
        self.ui.lineEdit_student_id_user.setText("")
        self.ui.lineEdit_phon_number_user.setText("")
        self.ui.lineEdit_email_user.setText("")
        self.ui.lineEdit_telegram_user.setText("")
        self.ui.lineEdit_vk_user.setText("")

    def ClearValueAddBook(self):
        self.ui.lineEdit_name_book_add.setText("")
        self.ui.lineEdit_author_add.setText("")
        self.ui.lineEdit_isbn_add.setText("")
        self.ui.dateEdit_year_publication_add.setDate(QtCore.QDate(2000, 1, 1))
        self.ui.spinBox_quantity_add.setValue(0)

    def EditDataBook(self):
        """
        Изменяет информацию о книги 
        """
        all_info = (
            self.ui.lineEdit_name_book.text().strip(),
            self.ui.lineEdit_author_book.text().strip(),
            self.ui.lineEdit_isbn_book.text().strip(),
            self.ui.dateEdit_year_publication_book.dateTime().toString("yyyy"),
            self.ui.spinBox_quantity_book.value(),
        )

        ru_translate_key = {"name_book": "Название книги",
                            "author": "Автор",
                            "ISBN": "ISBN",
                            "year_publication": "Год публикации",
                            "quantity": "Количество",
                            }

        info_edit = {}

        for key_dict, value_tuple in zip(tuple(self.info_open_book.keys())[1:], all_info):
            if value_tuple == "":
                notification = DialogNotification()
                notification.OpenDialog("Нельзя изменить информацию на пустое значение")
                self.OpenPageFunctionalBook(self.info_open_book["id"])
                return

            elif str(self.info_open_book[key_dict]) != str(value_tuple):
                info_edit[key_dict] = value_tuple

        if info_edit == {}:
            return

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
            element += f"<p>{ru_translate_key[key]} с {'___' if self.info_open_book[key] is None else self.info_open_book[key]} изменить на {'___' if info_edit[key] == '' else info_edit[key]}</p>\n"

        text_for_message += element + "</body></html>"

        dialog = DialogEditInfo()
        choice = dialog.OpenDialog(text_for_message)

        if "quantity" in info_edit.keys():
            count_give_book = GetQuantityBookThatUserHaveById(self.info_open_book['id'])
            if count_give_book > info_edit['quantity']:
                notification = DialogNotification()
                notification.OpenDialog(
                    "Изменение не могут быть совершены так как вы изменили количество книг на меньшее чем выданы в "
                    "текущий момент")
                self.OpenPageFunctionalBook(self.info_open_book["id"])
                return
            elif info_edit['quantity'] == 0:
                notification = DialogNotification()
                notification.OpenDialog("Изменение не могут быть совершены так как вы изменили количество книг на 0")
                self.OpenPageFunctionalBook(self.info_open_book["id"])
                return

        if choice is False:
            return

        if UpdateDataBook(self.info_open_book["id"], info_edit):
            notification = DialogNotification()
            notification.OpenDialog("Данные изменены")
            self.OpenPageFunctionalBook(self.info_open_book["id"])
            self.UpdateAllInfo()

    def OpenPageFunctionalBook(self, id_book: int):
        data = GetAboutBookById(id_book)

        self.info_open_book = data

        self.ui.lineEdit_name_book.setText(f"{data['name_book']}")
        self.ui.lineEdit_author_book.setText(f"{data['author']}")
        self.ui.lineEdit_isbn_book.setText(f"{data['ISBN']}")
        self.ui.spinBox_quantity_book.setValue(data['quantity'])
        self.ui.dateEdit_year_publication_book.setDate(QtCore.QDate(data['year_publication'], 1, 1))

        self.ui.stackedWidget_book.setCurrentIndex(1)

        data_info_user = GetHistoryUsersTakeBookById(data["id"])

        for element in data_info_user:
            widget = CreateUserHistoryTakeBook(self.OpenPageFunctionalUser, *element)
            self.ui.verticalLayout_history_user_take_book.addWidget(widget)

    def OpenPageEmitMessage(self, id_user: int, id_page_back: int, social_network: str = ""):

        # Info user
        data = GetAboutUser(id_user)
        self.info_open_user = data

        model = self.ui.comboBox_social_network.model()
        for i in range(model.rowCount()):
            model.item(i).setEnabled(True)

        if data["email"] is None or not data["email"]:
            model.item(1).setEnabled(False)
        if data["telegram"] is None or not data["telegram"]:
            model.item(2).setEnabled(False)
        if data["vk"] is None or not data["vk"]:
            model.item(3).setEnabled(False)

        self.ui.pushButton_back_message.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(id_page_back))

        match social_network:
            case "":
                self.ui.comboBox_social_network.setCurrentIndex(0)
            case "email":
                self.ui.comboBox_social_network.setCurrentIndex(1)
            case "telegram":
                self.ui.comboBox_social_network.setCurrentIndex(2)
            case "vk":
                self.ui.comboBox_social_network.setCurrentIndex(3)

        self.ui.textEdit_message.setText("")

        self.ClearLayoutFromFrame(self.ui.verticalLayout_all_message)

        data_message = GetAllHistoryMessageUsers(data["id"])

        for element in data_message:
            widget = CreateMessage(*element)
            self.ui.verticalLayout_all_message.addWidget(widget)

        self.ui.label_fio_message.setText(f"{data['FIO']}")
        self.ui.label_number_group_message.setText(f"{data['number_group']}")

        self.ui.stackedWidget.setCurrentIndex(2)

    def SearchBook(self, info: int):
        match info:
            case 1:
                self.CreateBookForInfo(GetAllBooks())
                self.ui.pushButton_reset_book.hide()
            case 2:
                self.CreateBookForInfo(GetBookWhichAllMissing())
                self.ui.pushButton_reset_book.show()
            case 3:
                self.CreateBookForInfo(GetBookNotAllMissing())
                self.ui.pushButton_reset_book.show()
            case 4:
                input_data_book = self.ui.lineEdit_search_book.text().strip()
                if not input_data_book:
                    return
                self.CreateBookForInfo(GetInfoByInputDataBook(input_data_book))
                self.ui.frame_radioButton_book.hide()
                self.ui.pushButton_reset_book.show()

    def ReturnBook(self, id_book: int, name_book: str):

        choice = DialogChoiceYesOrNo()
        info_choice = choice.OpenDialog(
            f"Подтвердите действие пользователь - '{self.info_open_user['FIO']}' вернул книгу - '{name_book}'")

        if info_choice is False:
            return

        if UpdateReturnBook(self.info_open_user["id"], id_book):
            notification = DialogNotification()
            notification.OpenDialog("Информация успешно обновилась!")

            self.OpenPageFunctionalUser(self.info_open_user["id"])
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

    def AddNewUser(self):
        fio = self.ui.lineEdit_fio_add_user.text().strip()
        number_group = self.ui.lineEdit_number_group_user.text().strip()
        student_id = self.ui.lineEdit_student_id_user.text().strip()
        number_phone = self.ui.lineEdit_phon_number_user.text().strip()
        email = self.ui.lineEdit_email_user.text().strip()
        telegram = self.ui.lineEdit_telegram_user.text().strip()
        vk = self.ui.lineEdit_vk_user.text().strip()

        if (not fio) or (not number_group) or (not student_id):
            notification = DialogNotification()
            notification.OpenDialog(
                "Заполните основную информацию для создание пользователя\n(ФИО, номер группы, студенческий билет)")
            return

        status = InsertNewUser((fio, number_group, student_id, number_phone, email, telegram, vk))
        if status:
            notification = DialogNotification()
            notification.OpenDialog("Студент успешно зарегистрирован!")

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

        if self.ui.lineEdit_fio_info_user.text().strip() == "":
            notification = DialogNotification()
            notification.OpenDialog("Нельзя изменить ФИО на пустое значение")
            self.OpenPageFunctionalUser(self.info_open_user["id"])
            return

        if self.ui.lineEdit_number_group.text().strip() == "":
            notification = DialogNotification()
            notification.OpenDialog("Нельзя изменить номер группы на пустое значение")
            self.OpenPageFunctionalUser(self.info_open_user["id"])
            return

        if self.ui.lineEdit_student_id_number.text().strip() == "":
            notification = DialogNotification()
            notification.OpenDialog("Нельзя изменить студенческий билет на пустое значение")
            self.OpenPageFunctionalUser(self.info_open_user["id"])
            return

        for key_dict, value_tuple in zip(tuple(self.info_open_user.keys())[1:], all_info):
            if self.info_open_user[key_dict] is None and value_tuple == "":
                continue

            elif str(self.info_open_user[key_dict]) != str(value_tuple):
                info_edit[key_dict] = value_tuple

        if info_edit == {}:
            return

        ru_translate_key = {"FIO": "ФИО",
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
            element += f"<p>{ru_translate_key[key]} с {'___' if self.info_open_user[key] is None else self.info_open_user[key]} изменить на {'___' if info_edit[key] == '' else info_edit[key]}</p>\n"

        text_for_message += element + "</body></html>"

        dialog = DialogEditInfo()
        choice = dialog.OpenDialog(text_for_message)

        if choice is False:
            self.OpenPageFunctionalUser(self.info_open_user["id"])
            return

        if UpdateDataUser(self.info_open_user["id"], info_edit):
            notification = DialogNotification()
            notification.OpenDialog("Данные изменены")
            self.OpenPageFunctionalUser(self.info_open_user["id"])
            self.UpdateAllInfo()

    # edit next
    def UpdateAllInfo(self):
        """
        Запускает все методы для обновления информации на экране
        """
        # требуется перезагрузка открытого окна информации пользователя книги если произошло удаление данных
        # также перезагрузка нужна там где осуществляется поиск информации кому выдать книгу
        self.EditMainInfo()

        self.CreateBookForInfo(GetAllBooks())
        self.ResetTabBook()

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
        self.ui.label_total_number_books.setText(f"{GetCountBook()}")
        self.ui.label_how_many_given_book.setText(f"{GetCountIssuedBookAll()}")
        self.ui.label__how_many_given_book_today.setText(f"{GetCountIssuedBookToday()}")
        self.ui.label_how_many_debtors.setText(f"{GetCountQuantityDebtors()}")
        self.ui.label_how_many_return_today.setText(f"{GetCountReturnBookToday()}")

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
            "Сколько книг вернуто за сегодня:": self.ui.label_how_many_return_today.text()
        }
        if CreateReportMainInfo(filename, info):
            notification = DialogNotification()
            notification.OpenDialog("Файл успешно создан!")

    def OpenPageFunctionalUser(self, id_user: int):
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
                widget = CreateGivetBook(*element, self.ReturnBook)
                self.ui.verticalLayout_take_book.addWidget(widget, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Заполнение третей странички (история взятых книг)
        data_history_take_book = GetInfoHistoryBooksTakenUserById(id_user)
        if data_history_take_book != ():
            for element in data_history_take_book:
                widget = CreateHistoryBook(*element)
                self.ui.verticalLayout_history_take_bok.addWidget(widget, 0,
                                                                  QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Кнопка написать сообщение
        self.ui.pushButton_open_page_emit_message.setEnabled(True)
        if (data['email'] is None or not data['email']) and (data['telegram'] is None or not data['telegram']) and (
                data['vk'] is None or not data['vk']):
            self.ui.pushButton_open_page_emit_message.setEnabled(False)

        # Переход на страничку
        self.ui.toolBox.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.tabWidget.setCurrentIndex(4)

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

        if data_info_book == ():
            self.ui.label_dont_have_result_book.show()
            return

        self.ui.label_dont_have_result_book.hide()

        print(data_info_book)
        for element in data_info_book:
            widget = CreateBook(self.OpenPageFunctionalBook, *element)
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
            widget = CreateUser(self.OpenPageFunctionalUser, self.OpenPageEmitMessage, *element)
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

    def ResetTabBook(self):
        self.SearchBook(1)
        self.ui.lineEdit_search_book.setText("")
        self.ui.radioButton_all_book.setChecked(True)
        self.ui.pushButton_reset_book.hide()
        self.ui.label_dont_have_result_book.hide()
        self.ui.frame_radioButton_book.show()

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
                self.CreateUserForInfo(GetInfoByInputDataUsers(input_data_user))
                self.ui.pushButton_reset_user.show()
                self.ui.frame_radioButton_users.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
