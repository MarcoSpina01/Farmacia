from datetime import date
from random import randint
from tkinter import messagebox

from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneFarmacia.GestioneSistema.data import data
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneMagazzino.Ordine import Ordine

gestore = Gestore()

class Ui_pfizer(object):

    nProdSelezionati = 0
    prodSelezionati = []
    totale = []

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
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth() + "loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ricercafornitorebtn.setIcon(icon)
        self.ricercafornitorebtn.setObjectName("ricercafornitorebtn")
        self.lineEdit = QtWidgets.QLineEdit(pfizer)
        self.lineEdit.setGeometry(QtCore.QRect(140, 380, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.codicele = QtWidgets.QLineEdit(pfizer)
        self.codicele.setGeometry(QtCore.QRect(70, 500, 131, 20))
        self.codicele.setObjectName("codicele")
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
        self.carrellobtn.setGeometry(QtCore.QRect(290, 530, 131, 41))
        self.carrellobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.carrellobtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconacarrello.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carrellobtn.setIcon(icon1)
        self.carrellobtn.setIconSize(QtCore.QSize(30, 30))
        self.carrellobtn.setObjectName("carrellobtn")
        self.label_3 = QtWidgets.QLabel(pfizer)
        self.label_3.setGeometry(QtCore.QRect(440, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(pfizer)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 951, 601))
        self.frame.setStyleSheet("background-image: url("+ gestore.returnPth() +"loghi-icone/sfondopfizer.PNG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(pfizer)
        self.pushButton.setGeometry(QtCore.QRect(700, 510, 61, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconaindietro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.homebtn = QtWidgets.QPushButton(pfizer)
        self.homebtn.setGeometry(QtCore.QRect(780, 520, 101, 31))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon3)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.tableWidgetlist = QtWidgets.QTableWidget(pfizer)
        self.tableWidgetlist.setGeometry(QtCore.QRect(20, 70, 451, 231))
        self.tableWidgetlist.setObjectName("tableWidgetlist")
        self.tableWidgetlist.setColumnCount(0)
        self.tableWidgetlist.setRowCount(0)
        self.tableWidgetcarrello = QtWidgets.QTableWidget(pfizer)
        self.tableWidgetcarrello.setGeometry(QtCore.QRect(480, 70, 451, 231))
        self.tableWidgetcarrello.setObjectName("tableWidgetcarrello")
        self.tableWidgetcarrello.setColumnCount(0)
        self.tableWidgetcarrello.setRowCount(0)
        self.acquistabtn = QtWidgets.QPushButton(pfizer)
        self.acquistabtn.setGeometry(QtCore.QRect(790, 320, 121, 41))
        self.acquistabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acquistabtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(gestore.returnPth()+ "loghi-icone/iconadollaro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acquistabtn.setIcon(icon4)
        self.acquistabtn.setIconSize(QtCore.QSize(30, 30))
        self.acquistabtn.setObjectName("acquistabtn")
        self.frame.raise_()
        self.label_4.raise_()
        self.ricercafornitorebtn.raise_()
        self.lineEdit.raise_()
        self.codicele.raise_()
        self.label.raise_()
        self.quantitaprodsb.raise_()
        self.carrellobtn.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.homebtn.raise_()
        self.tableWidgetlist.raise_()
        self.tableWidgetcarrello.raise_()
        self.acquistabtn.raise_()

        #Metodi di creazione e popolazione della widget list dei prodotti del fornitore
        self.creaListaProdotti()
        self.popolaListaProdotti()

        #Associazione di metodi ad eventi di click
        self.homebtn.clicked.connect(self.returnToHome)
        self.pushButton.clicked.connect(self.returnToFornitori)
        self.carrellobtn.clicked.connect(self.selezionaProdotto)
        self.acquistabtn.clicked.connect(self.chiudiOrdine)
        self.ricercafornitorebtn.clicked.connect(self.ricercaArticolo)

        #Pulizia degli array
        self.prodSelezionati.clear()
        self.totale.clear()


        self.retranslateUi(pfizer)
        QtCore.QMetaObject.connectSlotsByName(pfizer)

    def retranslateUi(self, pfizer):
        _translate = QtCore.QCoreApplication.translate
        pfizer.setWindowTitle(_translate("pfizer", "Form"))
        self.label_4.setText(_translate("pfizer", "Lista prodotti:"))
        self.ricercafornitorebtn.setText(_translate("pfizer", "  Ricerca"))
        self.label.setText(_translate("pfizer", "Inserisci codice e quantità da comprare"))
        self.carrellobtn.setText(_translate("pfizer", "Metti nel carrello"))
        self.label_3.setText(_translate("pfizer", "Carrello:"))
        self.homebtn.setText(_translate("pfizer", "Home"))
        self.acquistabtn.setText(_translate("pfizer", "  Acquista"))

    #Metodo associato al bottone returnToHome che permette di tornare alla schermata di home
    def returnToHome(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()
        self.prodSelezionati.clear()

    #Metodo associato al bottone che permette di tornare alla schermata di scelta fornitore
    def returnToFornitori(self):
        from GestioneFarmacia.Gui.GestioneMagazzino.sceltafornitore import Ui_Fornitori
        self.fornitori = QtWidgets.QFrame()
        self.ui = Ui_Fornitori()
        self.ui.setupUi(self.fornitori)
        self.fornitori.show()
        self.Frame.close()
        self.prodSelezionati.clear()

    #Metodo che permette di popolare la widget list con la lista dei prodotti e farmaci del fornitore
    def creaListaProdotti(self):
        data.downloadFornitore()
        self.tableWidgetlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetlist.setObjectName("tableWidget")
        self.tableWidgetlist.setColumnCount(4)
        self.tableWidgetlist.setRowCount(data.nFarmForn + data.nProdForn)
        for i in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetlist.setHorizontalHeaderItem(i, item)

        self.tableWidgetlist.horizontalHeader().setVisible(True)
        self.tableWidgetlist.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetlist.verticalHeader().setVisible(True)

    #Metodo che permette di popolare la lista dei prodotti del fornitore leggendo dal file pickle
    def popolaListaProdotti(self):
        item = self.tableWidgetlist.horizontalHeaderItem(0)
        _translate = QtCore.QCoreApplication.translate
        item.setText(_translate("pfizer", "Prodotto"))
        item = self.tableWidgetlist.horizontalHeaderItem(1)
        item.setText(_translate("pfizer", "Quantità"))
        item = self.tableWidgetlist.horizontalHeaderItem(2)
        item.setText(_translate("pfizer", "Prezzo"))
        item = self.tableWidgetlist.horizontalHeaderItem(3)
        item.setText(_translate("pfizer", "Codice"))
        for riga in range(0, data.nFarmForn):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("pfizer", data.listaFarmaciFornitore[riga].nome))
                if (colonna == 1):
                    item.setText(_translate("pfizer", str(data.listaFarmaciFornitore[riga].giacenza)))
                if (colonna == 2):
                    item.setText(_translate("pfizer", str(data.listaFarmaciFornitore[riga].prezzo)))
                if (colonna == 3):
                    item.setText(_translate("pfizer", str(data.listaFarmaciFornitore[riga].codice)))
        for riga in range(data.nFarmForn, data.nFarmForn + data.nProdForn):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("pfizer", data.listaProdottiFornitore[riga - data.nFarmForn].nome))
                if (colonna == 1):
                    item.setText(_translate("pfizer", str(data.listaProdottiFornitore[riga - data.nFarmForn].giacenza)))
                if (colonna == 2):
                    item.setText(_translate("pfizer", str(data.listaProdottiFornitore[riga - data.nFarmForn].prezzo)))
                if (colonna == 3):
                    item.setText(_translate("pfizer", str(data.listaProdottiFornitore[riga - data.nFarmForn].codice)))

    #Metodo di ricerca di un articolo nella lista dei prodotti fornitore
    def ricercaArticolo(self):
        param = self.lineEdit.text()
        if (param == ""):
            self.popolaListaProdotti()
            return
        else:
            prodottiRicercati = []
            for element in data.listaFarmaciFornitore:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
            for element in data.listaProdottiFornitore:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
        self.popolaRicerca(prodottiRicercati)

    #Metodo che restituisce nella widget list i prodotti ricercati
    def popolaRicerca(self, prodRicercati):
        self.tableWidgetlist.clear()
        self.creaListaProdotti()
        item = self.tableWidgetlist.horizontalHeaderItem(0)
        _translate = QtCore.QCoreApplication.translate
        item.setText(_translate("pfizer", "Prodotto"))
        item = self.tableWidgetlist.horizontalHeaderItem(1)
        item.setText(_translate("pfizer", "Quantità"))
        item = self.tableWidgetlist.horizontalHeaderItem(2)
        item.setText(_translate("pfizer", "Prezzo"))
        item = self.tableWidgetlist.horizontalHeaderItem(3)
        item.setText(_translate("pfizer", "Codice"))
        for riga in range(0, len(prodRicercati)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("pfizer", prodRicercati[riga].nome))
                if (colonna == 1):
                    item.setText(_translate("pfizer", str(prodRicercati[riga].giacenza)))
                if (colonna == 2):
                    item.setText(_translate("pfizer", str(prodRicercati[riga].prezzo)))
                if (colonna == 3):
                    item.setText(_translate("pfizer", str(prodRicercati[riga].codice)))

    #Metodo di creazione della lista di prodotti nel carrello
    #Permette di creare la widgetlist dei prodotti selezionati dalla lista articoli del fornitore
    def creaCarrello(self):
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
        item.setText(_translate("pfizer", "Prodotto"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(1)
        item.setText(_translate("pfizer", "Quantità"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(2)
        item.setText(_translate("pfizer", "Prezzo"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(3)
        item.setText(_translate("pfizer", "Codice"))
        self.tableWidgetcarrello.horizontalHeader().setVisible(True)
        self.tableWidgetcarrello.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetcarrello.verticalHeader().setVisible(True)

    #Metodo che permette di selezionare un prodotto nella lista fornitore controllandone il codice e la giacienza
    def selezionaProdotto(self):
        from tkinter import messagebox
        param = self.codicele.text()

        if self.quantitaprodsb.value() == 0:
            messagebox.showinfo("Errore", "Inserisci la quantità da aquistare")
            return

        for element in data.listaFarmaciFornitore:
            if param == element.codice:
                nProdSelezionati = len(self.prodSelezionati)
                self.prodSelezionati.append(element)

                if self.quantitaprodsb.value() <= self.prodSelezionati[nProdSelezionati].giacenza:
                    self.prodSelezionati[nProdSelezionati].quantita = self.quantitaprodsb.value()
                    for x in range (nProdSelezionati):
                        if param == self.prodSelezionati[x].codice:
                            elemrimosso = self.prodSelezionati[x]
                            self.prodSelezionati.pop()
                            messagebox.showinfo("Imprevisto",
                                                 "L'articolo è già stato selezionato in precedenza, è stato eliminato dal carrello"
                                                 " a favore dell'inserimento del prodotto appena selezionato")
                            nProdSelezionati -= 1

                            self.creaCarrello()
                            self.modificaCarrello(x, elemrimosso)
                            return

                    self.creaCarrello()
                    self.popolaCarrello(nProdSelezionati)
                    return
                else:
                    self.prodSelezionati.remove(element)
                    messagebox.showinfo("Errore", "La quantità inserita è maggiore della giacenza dell'articolo")
                    return

        for element in data.listaProdottiFornitore:
            if param == element.codice:
                nProdSelezionati = len(self.prodSelezionati)
                self.prodSelezionati.append(element)

                if self.quantitaprodsb.value() <= self.prodSelezionati[nProdSelezionati].giacenza:
                    self.prodSelezionati[nProdSelezionati].quantita = self.quantitaprodsb.value()
                    for x in range (nProdSelezionati):
                        if param == self.prodSelezionati[x].codice:
                            self.prodSelezionati.remove(self.prodSelezionati[x])
                            messagebox.showinfo("Imprevisto",
                                                "L'articolo è già stato selezionato in precedenza, è stato eliminato dal carrello"
                                                " a favore dell'inserimento del prodotto appena selezionato")
                            nProdSelezionati -= 1
                            self.creaCarrello()
                            self.popolaCarrello(nProdSelezionati)
                            return

                    self.creaCarrello()
                    self.popolaCarrello(nProdSelezionati)
                    return
                else:
                    self.prodSelezionati.remove(element)
                    messagebox.showinfo("Errore", "La quantità inserita è maggiore della giacenza dell'articolo")
                    return

        messagebox.showinfo("Errore","Inserisci il codice corretto")
        return

    #Metodo che popola il carrello con i prodotti selezionati
    def popolaCarrello(self, nProdSelezionati):
        _translate = QtCore.QCoreApplication.translate
        for colonna in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(nProdSelezionati, colonna, item)
            item = self.tableWidgetcarrello.item(nProdSelezionati, colonna)
            if(colonna == 0):
                item.setText(_translate("pfizer", self.prodSelezionati[nProdSelezionati].nome))
            if(colonna == 1):
                item.setText(_translate("pfizer", str(self.quantitaprodsb.value())))
            if(colonna == 2):
                item.setText(_translate("pfizer", str(self.prodSelezionati[nProdSelezionati].prezzo)))
            if(colonna == 3):
                item.setText(_translate("pfizer", str(self.prodSelezionati[nProdSelezionati].codice)))
        self.totale.append(self.prodSelezionati[nProdSelezionati].prezzo*self.quantitaprodsb.value())

    #Metodo che permette la modifica della lista di prodotti nel carrello rimuovendone quelli mal selezionati
    def modificaCarrello(self, riga, elemrimosso):
        _translate = QtCore.QCoreApplication.translate
        for colonna in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(riga, colonna, item)
            item = self.tableWidgetcarrello.item(riga, colonna)
            if(colonna == 0):
                item.setText(_translate("pfizer", elemrimosso.nome))
            if(colonna == 1):
                item.setText(_translate("pfizer", str(self.quantitaprodsb.value())))
            if(colonna == 2):
                item.setText(_translate("pfizer", str(elemrimosso.prezzo)))
            if(colonna == 3):
                item.setText(_translate("pfizer", str(elemrimosso.codice)))
        self.totale[riga] = elemrimosso.prezzo*self.quantitaprodsb.value()

    #Metodo associato ad un bottone che permette di chiudere l'ordine di prodotti e farmaci dalla lista fornitori
    def chiudiOrdine(self):
        if not self.prodSelezionati:
            messagebox.showinfo("Errore", "Inserisci almeno un prodotto nel carrello")
            return
            check = False
            check2 = False
            data.downloadMagazzino()
            data.downloadFornitore()
            for element in self.prodSelezionati:
                for prodotto in data.listaProdottiFornitore:
                    if (element.codice == prodotto.codice):
                        if (element.quantita == prodotto.giacenza):
                            data.listaFarmaciFornitore.remove(prodotto)
                        else:
                            prodotto.giacenza -= element.quantita
                        check2 = True
                        for prodottoM in data.listaProdottiMagazzino:
                            if (element.codice == prodottoM.codice):
                                prodottoM.giacenza += element.quantita
                                check = True
                        if (not (check)):
                            data.listaProdottiMagazzino.append(element)
                            data.listaProdottiMagazzino[
                                len(data.listaProdottiMagazzino) - 1].giacenza = element.quantita

                if (not (check2)):
                    check = False
                    for farmacoM in data.listaFarmaciMagazzino:
                        if (element.codice == farmacoM.codice):
                            farmacoM.giacenza += element.quantita
                            check = True
                    if (not (check)):
                        data.listaFarmaciMagazzino.append(element)
                        data.listaFarmaciMagazzino[len(data.listaFarmaciMagazzino) - 1].giacenza = element.quantita
                    for farmacoF in data.listaFarmaciFornitore:
                        if (element.codice == farmacoF.codice):
                            if (element.quantita == farmacoF.giacenza):
                                data.listaFarmaciFornitore.remove(farmacoF)
                            else:
                                farmacoF.giacenza -= element.quantita
            tmp = str(sum(self.totale))
            messagebox.showinfo("Spesa totale", "Il totale è " + tmp[0:5] + "€")
            self.returnToHome()
            self.aggiornaArchivio(tmp)
            data.uploadMagazzino()
            data.uploadFornitore()
            data.downloadMagazzino()
            data.downloadFornitore()
            self.popolaListaProdotti()

    #Metodo che aggiorna l'archivio una volta chiuso l'ordine
    def aggiornaArchivio(self, tmp):
            data.downloadArchivioOrdini()
            if not (self.generaCodice() == 0):
                today = date.today()
                ordine = Ordine(self.generaCodice(), "Pfizer", tmp, today)
                data.archivioOrdini.append(ordine)
                data.uploadArchivioOrdini()
            else:
                self.aggiornaArchivio()

    #Metodo che genera il codice dell'ordine concluso
    def generaCodice(self):
            codice = randint(1, 1000000)
            for element in data.archivioOrdini:
                if codice == element.codice:
                    return 0
            return codice







