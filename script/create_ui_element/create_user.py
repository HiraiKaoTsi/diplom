from PyQt5 import QtCore, QtGui, QtWidgets
from collections.abc import Callable


class CreateUser(QtWidgets.QFrame):
    """
    Создает виджет QFrame пользователь по полученной информации
    """
    def __init__(self, function_details_user: Callable, functional_open_message: Callable,
                 id_user: int, fio: str, number_group: str, student_id_number: str,
                 number_phone=None, email=None):
        """
        :param function_details_user: функция для открытия подробной информации пользователя
        с аргументом на id пользователя
        :param functional_open_message: функция для открытия истории сообщений отправленные пользователю
        с аргументом на id пользователя, id на страницу для функции назад, и текс социальной сети (email, vk, telegram),
        которой открыта меню отправки сообщений
        :param id_user: id пользователя
        :param fio: ФИО пользователя
        :param number_group: Номер группы
        :param student_id_number: номер студенческого билета
        :param number_phone: номер телефона
        :param email: почтовый адрес
        :param telegram: ссылка телеграм
        :param vk: ссылка вк
        """
        super().__init__()
        
        # Настройка самого виджета
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame-user")

        # Сетка для виджета
        gridLayout = QtWidgets.QGridLayout(self)
        gridLayout.setContentsMargins(25, 25, 25, 5)
        gridLayout.setSpacing(5)
        gridLayout.setObjectName("gridLayout")

        # ФИО студента
        label_fio = QtWidgets.QLabel(self)
        label_fio.setText(f"{fio}")
        label_fio.setWordWrap(True)
        label_fio.setObjectName("label_fio")
        gridLayout.addWidget(label_fio, 0, 0, 1, 3)

        # Номер группы
        label_number_group = QtWidgets.QLabel(self)
        label_number_group.setText(f"{number_group}")
        label_number_group.setWordWrap(True)
        label_number_group.setObjectName("label_number_group")
        gridLayout.addWidget(label_number_group, 1, 0, 1, 3)

        # Студенческий билет
        label_student_id_number = QtWidgets.QLabel(self)
        label_student_id_number.setText(f"{student_id_number}")
        label_student_id_number.setWordWrap(True)
        label_student_id_number.setObjectName("label_student_id_number")
        gridLayout.addWidget(label_student_id_number, 2, 0, 1, 3)

        if (number_phone is not None) and (number_phone != ""):
            # Frame для номера телефона
            frame_phone = QtWidgets.QFrame(self)
            frame_phone.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame_phone.setFrameShadow(QtWidgets.QFrame.Raised)
            frame_phone.setObjectName("frame_phone")

            # Сетка для frame номера телефона
            horizontalLayout_phone = QtWidgets.QHBoxLayout(frame_phone)
            horizontalLayout_phone.setContentsMargins(0, 0, 0, 0)
            horizontalLayout_phone.setSpacing(4)
            horizontalLayout_phone.setObjectName("horizontalLayout_phone")
            gridLayout.addWidget(frame_phone, 3, 0, 1, 1)

            # Иконка телефона
            label_icon_phone = QtWidgets.QLabel(frame_phone)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(label_icon_phone.sizePolicy().hasHeightForWidth())
            label_icon_phone.setSizePolicy(sizePolicy)
            label_icon_phone.setMaximumSize(QtCore.QSize(40, 40))
            label_icon_phone.setText("")
            label_icon_phone.setTextFormat(QtCore.Qt.AutoText)
            label_icon_phone.setPixmap(QtGui.QPixmap(":/icons/socialNetwork/phone.png"))
            label_icon_phone.setScaledContents(True)
            label_icon_phone.setObjectName("label_icon_phone")
            horizontalLayout_phone.addWidget(label_icon_phone, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

            # Номер телефона
            label_phone_number = QtWidgets.QLabel(frame_phone)
            label_phone_number.setText(f"{number_phone}")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(label_phone_number.sizePolicy().hasHeightForWidth())
            label_phone_number.setSizePolicy(sizePolicy)
            label_phone_number.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            label_phone_number.setObjectName("label_phone_number")
            horizontalLayout_phone.addWidget(label_phone_number)

        # Frame для кнопок
        frame_button = QtWidgets.QFrame(self)
        frame_button.setMinimumSize(QtCore.QSize(151, 42))
        frame_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_button.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_button.setObjectName("frame_button")
        gridLayout.addWidget(frame_button, 3, 1, 1, 2, QtCore.Qt.AlignRight)

        # Сетка для frame кнопок
        horizontalLayout = QtWidgets.QHBoxLayout(frame_button)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(5)
        horizontalLayout.setObjectName("horizontalLayout")

        # Кнопка email
        pushButton_mail = QtWidgets.QPushButton(frame_button)
        pushButton_mail.clicked.connect(lambda: functional_open_message(id_user, 1, "email"))
        pushButton_mail.setMaximumSize(QtCore.QSize(64, 64))
        pushButton_mail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_mail.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/socialNetwork/email.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_mail.setIcon(icon1)
        pushButton_mail.setIconSize(QtCore.QSize(32, 32))
        pushButton_mail.setObjectName("pushButton_mail")
        horizontalLayout.addWidget(pushButton_mail)
        
        # Кнопка sms
        pushButton_phone_sms = QtWidgets.QPushButton(frame_button)
        pushButton_phone_sms.clicked.connect(lambda: functional_open_message(id_user, 1, "sms"))
        pushButton_phone_sms.setMaximumSize(QtCore.QSize(64, 64))
        pushButton_phone_sms.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_phone_sms.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/socialNetwork/phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_phone_sms.setIcon(icon2)
        pushButton_phone_sms.setIconSize(QtCore.QSize(32, 32))
        pushButton_phone_sms.setObjectName("pushButton_phone_sms")
        horizontalLayout.addWidget(pushButton_phone_sms)


        # Кнопка подробная информация
        pushButton_all_info = QtWidgets.QPushButton(self)
        pushButton_all_info.setText("Подробная информация")
        pushButton_all_info.clicked.connect(lambda: function_details_user(id_user))
        pushButton_all_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/main/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_all_info.setIcon(icon)
        pushButton_all_info.setIconSize(QtCore.QSize(25, 25))
        pushButton_all_info.setObjectName("pushButton_all_info")
        gridLayout.addWidget(pushButton_all_info, 4, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)

        # Выключение кнопок если информации нет
        if email is None or not email:
            pushButton_mail.setEnabled(False)
        if number_phone is None or not number_phone:
            pushButton_phone_sms.setEnabled(False)

