from datetime import date
from random import randint
from tkinter import messagebox

from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneSistema.data import data
from GestioneFarmacia.GestioneMagazzino.Ordine import Ordine

# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()

class Ui_angelini(object):

    #Array e variabili di supporto funzionali alla classe
    nProdSelezionati = 0
    totale = []
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
        self.codicele = QtWidgets.QLineEdit(angelini)
        self.codicele.setGeometry(QtCore.QRect(650, 190, 113, 20))
        self.codicele.setObjectName("codicele")
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
        self.codicele.raise_()
        self.label.raise_()
        self.carrellobtn.raise_()
        self.acquistabtn.raise_()
        self.homebtn.raise_()
        self.pushButton.raise_()
        self.tableWidgetlist.raise_()
        self.tableWidgetcarrello.raise_()

        #Metodi di creazione e popolazione della widget list dei prodotti del fornitore
        self.creaListaProdotti()
        self.popolaListaProdotti()

        #Associazione di metodi ad eventi di click
        self.homebtn.clicked.connect(self.returnToHome)
        self.pushButton.clicked.connect(self.returnToFornitori)
        self.ricercafornitorebtn.clicked.connect(self.ricercaArticolo)
        self.carrellobtn.clicked.connect(self.selezionaProdotto)
        self.acquistabtn.clicked.connect(self.chiudiOrdine)

        #Pulizia degli array
        self.prodSelezionati.clear()
        self.totale.clear()

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
        for i in range(0, data.nFarmForn + data.nProdForn):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetlist.setHorizontalHeaderItem(i, item)

        self.tableWidgetlist.horizontalHeader().setVisible(True)
        self.tableWidgetlist.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetlist.verticalHeader().setVisible(True)

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
        item.setText(_translate("angelini", "Prodotto"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(1)
        item.setText(_translate("angelini", "Quantità"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(2)
        item.setText(_translate("angelini", "Prezzo"))
        item = self.tableWidgetcarrello.horizontalHeaderItem(3)
        item.setText(_translate("angelini", "Codice"))
        self.tableWidgetcarrello.horizontalHeader().setVisible(True)
        self.tableWidgetcarrello.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetcarrello.verticalHeader().setVisible(True)

    #Metodo che permette di popolare la lista dei prodotti del fornitore leggendo dal file pickle
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
        item.setText(_translate("angelini", "Prodotto"))
        item = self.tableWidgetlist.horizontalHeaderItem(1)
        item.setText(_translate("angelini", "Quantità"))
        item = self.tableWidgetlist.horizontalHeaderItem(2)
        item.setText(_translate("angelini", "Prezzo"))
        item = self.tableWidgetlist.horizontalHeaderItem(3)
        item.setText(_translate("angelini", "Codice"))
        for riga in range(0, len(prodRicercati)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("angelini", prodRicercati[riga].nome))
                if (colonna == 1):
                    item.setText(_translate("angelini", str(prodRicercati[riga].giacenza)))
                if (colonna == 2):
                    item.setText(_translate("angelini", str(prodRicercati[riga].prezzo)))
                if (colonna == 3):
                    item.setText(_translate("angelini", str(prodRicercati[riga].codice)))

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
                item.setText(_translate("angelini", self.prodSelezionati[nProdSelezionati].nome))
            if(colonna == 1):
                item.setText(_translate("angelini", str(self.quantitaprodsb.value())))
            if(colonna == 2):
                item.setText(_translate("angelini", str(self.prodSelezionati[nProdSelezionati].prezzo)))
            if(colonna == 3):
                item.setText(_translate("angelini", str(self.prodSelezionati[nProdSelezionati].codice)))
        self.totale.append(self.prodSelezionati[nProdSelezionati].prezzo * self.quantitaprodsb.value())

    #Metodo che permette la modifica della lista di prodotti nel carrello rimuovendone quelli mal selezionati
    def modificaCarrello(self, riga, elemrimosso):
        _translate = QtCore.QCoreApplication.translate
        for colonna in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(riga, colonna, item)
            item = self.tableWidgetcarrello.item(riga, colonna)
            if(colonna == 0):
                item.setText(_translate("angelini", elemrimosso.nome))
            if(colonna == 1):
                item.setText(_translate("angelini", str(self.quantitaprodsb.value())))
            if(colonna == 2):
                item.setText(_translate("angelini", str(elemrimosso.prezzo)))
            if(colonna == 3):
                item.setText(_translate("angelini", str(elemrimosso.codice)))
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
                    if (not(check)):
                        data.listaProdottiMagazzino.append(element)
                        data.listaProdottiMagazzino[len(data.listaProdottiMagazzino) - 1].giacenza = element.quantita

            if not check2:
                check = False
                for farmacoM in data.listaFarmaciMagazzino:
                    if element.codice == farmacoM.codice:
                        farmacoM.giacenza += element.quantita
                        check = True
                if not check:
                    data.listaFarmaciMagazzino.append(element)
                    data.listaFarmaciMagazzino[len(data.listaFarmaciMagazzino) - 1].giacenza = element.quantita
                for farmacoF in data.listaFarmaciFornitore:
                    if element.codice == farmacoF.codice:
                        if element.quantita == farmacoF.giacenza:
                            data.listaFarmaciFornitore.remove(farmacoF)
                        else:
                            farmacoF.giacenza -= element.quantita
        tmp = str(sum(self.totale))
        messagebox.showinfo("Spesa totale", "Il totale è " + tmp[0:5] + "€" )
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
        if not(self.generaCodice() == 0):
            today = date.today()
            ordine = Ordine(self.generaCodice(), "Angelini", tmp, today)
            data.archivioOrdini.append(ordine)
            data.uploadArchivioOrdini()
        else:
            self.aggiornaArchivio()

    #Metodo che genera il codice dell'ordine concluso
    def generaCodice(self):
        codice = randint(1,1000000)
        for element in data.archivioOrdini:
            if codice == element.codice:
                return 0
        return codice



