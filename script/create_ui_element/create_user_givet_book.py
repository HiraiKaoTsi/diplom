from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Callable


class CreateUserGivetBook(QtWidgets.QFrame):
    def __init__(self, function_details_user: Callable, function_next_stage_givet_book: Callable, id_user: int, fio: str, number_group: str, student_id: str):
        super().__init__()
 
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumWidth(500)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame-user-givet-book")

        verticalLayout = QtWidgets.QVBoxLayout(self)
        verticalLayout.setContentsMargins(20, 20, 20, 20)
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
        label_student_id_number.setText(f"Студенческий: {student_id}")
        label_student_id_number.setWordWrap(True)
        label_student_id_number.setObjectName("label_student_id_number")
        verticalLayout.addWidget(label_student_id_number)

        pushButton_all_info = QtWidgets.QPushButton(self)
        pushButton_all_info.setText("Подробная информация пользователя")
        pushButton_all_info.clicked.connect(lambda: function_details_user(id_user))
        pushButton_all_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/main/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_all_info.setIcon(icon)
        pushButton_all_info.setIconSize(QtCore.QSize(30, 30))
        pushButton_all_info.setObjectName("pushButton_all_info")
        verticalLayout.addWidget(pushButton_all_info, 0, QtCore.Qt.AlignHCenter)

        pushButton_givet_book = QtWidgets.QPushButton(self)
        pushButton_givet_book.clicked.connect(lambda: function_next_stage_givet_book(id_user))
        pushButton_givet_book.setText("Выдать книгу")
        pushButton_givet_book.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/book/book-gived.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_givet_book.setIcon(icon1)
        pushButton_givet_book.setIconSize(QtCore.QSize(30, 30))
        pushButton_givet_book.setObjectName("pushButton_givet_book")
        verticalLayout.addWidget(pushButton_givet_book, 0, QtCore.Qt.AlignHCenter)
