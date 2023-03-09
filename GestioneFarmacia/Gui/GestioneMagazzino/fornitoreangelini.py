from PyQt5 import QtCore, QtGui, QtWidgets
import pickle

from GestioneFarmacia.GestioneMagazzino.GestoreMagazzino import GestoreMagazzino
from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

g1 = GestoreMagazzino()
g1.downloadMagazzino()
p = Prodotto(12, "nome", "tipologia", 3, "dosaggio", "scadenza", 2)

class Ui_angelini(object):



    def setupUi(self, angelini):
        self.Frame = angelini
        angelini.setObjectName("angelini")
        angelini.resize(939, 590)
        angelini.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ricercafornitorebtn = QtWidgets.QPushButton(angelini)
        self.ricercafornitorebtn.setGeometry(QtCore.QRect(620, 50, 91, 41))
        self.ricercafornitorebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercafornitorebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ricercafornitorebtn.setIcon(icon)
        self.ricercafornitorebtn.setObjectName("ricercafornitorebtn")
        self.lineEdit = QtWidgets.QLineEdit(angelini)
        self.lineEdit.setGeometry(QtCore.QRect(720, 60, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.quantitaprodsb = QtWidgets.QSpinBox(angelini)
        self.quantitaprodsb.setGeometry(QtCore.QRect(790, 190, 42, 22))
        self.quantitaprodsb.setObjectName("quantitaprodsb")
        self.lineEdit_2 = QtWidgets.QLineEdit(angelini)
        self.lineEdit_2.setGeometry(QtCore.QRect(650, 190, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(angelini)
        self.label.setGeometry(QtCore.QRect(620, 140, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.carrellobtn = QtWidgets.QPushButton(angelini)
        self.carrellobtn.setGeometry(QtCore.QRect(690, 330, 131, 41))
        self.carrellobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.carrellobtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconacarrello.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carrellobtn.setIcon(icon1)
        self.carrellobtn.setIconSize(QtCore.QSize(30, 30))
        self.carrellobtn.setObjectName("carrellobtn")
        self.acquistabtn = QtWidgets.QPushButton(angelini)
        self.acquistabtn.setGeometry(QtCore.QRect(530, 470, 121, 41))
        self.acquistabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acquistabtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconadollaro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acquistabtn.setIcon(icon2)
        self.acquistabtn.setIconSize(QtCore.QSize(30, 30))
        self.acquistabtn.setObjectName("acquistabtn")
        self.frame = QtWidgets.QFrame(angelini)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 971, 631))
        self.frame.setStyleSheet("background-image: url(C:/Users/Public/Pictures/loghi-icone/sfondoangelini.PNG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 310, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.homebtn = QtWidgets.QPushButton(angelini)
        self.homebtn.setGeometry(QtCore.QRect(790, 530, 101, 31))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon3)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.pushButton = QtWidgets.QPushButton(angelini)
        self.pushButton.setGeometry(QtCore.QRect(710, 520, 61, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/loghi-icone/iconaindietro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.tableWidgetlist = QtWidgets.QTableWidget(angelini)
        self.tableWidgetlist.setGeometry(QtCore.QRect(40, 50, 421, 241))
        self.tableWidgetlist.setObjectName("tableWidgetlist")
        self.tableWidgetlist.setColumnCount(0)
        self.tableWidgetlist.setRowCount(0)
        self.tableWidgetcarrello = QtWidgets.QTableWidget(angelini)
        self.tableWidgetcarrello.setGeometry(QtCore.QRect(40, 340, 421, 241))
        self.tableWidgetcarrello.setObjectName("tableWidgetcarrello")
        self.tableWidgetcarrello.setColumnCount(0)
        self.tableWidgetcarrello.setRowCount(0)
        self.frame.raise_()
        self.ricercafornitorebtn.raise_()
        self.lineEdit.raise_()
        self.quantitaprodsb.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.carrellobtn.raise_()
        self.acquistabtn.raise_()
        self.homebtn.raise_()
        self.pushButton.raise_()
        self.tableWidgetlist.raise_()
        self.tableWidgetcarrello.raise_()

        self.creaListaProdotti()
        self.creaCarrello()

        self.popolaListaProdotti()



        self.homebtn.clicked.connect(self.returnToHome)
        self.pushButton.clicked.connect(self.returnToFornitori)

        self.retranslateUi(angelini)
        QtCore.QMetaObject.connectSlotsByName(angelini)

    def retranslateUi(self, angelini):
        _translate = QtCore.QCoreApplication.translate
        angelini.setWindowTitle(_translate("angelini", "Form"))
        self.ricercafornitorebtn.setText(_translate("angelini", "  Ricerca"))
        self.label.setText(_translate("angelini", "Inserisci codice e quantità da comprare"))
        self.carrellobtn.setText(_translate("angelini", "Metti nel carrello"))
        self.acquistabtn.setText(_translate("angelini", "  Acquista"))
        self.label_3.setText(_translate("angelini", "Carrello:"))
        self.label_4.setText(_translate("angelini", "Lista prodotti:"))
        self.homebtn.setText(_translate("angelini", "Home"))


    def returnToHome(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    def returnToFornitori(self):
        from GestioneFarmacia.Gui.GestioneMagazzino.sceltafornitore import Ui_Fornitori
        self.fornitori = QtWidgets.QFrame()
        self.ui = Ui_Fornitori()
        self.ui.setupUi(self.fornitori)
        self.fornitori.show()
        self.Frame.close()

    def creaListaProdotti(self):

        self.tableWidgetlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetlist.setObjectName("tableWidget")
        self.tableWidgetlist.setColumnCount(10)
        self.tableWidgetlist.setRowCount(10)
        for i in range(0, 10):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetlist.setHorizontalHeaderItem(i, item)

        self.tableWidgetlist.horizontalHeader().setVisible(True)
        self.tableWidgetlist.horizontalHeader().setDefaultSectionSize(84)
        self.tableWidgetlist.verticalHeader().setVisible(True)

    def creaCarrello(self):

        self.tableWidgetcarrello.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetcarrello.setObjectName("tableWidget")
        self.tableWidgetcarrello.setColumnCount(4)
        self.tableWidgetcarrello.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetcarrello.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetcarrello.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetcarrello.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetcarrello.setHorizontalHeaderItem(3, item)

        self.tableWidgetcarrello.horizontalHeader().setVisible(True)
        self.tableWidgetcarrello.horizontalHeader().setDefaultSectionSize(84)
        self.tableWidgetcarrello.verticalHeader().setVisible(True)

    def popolaListaProdotti(self):

        item = self.tableWidgetlist.horizontalHeaderItem(0)
        _translate = QtCore.QCoreApplication.translate
        item.setText(_translate("angelini", "Prodotto"))
        item = self.tableWidgetlist.horizontalHeaderItem(1)
        item.setText(_translate("angelini", "Quantità"))
        item = self.tableWidgetlist.horizontalHeaderItem(2)
        item.setText(_translate("angelini", "Prezzo"))
        item = self.tableWidgetlist.horizontalHeaderItem(3)
        item.setText(_translate("angelini", "Codice"))
        lenf = len(g1.listaFarmaci)
        for riga in range(0, lenf):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                print(str(riga) + str(colonna))
                if(colonna == 0):
                    item.setText(_translate("angelini", g1.listaFarmaci[riga].nome))
                if(colonna == 1):
                    item.setText(_translate("angelini", str(g1.listaFarmaci[riga].giacenza)))
                if(colonna == 2):
                    item.setText(_translate("angelini", str(g1.listaFarmaci[riga].prezzo)))
                if(colonna == 3):
                    item.setText(_translate("angelini", str(g1.listaFarmaci[riga].codice)))
        lenp = len(g1.listaProdotti)
        for riga in range(lenf, lenp + lenf):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                print(str(riga) + str(colonna))
                if(colonna == 0):
                    item.setText(_translate("angelini", g1.listaProdotti[riga - lenf].nome))
                if(colonna == 1):
                    item.setText(_translate("angelini", str(g1.listaProdotti[riga - lenf].giacenza)))
                if(colonna == 2):
                    item.setText(_translate("angelini", str(g1.listaProdotti[riga - lenf].prezzo)))
                if(colonna == 3):
                    item.setText(_translate("angelini", str(g1.listaProdotti[riga - lenf].codice)))






