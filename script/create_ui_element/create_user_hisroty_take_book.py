from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Callable
from datetime import datetime


class CreateUserHistoryTakeBook(QtWidgets.QFrame):
    def __init__(self, function_details_user: Callable, id_user, fio, number_group, student_id_number,
                 date_take: datetime.date, how_many_days, date_return: datetime.date):
        super().__init__()

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumHeight(200)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("create-user-history-take-book")

        verticalLayout = QtWidgets.QVBoxLayout(self)
        verticalLayout.setContentsMargins(25, 25, 25, 25)
        verticalLayout.setSpacing(10)
        verticalLayout.setObjectName("verticalLayout")

        label_fio = QtWidgets.QLabel(self)
        label_fio.setText(f"ФИО: {fio}")
        label_fio.setWordWrap(True)
        label_fio.setObjectName("label_fio")
        verticalLayout.addWidget(label_fio)

        label_number_group = QtWidgets.QLabel(self)
        label_number_group.setText(f"Номер группы: {number_group}")
        label_number_group.setWordWrap(True)
        label_number_group.setObjectName("label_number_group")
        verticalLayout.addWidget(label_number_group)

        label_student_id_number = QtWidgets.QLabel(self)
        label_student_id_number.setText(f"Студенческий: {student_id_number}")
        label_student_id_number.setWordWrap(True)
        label_student_id_number.setObjectName("label_student_id_number")
        verticalLayout.addWidget(label_student_id_number)

        frame_date = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        frame_date.setSizePolicy(sizePolicy)
        frame_date.setMinimumWidth(180)
        frame_date.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_date.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_date.setObjectName("frame_date")
        verticalLayout.addWidget(frame_date, 0, QtCore.Qt.AlignHCenter)

        horizontalLayout = QtWidgets.QHBoxLayout(frame_date)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(10)
        horizontalLayout.setObjectName("horizontalLayout")

        label_date_take = QtWidgets.QLabel(frame_date)
        label_date_take.setText(f"Дата взятия - {datetime.strftime(date_take, '%d.%m.%Y')}")
        label_date_take.setObjectName("label_date_take")
        horizontalLayout.addWidget(label_date_take)

        label_how_many_day = QtWidgets.QLabel(frame_date)
        label_how_many_day.setText(f"  на - {how_many_days} дня/дней  ")
        label_how_many_day.setObjectName("label_how_many_day")
        horizontalLayout.addWidget(label_how_many_day)

        label_date_return = QtWidgets.QLabel(frame_date)
        label_date_return.setText(f"вернул - {datetime.strftime(date_return, '%d.%m.%Y')}")
        label_date_return.setObjectName("label_date_return")
        horizontalLayout.addWidget(label_date_return)
        
        pushButton_all_info = QtWidgets.QPushButton(self)
        pushButton_all_info.setText("Подробная Информация пользователя")
        pushButton_all_info.clicked.connect(lambda: function_details_user(id_user))
        pushButton_all_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/main/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_all_info.setIcon(icon)
        pushButton_all_info.setIconSize(QtCore.QSize(25, 25))
        pushButton_all_info.setObjectName("pushButton_all_info")
        verticalLayout.addWidget(pushButton_all_info, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        