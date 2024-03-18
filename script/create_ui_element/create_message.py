from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

class CreateMessage(QtWidgets.QFrame):
    def __init__(self, date_emit: datetime.date, text: str, social_network: str):
        super().__init__()
        
        # Настройка самого виджета
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame-message")

        # Сетка для виджета
        gridLayout = QtWidgets.QGridLayout(self)
        gridLayout.setContentsMargins(25, 25, 25, 25)
        gridLayout.setHorizontalSpacing(4)
        gridLayout.setVerticalSpacing(3)
        gridLayout.setObjectName("gridLayout")

        # Иконка в какой месенджер было отправлено сообщение
        label_icon_social_network = QtWidgets.QLabel(self)

        if social_network == "email":
            label_icon_social_network.setPixmap(QtGui.QPixmap(":/icons/socialNetwork/email.png"))
        if social_network == "telegram":
            label_icon_social_network.setPixmap(QtGui.QPixmap(":/icons/socialNetwork/telegram.png"))
        if social_network == "vk":
            label_icon_social_network.setPixmap(QtGui.QPixmap(":/icons/socialNetwork/vk.png"))

        label_icon_social_network.setMaximumSize(QtCore.QSize(35, 35))
        label_icon_social_network.setText("")
        
        label_icon_social_network.setScaledContents(True)
        label_icon_social_network.setObjectName("label_icon_social_network")
        gridLayout.addWidget(label_icon_social_network, 0, 2, 1, 1)

        # Дата отправки сообщения
        label_date = QtWidgets.QLabel(self)
        label_date.setText(f"{datetime.strftime(date_emit, '%d.%m.%Y')}")
        label_date.setObjectName("label_date")
        gridLayout.addWidget(label_date, 0, 1, 1, 1)

        # Пробел
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        gridLayout.addItem(spacerItem, 0, 0, 1, 1)

        # Текст сообщения
        label_text_message = QtWidgets.QLabel(self)
        label_text_message.setText(f"{text}")
        label_text_message.setWordWrap(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_text_message.sizePolicy().hasHeightForWidth())
        label_text_message.setSizePolicy(sizePolicy)
        label_text_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        label_text_message.setObjectName("label_text_message")
        gridLayout.addWidget(label_text_message, 1, 0, 1, 3)

import icons_rc
