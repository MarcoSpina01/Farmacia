from datetime import date
from random import randint
from tkinter import messagebox

from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneSistema.data import data
from GestioneFarmacia.GestioneVendite.Farmaco import Farmaco
from GestioneFarmacia.GestioneVendite.Vendita import Vendita

# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()

class Ui_Cassa(object):
    #Array di supporto funzionali al codice
    prodSelezionati = []
    totale = []

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


        self.prodSelezionati.clear
        self.totale.clear()
        self.creaListaVendita()
        self.popolaListaVendita()

        #eventi di click collegati a bottoni della schermata
        self.ricercabtn.clicked.connect(self.ricercaArticolo)
        self.carrellobtn.clicked.connect(self.selezionaProdotto)
        self.acquistabtn.clicked.connect(self.chiudiVendita)
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

    #Metodo associato al bottone returnToHome che permette di tornare alla schermata di home
    def returnToHome(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()
        self.prodSelezionati.clear()

    # Il metodo crea una tabella con numero di colonne fissate in base al numero di attributi di un prodotto
    # da voler mostrare e con numero di righe variabile in base al numero di prodotti differenti presenti
    # in magazzino
    def creaListaVendita(self):
        data.downloadMagazzino()
        self.tableWidgetlist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetlist.setObjectName("tableWidget")
        self.tableWidgetlist.setColumnCount(5)
        self.tableWidgetlist.setRowCount(data.nFarmMagaz + data.nProdMagaz)
        for i in range(0, 5):
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
        item = self.tableWidgetlist.horizontalHeaderItem(4)
        item.setText(_translate("cassa", "FlagRicetta"))
        self.tableWidgetlist.horizontalHeader().setVisible(True)
        self.tableWidgetlist.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidgetlist.verticalHeader().setVisible(True)

    # Il metodo consente di riempire la tabella creata precedentemente attraverso due cicli di lettura sui due liste
    # contenti rispettivamente farmaci e prodotti semplici presenti in magazzino
    def popolaListaVendita(self):
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, data.nFarmMagaz):
            for colonna in range(0, 5):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                match colonna:
                    case 0:
                        item.setText(_translate("cassa", data.listaFarmaciMagazzino[riga].nome))
                    case 1:
                        item.setText(_translate("cassa", str(data.listaFarmaciMagazzino[riga].giacenza)))
                    case 2:
                        item.setText(_translate("cassa", str(data.listaFarmaciMagazzino[riga].prezzo)))
                    case 3:
                        item.setText(_translate("cassa", str(data.listaFarmaciMagazzino[riga].codice)))
                    case 4:
                        match data.listaFarmaciMagazzino[riga].flagRicetta:
                            case False, None:
                                item.setText(_translate("cassa", "Dispensabile"))
                            case _:
                                item.setText(_translate("cassa", "Non dispensabile"))

        for riga in range(data.nFarmMagaz, data.nProdMagaz + data.nFarmMagaz):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidgetlist.setItem(riga, colonna, item)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                item = self.tableWidgetlist.item(riga, colonna)
                match colonna:
                    case 0:
                        item.setText(_translate("cassa", data.listaProdottiMagazzino[riga - data.nFarmMagaz].nome))
                    case 1:
                        item.setText(
                            _translate("cassa", str(data.listaProdottiMagazzino[riga - data.nFarmMagaz].giacenza)))
                    case 2:
                        item.setText(
                            _translate("cassa", str(data.listaProdottiMagazzino[riga - data.nFarmMagaz].prezzo)))
                    case 3:
                        item.setText(
                            _translate("cassa", str(data.listaProdottiMagazzino[riga - data.nFarmMagaz].codice)))

    # Il seguente metodo inizializza una nuova lista contenente tutti i prodotti o farmaci il cui nome o codice
    # contenga i caratteri che l'utente inserisce
    def ricercaArticolo(self):
        param = self.ricercale.text()
        if (param == ""):
            self.popolaListaVendita()
            return
        else:
            prodottiRicercati = []
            for element in data.listaFarmaciMagazzino:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
            for element in data.listaProdottiMagazzino:
                if param in element.nome or param in element.codice:
                    prodottiRicercati.append(element)
        self.popolaRicerca(prodottiRicercati)

    # Il seguente metodo svuota la tabella dei prodotti presenti in magazzino per poi ricrearla utilizzando
    # la lista di prodotti che rispondono ai criteri della ricerca
    def popolaRicerca(self, prodRicercati):
        self.tableWidgetlist.clear()
        self.creaListaVendita()
        item = self.tableWidgetlist.horizontalHeaderItem(0)
        _translate = QtCore.QCoreApplication.translate
        item.setText(_translate("cassa", "Prodotto"))
        item = self.tableWidgetlist.horizontalHeaderItem(1)
        item.setText(_translate("cassa", "Quantità"))
        item = self.tableWidgetlist.horizontalHeaderItem(2)
        item.setText(_translate("cassa", "Prezzo"))
        item = self.tableWidgetlist.horizontalHeaderItem(3)
        item.setText(_translate("cassa", "Codice"))
        item = self.tableWidgetlist.horizontalHeaderItem(4)
        item.setText(_translate("cassa", "FlagRicetta"))
        for riga in range(0, len(prodRicercati)):
            for colonna in range(0, 5):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetlist.setItem(riga, colonna, item)
                item = self.tableWidgetlist.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("cassa", prodRicercati[riga].nome))
                if (colonna == 1):
                    item.setText(_translate("cassa", str(prodRicercati[riga].giacenza)))
                if (colonna == 2):
                    item.setText(_translate("cassa", str(prodRicercati[riga].prezzo)))
                if (colonna == 3):
                    item.setText(_translate("cassa", str(prodRicercati[riga].codice)))
                if (colonna == 4):
                    if (isinstance(prodRicercati[riga], Farmaco)):
                        if (((prodRicercati[riga].flagRicetta) == False) or (prodRicercati[riga].flagRicetta is None)):
                            item.setText(_translate("cassa", "Dispensabile"))
                        else:
                            item.setText(_translate("cassa", "Non dispensabile"))


    # Il seguente metodo gestisce la selezione di un prodotto dal magazzino e la sua aggiunta al carrello, la modifica
    # della quantità di selezione e quindi l'eventuale rimozione
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

        for element in data.listaProdottiMagazzino:
            if param == element.codice:
                nProdSelezionati = len(self.prodSelezionati)
                self.prodSelezionati.append(element)

                if self.quantitaprodsb.value() <= self.prodSelezionati[nProdSelezionati].giacenza:
                    self.prodSelezionati[nProdSelezionati].quantita = self.quantitaprodsb.value()
                    for x in range (nProdSelezionati):
                        if param == self.prodSelezionati[x].codice:
                            elemrimosso = self.prodSelezionati.pop(x)
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

        messagebox.showinfo("Errore","Inserisci il codice corretto")
        return

    # Il seguente metodo crea una tabella per i prodotti da acquistare
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

    # Il seguente metodo gestisce il riempimento della tabella creata precedentemente relativa al carrello
    def popolaCarrello(self, nProdSelezionati):
        _translate = QtCore.QCoreApplication.translate
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
        self.totale.append(self.prodSelezionati[nProdSelezionati].prezzo * self.quantitaprodsb.value())

    # Il seguente metodo in particolare gestisce l'eliminazione di un prodotto e quindi
    # la conseguente variazione del carrello
    def modificaCarrello(self, riga, elemrimosso):
        _translate = QtCore.QCoreApplication.translate
        for colonna in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidgetcarrello.setItem(riga, colonna, item)
            item = self.tableWidgetcarrello.item(riga, colonna)
            if(colonna == 0):
                item.setText(_translate("cassa", elemrimosso.nome))
            if(colonna == 1):
                item.setText(_translate("cassa", str(self.quantitaprodsb.value())))
            if(colonna == 2):
                item.setText(_translate("cassa", str(elemrimosso.prezzo)))
            if(colonna == 3):
                item.setText(_translate("cassa", str(elemrimosso.codice)))
        self.totale[riga] = elemrimosso.prezzo*self.quantitaprodsb.value()

    # Il seguente metodo aggiorna dopo la conferma della vendita tutte le liste di dati e i file pickle
    # che le contengono, salvando il resoconto della vendita nell'archivio
    def chiudiVendita(self):
        if not self.prodSelezionati:
            messagebox.showinfo("Errore", "Inserisci almeno un prodotto nel carrello")
            return
        check2 = False
        data.downloadMagazzino()
        for element in self.prodSelezionati:
            for prodotto in data.listaProdottiMagazzino:
                if (element.codice == prodotto.codice):
                    if (element.quantita == prodotto.giacenza):
                        data.listaFarmaciMagazzino.remove(prodotto)
                    else:
                        prodotto.giacenza -= element.quantita
                    check2 = True

            if not check2:
                for farmaco in data.listaFarmaciMagazzino:
                    if element.codice == farmaco.codice:
                        if element.quantita == farmaco.giacenza:
                            data.listaFarmaciMagazzino.remove(farmaco)
                        else:
                            farmaco.giacenza -= element.quantita
        tmp = str(sum(self.totale))
        messagebox.showinfo("Spesa totale", "Il totale è " + tmp[0:5] + "€" )
        self.returnToHome()
        self.aggiornaArchivio(tmp)
        data.uploadMagazzino()
        data.downloadMagazzino()
        self.popolaListaVendita()

    def aggiornaArchivio(self, tmp):
        data.downloadArchivioVendite()
        if not(self.generaCodice() == 0):
            today = date.today()
            vendita = Vendita(self.generaCodice(), tmp, today)
            data.archivioVendite.append(vendita)
            data.uploadArchivioVendite()
        else:
            self.aggiornaArchivio()

    def generaCodice(self):
        codice = randint(1,1000000)
        for element in data.archivioVendite:
            if codice == element.codice:
                return 0
        return codice






