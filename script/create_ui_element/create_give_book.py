from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from typing import Callable


class CreateGiveBook(QtWidgets.QFrame):
    """
    Создает виджет QFrame по полученной информации
    """
    def __init__(self, functional_return_book: Callable, id_take_book: int, id_book, name: str, author: str, isbn: str,
                 year_release: int, date_take: datetime.date):
        super().__init__()

        # Настройка самого виджета
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(490, 200))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame-give-book")

        # Сетка для виджета
        gridLayout = QtWidgets.QGridLayout(self)
        gridLayout.setContentsMargins(25, 25, 25, 25)
        gridLayout.setSpacing(5)
        gridLayout.setObjectName("gridLayout")

        # Название
        label_name = QtWidgets.QLabel(self)
        label_name.setText(f"Название: {name}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_name.sizePolicy().hasHeightForWidth())
        label_name.setSizePolicy(sizePolicy)
        label_name.setObjectName("label_name")
        gridLayout.addWidget(label_name, 0, 0, 1, 1)

        # Автор
        label_author = QtWidgets.QLabel(self)
        label_author.setText(f"Автор: {author}")
        label_author.setObjectName("label_author")
        gridLayout.addWidget(label_author, 1, 0, 1, 1)

        # ISBN
        label_isbn = QtWidgets.QLabel(self)
        label_isbn.setText(f"ISBN: {isbn}")
        label_isbn.setObjectName("label_isbn")
        gridLayout.addWidget(label_isbn, 2, 0, 1, 1)    

        # Год публикации
        label_year_publication = QtWidgets.QLabel(self)
        label_year_publication.setText(f"Год выпуска: {year_release}")
        label_year_publication.setObjectName("label_year_publication")
        gridLayout.addWidget(label_year_publication, 3, 0, 1, 1)

        # Год даты взятие
        label_date_take = QtWidgets.QLabel(self)
        label_date_take.setText(f"Дата взятие книги: {datetime.strftime(date_take, '%d.%m.%Y')}")
        label_date_take.setObjectName("label_date_take")
        gridLayout.addWidget(label_date_take, 4, 0, 1, 1)

        # Кнопка принятие книги
        pushButton_accept = QtWidgets.QPushButton(self)
        pushButton_accept.setText("Принять книгу")
        pushButton_accept.clicked.connect(lambda: functional_return_book(id_take_book, name))
        pushButton_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/book/book-pick-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_accept.setIcon(icon)
        pushButton_accept.setIconSize(QtCore.QSize(32, 32))
        pushButton_accept.setObjectName("pushButton-accept-for-give-book")
        gridLayout.addWidget(pushButton_accept, 0, 1, 5, 1)

