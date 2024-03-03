from PyQt5 import QtCore, QtGui, QtWidgets


class CreateHistoryBook(QtWidgets.QFrame):
    """
    Создает виджет QFrame по полученной информации
    """
    def __init__(self, id: int, name: str, author: str, isbn: str, year_release, date_take, date_return):
        super().__init__()
        
        # Настройка самого виджета
        self.setGeometry(QtCore.QRect(10, 20, 381, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(321, 141))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame-book-history")

        # Сетка для виджета
        gridLayout = QtWidgets.QGridLayout(self)
        gridLayout.setContentsMargins(5, 5, 5, 5)
        gridLayout.setSpacing(5)
        gridLayout.setObjectName("gridLayout")

        # Название
        label_name = QtWidgets.QLabel(self)
        label_name.setText(f"{name}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_name.sizePolicy().hasHeightForWidth())
        label_name.setSizePolicy(sizePolicy)
        label_name.setObjectName("label_name")
        gridLayout.addWidget(label_name, 0, 0, 1, 1)

        # Автор 
        label_author = QtWidgets.QLabel(self)
        label_author.setText(f"{author}")
        label_author.setObjectName("label_author")
        gridLayout.addWidget(label_author, 1, 0, 1, 1)

        # ISBN 
        label_isbn = QtWidgets.QLabel(self)
        label_isbn.setText(f"{isbn}")
        label_isbn.setObjectName("label_isbn")
        gridLayout.addWidget(label_isbn, 2, 0, 1, 1)

        # Год публикации
        label_year_publication = QtWidgets.QLabel(self)
        label_year_publication.setText(f"{year_release}")
        label_year_publication.setObjectName("label_year_publication")
        gridLayout.addWidget(label_year_publication, 3, 0, 1, 1)

        # Frame для дат 
        frame_date = QtWidgets.QFrame(self)
        frame_date.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_date.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_date.setObjectName("frame")
        gridLayout.addWidget(frame_date, 4, 0, 1, 1)

        # Сетка для Frame
        horizontalLayout = QtWidgets.QHBoxLayout(frame_date)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(5)
        horizontalLayout.setObjectName("horizontalLayout")

        # Дата братия книги пользователем
        label_date_take = QtWidgets.QLabel(frame_date)
        label_date_take.setText(f"{date_take}")
        label_date_take.setObjectName("label_date_take")
        horizontalLayout.addWidget(label_date_take)

        # Дата когда пользователь вернул книгу
        label_date_return = QtWidgets.QLabel(frame_date)
        label_date_return.setText(f"{date_return}")
        label_date_return.setObjectName("label_date_return")
        horizontalLayout.addWidget(label_date_return)    
       