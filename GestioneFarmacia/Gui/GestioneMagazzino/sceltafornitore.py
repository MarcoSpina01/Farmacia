from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneFarmacia.GestioneSistema.gestione import Gestore

# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()

class Ui_Fornitori(object):

    def setupUi(self, Fornitori):
        self.Frame = Fornitori
        Fornitori.setObjectName("Fornitori")
        Fornitori.resize(723, 380)
        self.homebtn = QtWidgets.QPushButton(Fornitori)
        self.homebtn.setGeometry(QtCore.QRect(350, 320, 101, 31))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.label = QtWidgets.QLabel(Fornitori)
        self.label.setGeometry(QtCore.QRect(30, 10, 721, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Fornitori)
        self.pushButton.setGeometry(QtCore.QRect(270, 310, 61, 51))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconaindietro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Fornitori)
        self.frame.setGeometry(QtCore.QRect(-30, -10, 781, 431))
        self.frame.setStyleSheet("background-image: url("+gestore.returnPth()+"loghi-icone/sfondofornitori.PNG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Pfizerrbtn = QtWidgets.QRadioButton(Fornitori)
        self.Pfizerrbtn.setGeometry(QtCore.QRect(20, 190, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Pfizerrbtn.setFont(font)
        self.Pfizerrbtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Pfizerrbtn.setObjectName("Pfizerrbtn")
        self.Angelinirbtn = QtWidgets.QRadioButton(Fornitori)
        self.Angelinirbtn.setGeometry(QtCore.QRect(20, 240, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Angelinirbtn.setFont(font)
        self.Angelinirbtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.Angelinirbtn.setObjectName("Angelinirbtn")
        self.frame.raise_()
        self.homebtn.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.Pfizerrbtn.raise_()
        self.Angelinirbtn.raise_()
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Angelinirbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pfizerrbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # evento che permette di fare un ordine al fornitore angelini
        self.Angelinirbtn.clicked.connect(self.openFornitoreAngelini)
        # evento che permette di fare un ordine al fornitore pfizer
        self.Pfizerrbtn.clicked.connect(self.openFornitorePfizer)
        # evento che permette di tornare alla home
        self.homebtn.clicked.connect(self.returnToHome)
        # evento che permette di tornare al magazzino
        self.pushButton.clicked.connect(self.returnToMagazzino)

        self.retranslateUi(Fornitori)
        QtCore.QMetaObject.connectSlotsByName(Fornitori)

    def retranslateUi(self, Fornitori):
        _translate = QtCore.QCoreApplication.translate
        Fornitori.setWindowTitle(_translate("Fornitori", "Form"))
        self.homebtn.setText(_translate("Fornitori", "Home"))
        self.label.setText(_translate("Fornitori", "Scegli se aquistare dal fornitore Pfizer oppure dal fornitore Angelini"))
        self.Pfizerrbtn.setText(_translate("Fornitori", "Pfizer"))
        self.Angelinirbtn.setText(_translate("Fornitori", "Angelini"))

    # metodo che ti permette di tornare alla home
    def returnToHome(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    # metodo che ti permette di tornare al magazzino
    def returnToMagazzino(self):
        from GestioneFarmacia.Gui.GestioneMagazzino.magazzino import Ui_Magazzino
        self.magazzino = QtWidgets.QFrame()
        self.ui = Ui_Magazzino()
        self.ui.setupUi(self.magazzino)
        self.magazzino.show()
        self.Frame.close()

    # metodo che ti permette di aprire la schermata di ordine da angelini
    def openFornitoreAngelini(self):
        from GestioneFarmacia.Gui.GestioneMagazzino.fornitoreangelini import Ui_angelini
        self.angelini = QtWidgets.QFrame()
        self.ui = Ui_angelini()
        self.ui.setupUi(self.angelini)
        self.angelini.show()
        self.Frame.close()

    # metodo che ti permette di aprire la schermata di ordine da pfizer
    def openFornitorePfizer(self):
        from GestioneFarmacia.Gui.GestioneMagazzino.fornitorepfizer import Ui_pfizer
        self.pfizer = QtWidgets.QFrame()
        self.ui = Ui_pfizer()
        self.ui.setupUi(self.pfizer)
        self.pfizer.show()
        self.Frame.close()