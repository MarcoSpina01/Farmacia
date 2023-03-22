
from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneFarmacia.GestioneSistema.data import data
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneVendite.Farmaco import Farmaco
from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

gestore = Gestore()

class Ui_pfizer(object):

    nProdSelezionati = 0
    prodSelezionati = []

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


        self.creaListaProdotti()
        self.popolaListaProdotti()

        self.homebtn.clicked.connect(self.returnToHome)
        self.pushButton.clicked.connect(self.returnToFornitori)


        self.ricercafornitorebtn.clicked.connect(self.ricercaArticolo)
        self.prodSelezionati.clear()
        self.carrellobtn.clicked.connect(self.selezionaProdotto)
        # self.acquistabtn.clicked.connect(self.chiudiOrdine)

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
                p += str(
                    prodottiRicercati[x].nome + "  " + str(prodottiRicercati[x].giacenza) + "  " + prodottiRicercati[
                        x].codice + "  " + str(prodottiRicercati[x].prezzo) + "€" + "\n")
            if (p == ""):
                messagebox.showinfo("Errore", "Non è stato trovato alcun farmaco")
            else:
                messagebox.showinfo("Articolo/i", p)

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
                    for x in range (nProdSelezionati):
                        if param == self.prodSelezionati[x].codice:
                            elemrimosso = self.prodSelezionati[x]
                            self.prodSelezionati.pop()
                            # messagebox.showinfo("Imprevisto",
                            #                     "L'articolo è già stato selezionato in precedenza, è stato eliminato dal carrello"
                            #                     " a favore dell'inserimento del prodotto appena selezionato")
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


    # def chiudiOrdine(self):
    #     for element in self.prodSelezionati:
    #         if (isinstance(element, Prodotto)):
    #            for prodottoM in data.listaProdottiMagazzino:
    #                if (element.codice == prodottoM.codice):
    #                    prodottoM.giacenza += self.quantitaprodsb.value()
    #                else:
    #                    data.listaProdottiMagazzino.append(element)
    #
    #                for prodottoF in data.listaProdottiFornitore:
    #                    if (element.codice == prodottoF.codice):
    #                        if(self.quantitaprodsb.value() == prodottoF.giacenza):
    #                            data.listaProdottiFornitore.remove(prodottoF)
    #                        else:
    #                            prodottoF.giacenza -= self.quantitaprodsb.value()
    #
    #         if (isinstance(element, Farmaco)):
    #            for farmacoM in data.listaFarmaciMagazzino:
    #               if (element.codice == farmacoM.codice):
    #                    farmacoM.giacenza += self.quantitaprodsb.value()
    #               else:
    #                   data.listaFarmaciMagazzino.append(element)
    #            for farmacoF in data.listaFarmaciFornitore:
    #                 if (element.codice == farmacoF.codice):
    #                    if(self.quantitaprodsb.value() == farmacoF.giacenza):
    #                        data.listaFarmaciFornitore.remove(farmacoF)
    #                    else:
    #                        farmacoF.giacenza -= self.quantitaprodsb.value()
    #     data.uploadMagazzino()
    #     data.uploadFornitore()






