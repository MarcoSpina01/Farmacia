from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

p = Prodotto(1, "g", "f", 3, "h", "d", 2)
gestore = Gestore()
class Ui_RicercaMagazzino(object):
    def setupUi(self, Form):
        self.Frame = Form
        Form.setObjectName("Form")
        Form.resize(597, 376)
        self.Ricercaarticolobtn = QtWidgets.QPushButton(Form)
        self.Ricercaarticolobtn.setGeometry(QtCore.QRect(30, 290, 91, 41))
        self.Ricercaarticolobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ricercaarticolobtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ricercaarticolobtn.setIcon(icon)
        self.Ricercaarticolobtn.setObjectName("Ricercaarticolobtn")
        self.homebtn = QtWidgets.QPushButton(Form)
        self.homebtn.setGeometry(QtCore.QRect(450, 320, 101, 31))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon1)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 621, 391))
        self.frame.setStyleSheet("background-image: url(" +gestore.returnPth()+ "loghi-icone/sfondomagazzino.PNG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 310, 61, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconaindietro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.ricercamagazzinotb = QtWidgets.QLineEdit(Form)
        self.ricercamagazzinotb.setGeometry(QtCore.QRect(140, 300, 191, 21))
        self.ricercamagazzinotb.setObjectName("ricercamagazzinotb")
        self.tableWidgetmagazzino = QtWidgets.QTableWidget(Form)
        self.tableWidgetmagazzino.setGeometry(QtCore.QRect(40, 30, 501, 221))
        self.tableWidgetmagazzino.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetmagazzino.setObjectName("tableWidgetmagazzino")
        self.tableWidgetmagazzino.setColumnCount(0)
        self.tableWidgetmagazzino.setRowCount(0)
        self.frame.raise_()
        self.Ricercaarticolobtn.raise_()
        self.homebtn.raise_()
        self.pushButton.raise_()
        self.ricercamagazzinotb.raise_()
        self.tableWidgetmagazzino.raise_()


        self.creaListaProdotti()


        self.homebtn.clicked.connect(self.returnToHome)
        self.pushButton.clicked.connect(self.returnToMagazzino)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Ricercaarticolobtn.setText(_translate("Form", "  Ricerca"))
        self.homebtn.setText(_translate("Form", "Home"))

    def returnToHome(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    def returnToMagazzino(self):
        from GestioneFarmacia.Gui.GestioneMagazzino.magazzino import Ui_Magazzino
        self.magazzino = QtWidgets.QFrame()
        self.ui = Ui_Magazzino()
        self.ui.setupUi(self.magazzino)
        self.magazzino.show()
        self.Frame.close()

    def creaListaProdotti(self):
        self.tableWidgetmagazzino.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetmagazzino.setObjectName("tableWidget")
        self.tableWidgetmagazzino.setColumnCount(4)
        self.tableWidgetmagazzino.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetmagazzino.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetmagazzino.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetmagazzino.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetmagazzino.setHorizontalHeaderItem(3, item)

        self.tableWidgetmagazzino.horizontalHeader().setVisible(True)
        self.tableWidgetmagazzino.horizontalHeader().setDefaultSectionSize(84)
        self.tableWidgetmagazzino.verticalHeader().setVisible(True)

    def popolaMagazzino(self):
        _translate = QtCore.QCoreApplication.translate
        lenf = len(g1.listaFarmaciFornitore)
        for riga in range(0, lenf):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if(colonna == 0):
                    item.setText(_translate("angelini", g1.listaFarmaci[riga].nome))
                if(colonna == 1):
                    item.setText(_translate("angelini", str(g1.listaFarmaci[riga].giacenza)))
                if(colonna == 2):
                    item.setText(_translate("angelini", str(g1.listaFarmaci[riga].prezzo)))
                if(colonna == 3):
                    item.setText(_translate("angelini", str(g1.listaFarmaci[riga].codice)))
        lenp = len(g1.listaProdottiFornitore)
        for riga in range(lenf, lenp + lenf):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if(colonna == 0):
                    item.setText(_translate("angelini", g1.listaProdotti[riga - lenf].nome))
                if(colonna == 1):
                    item.setText(_translate("angelini", str(g1.listaProdotti[riga - lenf].giacenza)))
                if(colonna == 2):
                    item.setText(_translate("angelini", str(g1.listaProdotti[riga - lenf].prezzo)))
                if(colonna == 3):
                    item.setText(_translate("angelini", str(g1.listaProdotti[riga - lenf].codice)))
