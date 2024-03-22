from PyQt5 import QtCore, QtWidgets

# interface
from .edit_ui import Ui_DialogEdit


class DialogEditInfo(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_DialogEdit()
        self.ui.setupUi(self)

        self.ui.pushButton_edit.clicked.connect(self.onEdit)
        self.ui.pushButton_cancel.clicked.connect(self.onCancel)

        # Переменная хранит данные о выборе пользователя
        self.info_choice = False

    def OpenDialog(self, old_data: dict, new_data: dict) -> bool:
        """
        Открытия диалогового окна
        :param old_data: старая информация
        :param new_data: новая информация
        :return: True сли пользователь подтвердил изменение False во всех других случаях
        """

        ru_translate_key = {
            "name_book": "Название книги",
            "author": "Автор",
            "ISBN": "ISBN",
            "year_publication": "Год публикации",
            "quantity": "Количество",
            "FIO": "ФИО",
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
        for key in new_data.keys():
            element += (f"<p>{ru_translate_key[key]} с {'___' if old_data[key] is None else old_data[key]} "
                        f"изменить на {'___' if new_data[key] == '' else new_data[key]}</p>\n")

        text_for_message += element + "</body></html>"

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
