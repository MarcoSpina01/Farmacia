from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneSistema.data import data


gestore = Gestore()

class Ui_Cassa(object):
    prodSelezionati = []
    def setupUi(self, Cassa):
        self.Frame = Cassa
        Cassa.setObjectName("Cassa")
        Cassa.resize(939, 615)
        self.label_4 = QtWidgets.QLabel(Cassa)
        self.label_4.setGeometry(QtCore.QRect(470, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tableWidgetcarrello = QtWidgets.QTableWidget(Cassa)
        self.tableWidgetcarrello.setGeometry(QtCore.QRect(20, 330, 421, 241))
        self.tableWidgetcarrello.setObjectName("tableWidgetcarrello")
        self.tableWidgetcarrello.setColumnCount(0)
        self.tableWidgetcarrello.setRowCount(0)
        self.ricercabtn = QtWidgets.QPushButton(Cassa)
        self.ricercabtn.setGeometry(QtCore.QRect(70, 30, 91, 41))
        self.ricercabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercabtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ricercabtn.setIcon(icon)
        self.ricercabtn.setObjectName("ricercabtn")
        self.homebtn = QtWidgets.QPushButton(Cassa)
        self.homebtn.setGeometry(QtCore.QRect(610, 530, 111, 41))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon1)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.tableWidgetlist = QtWidgets.QTableWidget(Cassa)
        self.tableWidgetlist.setGeometry(QtCore.QRect(480, 40, 421, 241))
        self.tableWidgetlist.setObjectName("tableWidgetlist")
        self.tableWidgetlist.setColumnCount(0)
        self.tableWidgetlist.setRowCount(0)
        self.carrellobtn = QtWidgets.QPushButton(Cassa)
        self.carrellobtn.setGeometry(QtCore.QRect(150, 190, 131, 41))
        self.carrellobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.carrellobtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconacarrello.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carrellobtn.setIcon(icon2)
        self.carrellobtn.setIconSize(QtCore.QSize(30, 30))
        self.carrellobtn.setObjectName("carrellobtn")
        self.label = QtWidgets.QLabel(Cassa)
        self.label.setGeometry(QtCore.QRect(90, 100, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.codicele = QtWidgets.QLineEdit(Cassa)
        self.codicele.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.codicele.setObjectName("codicele")
        self.ricercale = QtWidgets.QLineEdit(Cassa)
        self.ricercale.setGeometry(QtCore.QRect(170, 40, 131, 20))
        self.ricercale.setObjectName("ricercale")
        self.quantitaprodsb = QtWidgets.QSpinBox(Cassa)
        self.quantitaprodsb.setGeometry(QtCore.QRect(260, 150, 42, 22))
        self.quantitaprodsb.setObjectName("quantitaprodsb")
        self.acquistabtn = QtWidgets.QPushButton(Cassa)
        self.acquistabtn.setGeometry(QtCore.QRect(450, 530, 121, 41))
        self.acquistabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acquistabtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconadollaro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acquistabtn.setIcon(icon3)
        self.acquistabtn.setIconSize(QtCore.QSize(30, 30))
        self.acquistabtn.setObjectName("acquistabtn")
        self.label_3 = QtWidgets.QLabel(Cassa)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.Cassa_2 = QtWidgets.QFrame(Cassa)
        self.Cassa_2.setGeometry(QtCore.QRect(-1, -1, 941, 621))
        self.Cassa_2.setStyleSheet("background-image: url("+gestore.returnPth()+"loghi-icone/sfondocassa.PNG);")
        self.Cassa_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cassa_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cassa_2.setObjectName("Cassa_2")
        self.Cassa_2.raise_()
        self.label_4.raise_()
        self.tableWidgetcarrello.raise_()
        self.ricercabtn.raise_()
        self.homebtn.raise_()
        self.tableWidgetlist.raise_()
        self.carrellobtn.raise_()
        self.label.raise_()
        self.codicele.raise_()
        self.ricercale.raise_()
        self.quantitaprodsb.raise_()
        self.acquistabtn.raise_()
        self.label_3.raise_()


        self.creaListaVendita()
        self.popolaListaVendita()

        self.ricercabtn.clicked.connect(self.ricercaArticolo)

        self.carrellobtn.clicked.connect(self.selezionaProdotto)


        self.homebtn.clicked.connect(self.returnToHome)


        self.retranslateUi(Cassa)
        QtCore.QMetaObject.connectSlotsByName(Cassa)

    def retranslateUi(self, Cassa):
        _translate = QtCore.QCoreApplication.translate
        Cassa.setWindowTitle(_translate("Cassa", "Form"))
        self.label_4.setText(_translate("Cassa", "Lista prodotti:"))
        self.ricercabtn.setText(_translate("Cassa", "  Ricerca"))
        self.homebtn.setText(_translate("Cassa", "Home"))
        self.carrellobtn.setText(_translate("Cassa", "Metti nel carrello"))
        self.label.setText(_translate("Cassa", "Inserisci codice e quantità da comprare"))
        self.acquistabtn.setText(_translate("Cassa", "  Acquista"))
        self.label_3.setText(_translate("Cassa", "Carrello:"))

    def returnToHome(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    def creaListaVendita(self):
        data.downloadMagazzino()
        self.tableWidgetlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetlist.setObjectName("tableWidget")
        self.tableWidgetlist.setColumnCount(4)
        self.tableWidgetlist.setRowCount(data.nFarmMagaz + data.nProdMagaz)
        for i in range(0, data.nFarmMagaz + data.nProdMagaz):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetlist.setHorizontalHeaderItem(i, item)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetlist.horizontalHeaderItem(0)
        item.setText(_translate("cassa", "Prodotto"))
        item = self.tableWidgetlist.horizontalHeaderItem(1)
        item.setText(_translate("cassa", "Quantità"))
        item = self.tableWidgetlist.horizontalHeaderItem(2)
        item.setText(_translate("cassa", "Prezzo"))
        item = self.tableWidgetlist.horizontalHeaderItem(3)
        item.setText(_translate("cassa", "Codice"))
        self.tableWidgetlist.horizontalHeader().setVisible(True)
        self.tableWidgetlist.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetlist.verticalHeader().setVisible(True)

    def popolaListaVendita(self):
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, data.nFarmMagaz):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if(colonna == 0):
                    item.setText(_translate("cassa", data.listaFarmaciMagazzino[riga].nome))
                if(colonna == 1):
                    item.setText(_translate("cassa", str(data.listaFarmaciMagazzino[riga].giacenza)))
                if(colonna == 2):
                    item.setText(_translate("cassa", str(data.listaFarmaciMagazzino[riga].prezzo)))
                if(colonna == 3):
                    item.setText(_translate("cassa", str(data.listaFarmaciMagazzino[riga].codice)))
        for riga in range(data.nFarmMagaz, data.nProdMagaz + data.nFarmMagaz):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetlist.setItem(riga, colonna, item)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                item = self.tableWidgetlist.item(riga, colonna)
                if(colonna == 0):
                    item.setText(_translate("cassa", data.listaProdottiMagazzino[riga - data.nFarmMagaz].nome))
                if(colonna == 1):
                    item.setText(_translate("cassa", str(data.listaProdottiMagazzino[riga - data.nFarmMagaz].giacenza)))
                if(colonna == 2):
                    item.setText(_translate("cassa", str(data.listaProdottiMagazzino[riga - data.nFarmMagaz].prezzo)))
                if(colonna == 3):
                    item.setText(_translate("cassa", str(data.listaProdottiMagazzino[riga - data.nFarmMagaz].codice)))

    def ricercaArticolo(self):
        from tkinter import messagebox
        param = self.ricercale.text()
        if (param == ""):
            messagebox.showinfo("Errore", "Imposta almeno un carattere prima della ricerca")
        else:
            prodottiRicercati = []
            for element in data.listaFarmaciMagazzino:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
            for element in data.listaProdottiMagazzino:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
            p = ""
            for x in range(len(prodottiRicercati)):
                p += str(prodottiRicercati[x].nome +"  "+str(prodottiRicercati[x].giacenza)+"  "+prodottiRicercati[x].codice+"  "+str(prodottiRicercati[x].prezzo)+"€"+"\n")
            if(p==""):
                messagebox.showinfo("Errore", "Non è stato trovato alcun farmaco")
            else:
                messagebox.showinfo("Articolo/i", p)

    def selezionaProdotto(self):
        from tkinter import messagebox
        param = self.codicele.text()

        if self.quantitaprodsb.value() == 0:
            messagebox.showinfo("Errore", "Inserisci la quantità da aquistare")
            return

        for element in data.listaFarmaciMagazzino:
            if param == element.codice:
                nProdSelezionati = len(self.prodSelezionati)
                self.prodSelezionati.append(element)

                if self.quantitaprodsb.value() <= self.prodSelezionati[nProdSelezionati].giacenza:
                    self.creaCarrello()
                    self.popolaCarrello(nProdSelezionati)
                    return
                else:
                    self.prodSelezionati.remove(element)
                    messagebox.showinfo("Errore", "La quantità inserita è maggiore della giacenza dell'articolo")
                    return

        for element in data.listaProdottiMagazzino:
            if param == element.codice:
                nProdSelezionati = len(self.prodSelezionati)
                self.prodSelezionati.append(element)

                if self.quantitaprodsb.value() <= self.prodSelezionati[nProdSelezionati].giacenza:
                    self.prodSelezionati.append(element)
                    self.creaCarrello()
                    self.popolaCarrello(nProdSelezionati)
                    return
                else:
                    self.prodSelezionati.remove(element)
                    messagebox.showinfo("Errore", "La quantità inserita è maggiore della giacenza dell'articolo")
                    return

        messagebox.showinfo("Errore","Inserisci il codice corretto")
        return

    def creaCarrello(self):
        self.tableWidgetcarrello.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetcarrello.setObjectName("tableWidget")
        self.tableWidgetcarrello.setColumnCount(4)
        self.tableWidgetcarrello.setRowCount(data.nFarmMagaz + data.nProdMagaz)
        for x in range(data.nFarmMagaz + data.nProdMagaz):
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

    def popolaCarrello(self, nProdSelezionati):
        _translate = QtCore.QCoreApplication.translate
        print(self.codicele.text())
        print(str(self.prodSelezionati[nProdSelezionati].prezzo))
        print(nProdSelezionati)
        print(len(self.prodSelezionati))
        for colonna in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(nProdSelezionati, colonna, item)
            item = self.tableWidgetcarrello.item(nProdSelezionati, colonna)
            if(colonna == 0):
                item.setText(_translate("cassa", self.prodSelezionati[nProdSelezionati].nome))
            if(colonna == 1):
                item.setText(_translate("cassa", str(self.quantitaprodsb.value())))
            if(colonna == 2):
                item.setText(_translate("cassa", str(self.prodSelezionati[nProdSelezionati].prezzo)))
            if(colonna == 3):
                item.setText(_translate("cassa", str(self.prodSelezionati[nProdSelezionati].codice)))







