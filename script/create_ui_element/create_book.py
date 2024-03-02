from PyQt5 import QtCore, QtGui, QtWidgets


class CreateBook(QtWidgets.QFrame):
    """
    Создает виджет QFrame по полученной информации
    """
    def __init__(self, id: int, name: str, author: str, isbn: str, year_release, general_quanity: int, current_quanity_issued: int):
        super().__init__()

        # Настройка самого виджета
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(321, 141))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame_book")
        
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

        # isbn
        label_isbn = QtWidgets.QLabel(self)
        label_isbn.setText(f"{isbn}")
        label_isbn.setObjectName("label_isbn")
        gridLayout.addWidget(label_isbn, 2, 0, 1, 1)

        # Год публикации
        label_year_publication = QtWidgets.QLabel(self)
        # MB EDIT DATE TO RUS FORM
        label_year_publication.setText(f"{year_release}")
        label_year_publication.setObjectName("label_year_publication")
        gridLayout.addWidget(label_year_publication, 3, 0, 1, 1)

        # Общее количество книг
        label_all_quantity = QtWidgets.QLabel(self)
        label_all_quantity.setText(f"{general_quanity}")
        label_all_quantity.setObjectName("label_all_quantity")
        gridLayout.addWidget(label_all_quantity, 4, 0, 1, 1)

        # Текущее количество
        label_current_quantity = QtWidgets.QLabel(self)
        # label_current_quantity.setText(f"{current_quanity}")
        label_current_quantity.setObjectName("label_current_quantity")
        gridLayout.addWidget(label_current_quantity, 5, 0, 1, 1)

        # Frame для кнопок
        frame_button = QtWidgets.QFrame(self)
        frame_button.setMinimumSize(QtCore.QSize(0, 0))
        frame_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        frame_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_button.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_button.setObjectName("frame_button")
        gridLayout.addWidget(frame_button, 0, 1, 6, 1)

        # Сетка для frame-кнопок
        verticalLayout = QtWidgets.QVBoxLayout(frame_button)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setSpacing(5)
        verticalLayout.setObjectName("verticalLayout")

        # Кнопка принять книгу 
        pushButton_accept = QtWidgets.QPushButton(frame_button)
        pushButton_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/book/book-pick-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_accept.setIcon(icon)
        pushButton_accept.setIconSize(QtCore.QSize(32, 32))
        pushButton_accept.setObjectName("pushButton_accept")
        verticalLayout.addWidget(pushButton_accept)

        # Кнопка Выдать книгу
        pushButton_issue = QtWidgets.QPushButton(frame_button)
        pushButton_issue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/book/book-gived.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_issue.setIcon(icon1)
        pushButton_issue.setIconSize(QtCore.QSize(32, 32))
        pushButton_issue.setObjectName("pushButton_issue")
        verticalLayout.addWidget(pushButton_issue)

        # Кнопка изменить информацию
        pushButton_edit = QtWidgets.QPushButton(frame_button)
        pushButton_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/book/edit-book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_edit.setIcon(icon2)
        pushButton_edit.setIconSize(QtCore.QSize(29, 29))
        pushButton_edit.setObjectName("pushButton_edit")
        verticalLayout.addWidget(pushButton_edit)
