from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pfizer(object):
    def setupUi(self, pfizer):
        self.Frame = pfizer
        pfizer.setObjectName("pfizer")
        pfizer.resize(937, 587)
        self.label_4 = QtWidgets.QLabel(pfizer)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.ricercafornitorebtn = QtWidgets.QPushButton(pfizer)
        self.ricercafornitorebtn.setGeometry(QtCore.QRect(30, 370, 91, 41))
        self.ricercafornitorebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercafornitorebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ricercafornitorebtn.setIcon(icon)
        self.ricercafornitorebtn.setObjectName("ricercafornitorebtn")
        self.lineEdit = QtWidgets.QLineEdit(pfizer)
        self.lineEdit.setGeometry(QtCore.QRect(140, 380, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(pfizer)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 500, 131, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(pfizer)
        self.label.setGeometry(QtCore.QRect(50, 450, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.quantitaprodsb = QtWidgets.QSpinBox(pfizer)
        self.quantitaprodsb.setGeometry(QtCore.QRect(240, 500, 42, 22))
        self.quantitaprodsb.setObjectName("quantitaprodsb")
        self.carrellobtn = QtWidgets.QPushButton(pfizer)
        self.carrellobtn.setGeometry(QtCore.QRect(290, 530, 121, 41))
        self.carrellobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.carrellobtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconacarrello.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carrellobtn.setIcon(icon1)
        self.carrellobtn.setIconSize(QtCore.QSize(30, 30))
        self.carrellobtn.setObjectName("carrellobtn")
        self.acquistabtn = QtWidgets.QPushButton(pfizer)
        self.acquistabtn.setGeometry(QtCore.QRect(790, 280, 121, 41))
        self.acquistabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acquistabtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconadollaro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acquistabtn.setIcon(icon2)
        self.acquistabtn.setIconSize(QtCore.QSize(30, 30))
        self.acquistabtn.setObjectName("acquistabtn")
        self.fornitorelist = QtWidgets.QListView(pfizer)
        self.fornitorelist.setGeometry(QtCore.QRect(30, 70, 431, 221))
        self.fornitorelist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.fornitorelist.setObjectName("fornitorelist")
        self.label_3 = QtWidgets.QLabel(pfizer)
        self.label_3.setGeometry(QtCore.QRect(440, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.carrellolist = QtWidgets.QListView(pfizer)
        self.carrellolist.setGeometry(QtCore.QRect(480, 70, 431, 201))
        self.carrellolist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.carrellolist.setObjectName("carrellolist")
        self.frame = QtWidgets.QFrame(pfizer)
        self.frame.setGeometry(QtCore.QRect(0, 0, 951, 601))
        self.frame.setStyleSheet("background-image: url(C:/Users/Public/Pictures/loghi-icone/sfondopfizer.PNG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(pfizer)
        self.pushButton.setGeometry(QtCore.QRect(700, 510, 61, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconaindietro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.homebtn = QtWidgets.QPushButton(pfizer)
        self.homebtn.setGeometry(QtCore.QRect(780, 520, 101, 31))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon4)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.frame.raise_()
        self.label_4.raise_()
        self.ricercafornitorebtn.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.quantitaprodsb.raise_()
        self.carrellobtn.raise_()
        self.acquistabtn.raise_()
        self.fornitorelist.raise_()
        self.label_3.raise_()
        self.carrellolist.raise_()
        self.pushButton.raise_()
        self.homebtn.raise_()

        self.retranslateUi(pfizer)
        QtCore.QMetaObject.connectSlotsByName(pfizer)

    def retranslateUi(self, pfizer):
        _translate = QtCore.QCoreApplication.translate
        pfizer.setWindowTitle(_translate("pfizer", "Form"))
        self.label_4.setText(_translate("pfizer", "Lista prodotti:"))
        self.ricercafornitorebtn.setText(_translate("pfizer", "  Ricerca"))
        self.label.setText(_translate("pfizer", "Inserisci codice e quantità da comprare"))
        self.carrellobtn.setText(_translate("pfizer", "Metti nel carrello"))
        self.acquistabtn.setText(_translate("pfizer", "  Acquista"))
        self.label_3.setText(_translate("pfizer", "Carrello:"))
        self.homebtn.setText(_translate("pfizer", "Home"))

