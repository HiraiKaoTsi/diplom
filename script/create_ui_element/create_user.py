from PyQt5 import QtCore, QtGui, QtWidgets


class CreateUser(QtWidgets.QFrame):
    """
    Создает виджет QFrame по полученной информации
    """
    def __init__(self, details_user, id_user, fio, number_group, student_id_number, number_phone=None, email=None, vk=None, telegram=None):
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

        # Стуленческий билет
        label_student_id_number = QtWidgets.QLabel(self)
        label_student_id_number.setText(f"{student_id_number}")
        label_student_id_number.setWordWrap(True)
        label_student_id_number.setObjectName("label_student_id_number")
        gridLayout.addWidget(label_student_id_number, 2, 0, 1, 3)

        if number_phone is not None:
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
        pushButton_mail.setMaximumSize(QtCore.QSize(64, 64))
        pushButton_mail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_mail.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/socialNetwork/email.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_mail.setIcon(icon1)
        pushButton_mail.setIconSize(QtCore.QSize(32, 32))
        pushButton_mail.setObjectName("pushButton_mail")
        horizontalLayout.addWidget(pushButton_mail)
        
        # Кнопка VK
        pushButton_vk = QtWidgets.QPushButton(frame_button)
        pushButton_vk.setMaximumSize(QtCore.QSize(64, 64))
        pushButton_vk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_vk.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/socialNetwork/vk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_vk.setIcon(icon2)
        pushButton_vk.setIconSize(QtCore.QSize(32, 32))
        pushButton_vk.setObjectName("pushButton_vk")
        horizontalLayout.addWidget(pushButton_vk)

        # Кнопка telegram
        pushButton_telegram = QtWidgets.QPushButton(frame_button)
        pushButton_telegram.setMaximumSize(QtCore.QSize(64, 64))
        pushButton_telegram.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pushButton_telegram.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/socialNetwork/telegram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_telegram.setIcon(icon3)
        pushButton_telegram.setIconSize(QtCore.QSize(32, 32))
        pushButton_telegram.setObjectName("pushButton_telegram")
        horizontalLayout.addWidget(pushButton_telegram)

        # Кнопка подробная информация
        pushButton_all_info = QtWidgets.QPushButton(self)
        pushButton_all_info.setText("Подробная информация")
        pushButton_all_info.clicked.connect(lambda: details_user(id_user))
        pushButton_all_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/main/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_all_info.setIcon(icon)
        pushButton_all_info.setIconSize(QtCore.QSize(25, 25))
        pushButton_all_info.setObjectName("pushButton_all_info")
        gridLayout.addWidget(pushButton_all_info, 4, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
       
        if email is None:
            pushButton_mail.setEnabled(False)
        if vk is None:
            pushButton_vk.setEnabled(False)
        if telegram is None:
            pushButton_telegram.setEnabled(False)
    
