from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Callable


class CreateBook(QtWidgets.QFrame):
    """
    Создает виджет QFrame по полученной информации
    """
    def __init__(self, functional_open_book: Callable, id: int, name: str, author: str, isbn: str, year_release, general_quanity: int, quanity_issued: int):
        super().__init__()

        # Настройка самого виджета
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        # self.setMinimumSize(QtCore.QSize(321, 141))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame-book")

        # Сетка для виджета
        horizontalLayout = QtWidgets.QHBoxLayout(self)
        horizontalLayout.setContentsMargins(25, 25, 25, 25)
        horizontalLayout.setSpacing(5)
        horizontalLayout.setObjectName("horizontalLayout")

        # Frame - для основной информации
        frame_maim_info = QtWidgets.QFrame(self)
        frame_maim_info.setMinimumSize(QtCore.QSize(50, 100))
        frame_maim_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_maim_info.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_maim_info.setObjectName("frame_maim_info")
        horizontalLayout.addWidget(frame_maim_info)

        # Сетка для фрейма с основной информацией
        verticalLayout = QtWidgets.QVBoxLayout(frame_maim_info)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setSpacing(5)
        verticalLayout.setObjectName("verticalLayout")

        # Название
        label_name = QtWidgets.QLabel(frame_maim_info)
        label_name.setText(f"Название книги: {name}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_name.sizePolicy().hasHeightForWidth())
        label_name.setSizePolicy(sizePolicy)
        label_name.setObjectName("label_name")
        verticalLayout.addWidget(label_name)

        # Автор 
        label_author = QtWidgets.QLabel(frame_maim_info)
        label_author.setText(f"Автор: {author}")
        label_author.setObjectName("label_author")
        verticalLayout.addWidget(label_author)

        # ISBN
        label_isbn = QtWidgets.QLabel(frame_maim_info)
        label_isbn.setText(f"ISBN: {isbn}")
        label_isbn.setObjectName("label_isbn")
        verticalLayout.addWidget(label_isbn)

        # Год публикации
        label_year_publication = QtWidgets.QLabel(frame_maim_info)
        label_year_publication.setText(f"Год публикации: {year_release}")
        label_year_publication.setObjectName("label_year_publication")
        verticalLayout.addWidget(label_year_publication)

        # Общее количество книг
        label_all_quantity = QtWidgets.QLabel(frame_maim_info)
        label_all_quantity.setText(f"Количество экземпляров: {general_quanity}")
        label_all_quantity.setObjectName("label_all_quantity")
        verticalLayout.addWidget(label_all_quantity)

        # Текущее количество
        label_current_quantity = QtWidgets.QLabel(frame_maim_info)
        label_current_quantity.setText(f"Текущее количество: {general_quanity - quanity_issued}")
        label_current_quantity.setObjectName("label_current_quantity")
        verticalLayout.addWidget(label_current_quantity)
        

        # Кнопка с подробной информацией и функционалом с данной книгой
        pushButton_functional = QtWidgets.QPushButton(self)
        pushButton_functional.clicked.connect(lambda: functional_open_book(id))
        pushButton_functional.setText("Взаимодействие")
        pushButton_functional.setMinimumSize(QtCore.QSize(100, 0))
        pushButton_functional.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/main/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_functional.setIcon(icon)
        pushButton_functional.setIconSize(QtCore.QSize(28, 32))
        pushButton_functional.setAutoDefault(False)
        pushButton_functional.setObjectName("pushButton_functional")
        horizontalLayout.addWidget(pushButton_functional, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

import icons_rc
