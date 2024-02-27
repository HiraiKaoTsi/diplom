from PyQt5 import QtCore, QtGui, QtWidgets


class CreateFrameBook(QtWidgets.QFrame):
    def __init__(self, id, name_book, author, isbn, year_publication, quantity, have_book):
        super().__init__()


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)
        self.setObjectName("frame-book")
      
        gridLayout = QtWidgets.QGridLayout(self)
        gridLayout.setContentsMargins(5, 5, 5, 5)
        gridLayout.setSpacing(5)
        gridLayout.setObjectName("gridLayout")


        label_name = QtWidgets.QLabel(self)
        label_name.setText(f"{name_book}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        label_name.setSizePolicy(sizePolicy)
        label_name.setObjectName("label_name")
        gridLayout.addWidget(label_name, 0, 0, 1, 1)


        label_author = QtWidgets.QLabel(self)
        label_author.setText(f"{author}")
        label_author.setObjectName("label_author")
        gridLayout.addWidget(label_author, 1, 0, 1, 1)


        label_isbn = QtWidgets.QLabel(self)
        label_isbn.setText(f"{isbn}")
        label_isbn.setObjectName("ISBN")
        gridLayout.addWidget(label_isbn, 2, 0, 1, 1)

        
        label_year_publication = QtWidgets.QLabel(self)
        label_year_publication.setText(f"{year_publication}")
        label_year_publication.setObjectName("year_publication")
        gridLayout.addWidget(label_year_publication, 3, 0, 1, 1)

        info_about_book = QtWidgets.QLabel(self)
        info_about_book.setText("Книга свободна")
        info_about_book.setObjectName("info_about_book")
        gridLayout.addWidget(info_about_book, 4, 0, 1, 1)

        frame_for_button = QtWidgets.QFrame(self)
        frame_for_button.setMinimumSize(QtCore.QSize(0, 0))
        frame_for_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_for_button.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_for_button.setObjectName("frame_for_button")
        # mb edit
        gridLayout.addWidget(frame_for_button, 0, 1, 5, 1, QtCore.Qt.AlignVCenter)


        verticalLayout = QtWidgets.QVBoxLayout(frame_for_button)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setSpacing(5)
        verticalLayout.setObjectName("verticalLayout")




        accept_book = QtWidgets.QPushButton(frame_for_button)
        accept_book.setText("Принять книгу")
        accept_book.setObjectName("accept_book")
        verticalLayout.addWidget(accept_book)

        issue_book = QtWidgets.QPushButton(frame_for_button)
        issue_book.setText("Выдать книгу")
        issue_book.setObjectName("issue_book")
        verticalLayout.addWidget(issue_book)

        if have_book is False:
            issue_book.setEnabled(False)

        # self.gridLayout.addWidget(self.frame_14, 0, 1, 5, 1, QtCore.Qt.AlignVCenter)
