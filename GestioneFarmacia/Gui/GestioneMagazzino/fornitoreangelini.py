from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto
from GestioneFarmacia.GestioneSistema.data import data

gestore = Gestore()


class Ui_angelini(object):

    nProdSelezionati = 0
    prodSelezionati = []

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
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth() +"loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth() +"loghi-icone/iconacarrello.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon2.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconadollaro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acquistabtn.setIcon(icon2)
        self.acquistabtn.setIconSize(QtCore.QSize(30, 30))
        self.acquistabtn.setObjectName("acquistabtn")
        self.frame = QtWidgets.QFrame(angelini)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 971, 631))
        self.frame.setStyleSheet("background-image: url(" + gestore.returnPth() + "loghi-icone/sfondoangelini.PNG);")
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
        icon3.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon4.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconaindietro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

        self.ricercafornitorebtn.clicked.connect(self.ricercaArticolo)

        self.carrellobtn.clicked.connect(self.selezionaProdotto)

        self.retranslateUi(angelini)
        QtCore.QMetaObject.connectSlotsByName(angelini)

    def retranslateUi(self, angelini):
        _translate = QtCore.QCoreApplication.translate
        angelini.setWindowTitle(_translate("angelini", "Form"))
        self.ricercafornitorebtn.setText(_translate("angelini", "  Ricerca"))
        self.label.setText(_translate("angelini", "Inserisci nome e quantità da comprare"))
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
        data.downloadFornitore()
        self.tableWidgetlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetlist.setObjectName("tableWidget")
        self.tableWidgetlist.setColumnCount(4)
        self.tableWidgetlist.setRowCount(data.nFarmForn + data.nProdForn)
        for i in range(0, data.nFarmForn + data.nProdForn):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetlist.setHorizontalHeaderItem(i, item)

        self.tableWidgetlist.horizontalHeader().setVisible(True)
        self.tableWidgetlist.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetlist.verticalHeader().setVisible(True)

    def selezionaProdotto(self):
        from tkinter import messagebox

        param = self.lineEdit_2.text()
        self.prodSelezionati
        check = False
        for element in data.listaFarmaciFornitore:
            if (param == element.codice):
                Ui_angelini.prodSelezionati.append(element)
                check = True

        for element in data.listaProdottiFornitore:
            if (param == element.codice):
                Ui_angelini.prodSelezionati.append(element)
                check = True
        if check:
            self.creaCarrello()
            self.popolaCarrello()
        else:
            messagebox.showinfo("Errore","Inserisci il codice corretto")

    def creaCarrello(self):
        self.prodSelezionati.clear()
        self.tableWidgetcarrello.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetcarrello.setObjectName("tableWidget")
        self.tableWidgetcarrello.setColumnCount(4)
        self.tableWidgetcarrello.setRowCount(data.nFarmForn + data.nProdForn)
        for x in range(data.nFarmForn + data.nProdForn):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setHorizontalHeaderItem(x, item)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetcarrello.horizontalHeaderItem(0)
        item.setText(_translate("cassa", "Prodotto"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(1)
        item.setText(_translate("cassa", "Quantità"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(2)
        item.setText(_translate("cassa", "Prezzo"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(3)
        item.setText(_translate("cassa", "Codice"))
        self.tableWidgetcarrello.horizontalHeader().setVisible(True)
        self.tableWidgetcarrello.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetcarrello.verticalHeader().setVisible(True)

    def popolaCarrello(self):
        nProdSelezionati = len(self.prodSelezionati)
        _translate = QtCore.QCoreApplication.translate
        nProdSelezionati -= 1
        for colonna in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(nProdSelezionati, colonna, item)
            item = self.tableWidgetcarrello.item(nProdSelezionati, colonna)
            if(colonna == 0):
                item.setText(_translate("angelini", Ui_angelini.prodSelezionati[nProdSelezionati].nome))
            if(colonna == 1):
                item.setText(_translate("angelini", str(Ui_angelini.prodSelezionati[nProdSelezionati].giacenza)))
            if(colonna == 2):
                item.setText(_translate("angelini", str(Ui_angelini.prodSelezionati[nProdSelezionati].prezzo)))
            if(colonna == 3):
                item.setText(_translate("angelini", str(Ui_angelini.prodSelezionati[nProdSelezionati].codice)))

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
        for riga in range(0, data.nFarmForn):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if(colonna == 0):
                    item.setText(_translate("angelini", data.listaFarmaciFornitore[riga].nome))
                if(colonna == 1):
                    item.setText(_translate("angelini", str(data.listaFarmaciFornitore[riga].giacenza)))
                if(colonna == 2):
                    item.setText(_translate("angelini", str(data.listaFarmaciFornitore[riga].prezzo)))
                if(colonna == 3):
                    item.setText(_translate("angelini", str(data.listaFarmaciFornitore[riga].codice)))
        for riga in range(data.nFarmForn, data.nFarmForn + data.nProdForn):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if(colonna == 0):
                    item.setText(_translate("angelini", data.listaProdottiFornitore[riga - data.nFarmForn].nome))
                if(colonna == 1):
                    item.setText(_translate("angelini", str(data.listaProdottiFornitore[riga - data.nFarmForn].giacenza)))
                if(colonna == 2):
                    item.setText(_translate("angelini", str(data.listaProdottiFornitore[riga - data.nFarmForn].prezzo)))
                if(colonna == 3):
                    item.setText(_translate("angelini", str(data.listaProdottiFornitore[riga - data.nFarmForn].codice)))

    def ricercaArticolo(self):
        from tkinter import messagebox
        param = self.lineEdit.text()
        if (param == ""):
            messagebox.showinfo("Errore", "Imposta almeno un carattere prima della ricerca")
        else:
            prodottiRicercati = []
            for element in data.listaFarmaciFornitore:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
            for element in data.listaProdottiFornitore:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
            p = ""
            for x in range(len(prodottiRicercati)):
                p += str(prodottiRicercati[x].nome +"  "+str(prodottiRicercati[x].giacenza)+"  "+prodottiRicercati[x].codice+"  "+str(prodottiRicercati[x].prezzo)+"€"+"\n")
            if(p==""):
                messagebox.showinfo("Errore", "Non è stato trovato alcun farmaco")
            else:
                messagebox.showinfo("Articolo/i", p)





