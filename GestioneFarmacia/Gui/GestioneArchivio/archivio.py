from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from GestioneFarmacia.GestioneSistema.data import data
from GestioneFarmacia.GestioneSistema.gestione import Gestore

gestore = Gestore()

class Ui_Archivio(object):
    def setupUi(self, Form):
        self.Frame = Form
        Form.setObjectName("Form")
        Form.resize(827, 495)
        Form.setStyleSheet("")
        columns = ['Nome', 'Cognome', 'Cf', 'Email', 'Sesso', 'Indirizzo']
        columnsesiti = ['Codice', 'CF', 'Data', 'Stato', 'Esito']
        self.Archivio = QtWidgets.QFrame(Form)
        self.Archivio.setGeometry(QtCore.QRect(0, -10, 831, 531))
        self.Archivio.setStyleSheet("background-image: url("+gestore.returnPth()+"loghi-icone/schermataarchivio.PNG);")
        self.Archivio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Archivio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Archivio.setObjectName("Archivio")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(410, 250, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.homebtn = QtWidgets.QPushButton(Form)
        self.homebtn.setGeometry(QtCore.QRect(710, 240, 101, 31))
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 250, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.tableWidgetordini = QtWidgets.QTableWidget(Form)
        self.tableWidgetordini.setGeometry(QtCore.QRect(410, 40, 391, 161))
        self.tableWidgetordini.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetordini.setObjectName("tableWidgetordini")
        self.tableWidgetordini.setColumnCount(0)
        self.tableWidgetordini.setRowCount(0)
        self.tableWidgetclienti = QtWidgets.QTableWidget(Form)
        self.tableWidgetclienti.setGeometry(QtCore.QRect(10, 40, 391, 161))
        self.tableWidgetclienti.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetclienti.setObjectName("tableWidgetclienti")
        self.tableWidgetclienti.setColumnCount(len(columns))
        self.tableWidgetclienti.setHorizontalHeaderLabels(columns)
        self.tableWidgetclienti.setRowCount(0)
        self.ricercaarchivioclientibtn = QtWidgets.QPushButton(Form)
        self.ricercaarchivioclientibtn.setGeometry(QtCore.QRect(210, 210, 91, 41))
        self.ricercaarchivioclientibtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercaarchivioclientibtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconalente.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ricercaarchivioclientibtn.setIcon(icon1)
        self.ricercaarchivioclientibtn.setObjectName("ricercaarchivioclientibtn")
        self.ricercaarchivioordinibtn = QtWidgets.QPushButton(Form)
        self.ricercaarchivioordinibtn.setGeometry(QtCore.QRect(610, 210, 91, 41))
        self.ricercaarchivioordinibtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercaarchivioordinibtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.ricercaarchivioordinibtn.setIcon(icon1)
        self.ricercaarchivioordinibtn.setObjectName("ricercaarchivioordinibtn")
        self.ricercaarchivioclienti = QtWidgets.QLineEdit(Form)
        self.ricercaarchivioclienti.setGeometry(QtCore.QRect(10, 220, 191, 21))
        self.ricercaarchivioclienti.setObjectName("ricercaarchivioclienti")
        self.ricercaarchivioordini = QtWidgets.QLineEdit(Form)
        self.ricercaarchivioordini.setGeometry(QtCore.QRect(410, 220, 191, 21))
        self.ricercaarchivioordini.setObjectName("ricercaarchivioordini")
        self.Ricercaappuntamentobtn = QtWidgets.QPushButton(Form)
        self.Ricercaappuntamentobtn.setGeometry(QtCore.QRect(610, 450, 91, 41))
        self.Ricercaappuntamentobtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ricercaappuntamentobtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Ricercaappuntamentobtn.setIcon(icon1)
        self.Ricercaappuntamentobtn.setObjectName("Ricercaappuntamentobtn")
        self.ricercaarchiviovenditebtn = QtWidgets.QPushButton(Form)
        self.ricercaarchiviovenditebtn.setGeometry(QtCore.QRect(210, 450, 91, 41))
        self.ricercaarchiviovenditebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ricercaarchiviovenditebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.ricercaarchiviovenditebtn.setIcon(icon1)
        self.ricercaarchiviovenditebtn.setObjectName("ricercaarchiviovenditebtn")
        self.tableWidgetvendite = QtWidgets.QTableWidget(Form)
        self.tableWidgetvendite.setGeometry(QtCore.QRect(10, 280, 391, 161))
        self.tableWidgetvendite.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetvendite.setObjectName("tableWidgetvendite")
        self.tableWidgetvendite.setColumnCount(0)
        self.tableWidgetvendite.setRowCount(0)
        self.ricercaappuntamento = QtWidgets.QLineEdit(Form)
        self.ricercaappuntamento.setGeometry(QtCore.QRect(410, 460, 191, 21))
        self.ricercaappuntamento.setObjectName("ricercaappuntamento")
        self.tableWidgetesiti = QtWidgets.QTableWidget(Form)
        self.tableWidgetesiti.setGeometry(QtCore.QRect(410, 280, 391, 161))
        self.tableWidgetesiti.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetesiti.setObjectName("tableWidgetesiti")
        self.tableWidgetesiti.setColumnCount(len(columnsesiti))
        self.tableWidgetesiti.setHorizontalHeaderLabels(columnsesiti)
        self.tableWidgetesiti.setRowCount(0)
        self.ricercaarchiviovendite = QtWidgets.QLineEdit(Form)
        self.ricercaarchiviovendite.setGeometry(QtCore.QRect(10, 460, 191, 21))
        self.ricercaarchiviovendite.setObjectName("ricercaarchiviovendite")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.ricercaarchivioordinibtn.clicked.connect(self.ricercaOrdiniPerFornitore)
        self.ricercaarchiviovenditebtn.clicked.connect(self.ricercaVendite)
        self.ricercaarchivioclientibtn.clicked.connect(self.ricercaClienti)
        self.Ricercaappuntamentobtn.clicked.connect(self.ricercaEsiti)
        self.homebtn.clicked.connect(self.returnToHome)
        self.creaArchivioVendite()
        self.popolaVendite()
        self.creaArchivioOrdini()
        self.popolaOrdini()
        self.creaArchivioClienti()
        self.popolaClienti()
        self.creaArchivioEsiti()
        self.popolaEsiti()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Archivio esiti"))
        self.homebtn.setText(_translate("Form", "Home"))
        self.label.setText(_translate("Form", "Archivio vendite"))
        self.ricercaarchivioclientibtn.setText(_translate("Form", "  Ricerca"))
        self.ricercaarchivioordinibtn.setText(_translate("Form", "  Ricerca"))
        self.Ricercaappuntamentobtn.setText(_translate("Form", "  Ricerca"))
        self.ricercaarchiviovenditebtn.setText(_translate("Form", "  Ricerca"))
        self.label_4.setText(_translate("Form", "Archivio clienti"))
        self.label_2.setText(_translate("Form", "Archivio ordini"))

    def returnToHome(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    #Il metodo gestisce la creazione di una tabella da popolare con tutti gli ordini effettuati
    def creaArchivioOrdini(self):
        data.downloadArchivioOrdini()
        self.tableWidgetordini.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetordini.setObjectName("tableWidget")
        self.tableWidgetordini.setColumnCount(4)
        self.tableWidgetordini.setRowCount(data.nOrdini)
        for i in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetordini.setHorizontalHeaderItem(i, item)
        self.tableWidgetordini.horizontalHeader().setVisible(True)
        self.tableWidgetordini.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidgetordini.verticalHeader().setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetordini.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice"))
        item = self.tableWidgetordini.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Fornitore"))
        item = self.tableWidgetordini.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Totale"))
        item = self.tableWidgetordini.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Data"))

    #Il metodo popola la tabella con tutti gli ordini effettuati
    def popolaOrdini(self):
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, data.nOrdini):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetordini.setItem(riga, colonna, item)
                item = self.tableWidgetordini.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("Form", str(data.archivioOrdini[riga].codice)))
                if (colonna == 1):
                    item.setText(_translate("Form", str(data.archivioOrdini[riga].fornitore)))
                if (colonna == 2):
                    item.setText(_translate("Form", str(data.archivioOrdini[riga].totale)[0:5] + "€"))
                if (colonna == 3):
                    item.setText(_translate("Form", str(data.archivioOrdini[riga].date)))

    #Il metodo gestisce la ricerca tra gli ordini (fatta per fornitore o per data) creand una lista temporanea di ordini
    def ricercaOrdiniPerFornitore(self):
        param = self.ricercaarchivioordini.text()
        ordiniRicercati = []
        if (param == ""):
            self.popolaOrdini()
            return
        for element in data.archivioOrdini:
            if (param in element.fornitore or param in element.date):
                ordiniRicercati.append(element)
        self.popolaRicerca(ordiniRicercati)

    #Il metodo aggiorna la tabella degli ordini in base alla ricerca effettuata dopo aver premuto il rispettivo bottone
    def popolaRicerca(self, ordiniRicercati):
        self.tableWidgetordini.clear()
        self.creaArchivioOrdini()
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, len(ordiniRicercati)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetordini.setItem(riga, colonna, item)
                item = self.tableWidgetordini.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("Form", str(ordiniRicercati[riga].codice)))
                if (colonna == 1):
                    item.setText(_translate("Form", str(ordiniRicercati[riga].fornitore)))
                if (colonna == 2):
                    item.setText(_translate("Form", str(ordiniRicercati[riga].totale)[0:5] + "€"))
                if (colonna == 3):
                    item.setText(_translate("Form", str(ordiniRicercati[riga].date)))

    # La gestione delle classi sottostanti è fatta allo stesso modo di quelle precedenti, vengono quindi creati e popolati
    # gli archivi di vendite, clienti e appuntamenti con la possibilità per ognuno di ricercare per i vari parametri
    # rispettivamente: data, nome e cognome, e codice fiscale

    def creaArchivioVendite(self):
        data.downloadArchivioVendite()
        self.tableWidgetvendite.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetvendite.setObjectName("tableWidget")
        self.tableWidgetvendite.setColumnCount(4)
        self.tableWidgetvendite.setRowCount(data.nVendite)
        for i in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetvendite.setHorizontalHeaderItem(i, item)
        self.tableWidgetvendite.horizontalHeader().setVisible(True)
        self.tableWidgetvendite.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidgetvendite.verticalHeader().setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetvendite.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice"))
        item = self.tableWidgetvendite.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Totale"))
        item = self.tableWidgetvendite.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Data"))

    def popolaVendite(self):
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, data.nVendite):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetvendite.setItem(riga, colonna, item)
                item = self.tableWidgetvendite.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("Form", str(data.archivioVendite[riga].codice)))
                if (colonna == 1):
                    item.setText(_translate("Form", str(data.archivioVendite[riga].totale)[0:5] + "€"))
                if (colonna == 2):
                    item.setText(_translate("Form", str(data.archivioVendite[riga].date)))

    def ricercaVendite(self):
        param = self.ricercaarchiviovendite.text()
        venditeRicercate = []
        if (param == ""):
            self.popolaVendite()
            return
        for element in data.archivioVendite:
            if (param in str(element.date)):
                venditeRicercate.append(element)
        self.popolaRicercaVendite(venditeRicercate)


    def popolaRicercaVendite(self, venditeRicercate):
        self.tableWidgetvendite.clear()
        self.creaArchivioVendite()
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, len(venditeRicercate)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetvendite.setItem(riga, colonna, item)
                item = self.tableWidgetvendite.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("Form", str(venditeRicercate[riga].codice)))
                if (colonna == 1):
                    item.setText(_translate("Form", str(venditeRicercate[riga].totale)[0:5] + "€"))
                if (colonna == 2):
                    item.setText(_translate("Form", str(venditeRicercate[riga].date)))

    def creaArchivioClienti(self):
        data.downloadClienti()
        self.tableWidgetclienti.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetclienti.setObjectName("tableWidget")
        self.tableWidgetclienti.setColumnCount(7)
        self.tableWidgetclienti.setRowCount(len(data.listaClienti))
        for i in range(0, 7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetclienti.setHorizontalHeaderItem(i, item)
        self.tableWidgetclienti.horizontalHeader().setVisible(True)
        self.tableWidgetclienti.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidgetclienti.verticalHeader().setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetclienti.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidgetclienti.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Cognome"))
        item = self.tableWidgetclienti.horizontalHeaderItem(2)
        item.setText(_translate("Form", "CF"))
        item = self.tableWidgetclienti.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Eta"))
        item = self.tableWidgetclienti.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Email"))
        item = self.tableWidgetclienti.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Sesso"))
        item = self.tableWidgetclienti.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Indirizzo"))

    def ricercaClienti(self):
        param = self.ricercaarchivioclienti.text()
        clientiRicercati = []
        if (param == ""):
            self.popolaClienti()
            return
        for element in data.listaClienti:
            if (param in element.nome or param in element.cognome):
                clientiRicercati.append(element)
        self.popolaRicercaClienti(clientiRicercati)

    def popolaClienti(self):
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, len(data.listaClienti)):
            for colonna in range(0, 7):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetclienti.setItem(riga, colonna, item)
                item = self.tableWidgetclienti.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("Form", str(data.listaClienti[riga].nome)))
                if (colonna == 1):
                    item.setText(_translate("Form", str(data.listaClienti[riga].cognome)))
                if (colonna == 2):
                    item.setText(_translate("Form", str(data.listaClienti[riga].cf)))
                if (colonna == 3):
                    item.setText(_translate("Form", str(data.listaClienti[riga].eta)))
                if (colonna == 4):
                    item.setText(_translate("Form", str(data.listaClienti[riga].email)))
                if (colonna == 5):
                    item.setText(_translate("Form", str(data.listaClienti[riga].sesso)))
                if (colonna == 6):
                    item.setText(_translate("Form", str(data.listaClienti[riga].indirizzo)))

    def popolaRicercaClienti(self, clientiRicercati):
        self.tableWidgetclienti.clear()
        self.creaArchivioClienti()
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, len(clientiRicercati)):
            for colonna in range(0, 7):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetclienti.setItem(riga, colonna, item)
                item = self.tableWidgetclienti.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("Form", str(clientiRicercati[riga].nome)))
                if (colonna == 1):
                    item.setText(_translate("Form", str(clientiRicercati[riga].cognome)))
                if (colonna == 2):
                    item.setText(_translate("Form", str(clientiRicercati[riga].cf)))
                if (colonna == 3):
                    item.setText(_translate("Form", str(clientiRicercati[riga].eta)))
                if (colonna == 4):
                    item.setText(_translate("Form", str(clientiRicercati[riga].email)))
                if (colonna == 5):
                    item.setText(_translate("Form", str(clientiRicercati[riga].sesso)))
                if (colonna == 6):
                    item.setText(_translate("Form", str(clientiRicercati[riga].indirizzo)))

    def creaArchivioEsiti(self):
        data.downloadAppuntamenti()
        data.downloadEsiti()
        self.tableWidgetesiti.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetesiti.setObjectName("tableWidget")
        self.tableWidgetesiti.setColumnCount(4)
        self.tableWidgetesiti.setRowCount(len(data.listaClienti))
        for i in range(0, 4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidgetesiti.setHorizontalHeaderItem(i, item)
        self.tableWidgetesiti.horizontalHeader().setVisible(True)
        self.tableWidgetesiti.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidgetesiti.verticalHeader().setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidgetesiti.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Id"))
        item = self.tableWidgetesiti.horizontalHeaderItem(1)
        item.setText(_translate("Form", "CF"))
        item = self.tableWidgetesiti.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Data"))
        item = self.tableWidgetesiti.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Esito"))

    def popolaEsiti(self):
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, len(data.listaEsiti)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetesiti.setItem(riga, colonna, item)
                item = self.tableWidgetesiti.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("Form", str(data.listaEsiti[riga].id_app)))
                if (colonna == 1):
                    item.setText(_translate("Form", str(data.listaEsiti[riga].cliente.cf)))
                if (colonna == 2):
                    item.setText(_translate("Form", str(data.listaEsiti[riga].data)))
                if (colonna == 3):
                    if data.listaEsiti[riga].esito:
                        item.setText(_translate("Form", "Positivo"))
                    else:
                        item.setText(_translate("Form", "Negativo"))

    def ricercaEsiti(self):
        param = self.ricercaappuntamento.text()
        esitiRicercati = []
        if (param == ""):
            self.popolaEsiti()
            return
        for element in data.listaEsiti:
            if (param in element.cliente.cf):
                esitiRicercati.append(element)
        self.popolaRicercaEsiti(esitiRicercati)

    def popolaRicercaEsiti(self, esitiRicercati):
        self.tableWidgetesiti.clear()
        self.creaArchivioEsiti()
        _translate = QtCore.QCoreApplication.translate
        for riga in range(0, len(esitiRicercati)):
            for colonna in range(0, 4):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetesiti.setItem(riga, colonna, item)
                item = self.tableWidgetesiti.item(riga, colonna)
                if (colonna == 0):
                    item.setText(_translate("Form", str(esitiRicercati[riga].id_app)))
                if (colonna == 1):
                    item.setText(_translate("Form", str(esitiRicercati[riga].cliente.cf)))
                if (colonna == 2):
                    item.setText(_translate("Form", str(esitiRicercati[riga].data)))
                if (colonna == 3):
                    if esitiRicercati[riga].esito:
                        item.setText(_translate("Form", "Positivo"))
                    else:
                        item.setText(_translate("Form", "Negativo"))





