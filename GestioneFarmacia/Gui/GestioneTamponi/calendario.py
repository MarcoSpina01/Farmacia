from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from GestioneFarmacia.GestioneSistema.Statistiche import Statistiche
from GestioneFarmacia.GestioneSistema.data import data
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneTamponi.Appuntamento import Appuntamento
from GestioneFarmacia.GestioneTamponi.ClassiTamponi import Tampone, Cliente

gestore = Gestore()

class Ui_DialogCalendario(object):

    def setupUi(self, DialogCalendario):
        self.Frame = DialogCalendario
        self.ricerca = ['', "Non Concluso", "Concluso"]
        self.registrazione = QtWidgets.QFrame()


        DialogCalendario.setObjectName("DialogCalendario")
        DialogCalendario.resize(1185, 800)
        DialogCalendario.setStyleSheet("QWidget#DialogCalendario{\n"
"background-color:qlineargradient(spread:pad, x1:0.058, y1:0.136364, x2:1, y2:1, stop:0 rgba(0, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.label = QtWidgets.QLabel(DialogCalendario)
        self.label.setGeometry(QtCore.QRect(110, 120, 971, 61))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(DialogCalendario)
        self.calendarWidget.selectionChanged.connect(self.popolaCalendario)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 210, 451, 471))
        self.calendarWidget.setObjectName("calendarWidget")
        self.nuovoappbtn = QtWidgets.QPushButton(DialogCalendario)
        self.nuovoappbtn.clicked.connect(self.openRegistrazione)
        self.nuovoappbtn.setGeometry(QtCore.QRect(520, 470, 161, 41))
        self.nuovoappbtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.nuovoappbtn.setObjectName("nuovoappbtn")
        self.AppuntamentiTable = QtWidgets.QTableWidget(DialogCalendario)
        self.AppuntamentiTable.setGeometry(QtCore.QRect(520, 210, 621, 231))
        self.AppuntamentiTable.setObjectName("AppuntamentiTable")
        self.AppuntamentiTable.setColumnCount(5)
        self.AppuntamentiTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.AppuntamentiTable.setHorizontalHeaderItem(4, item)
        self.ricercaappCombo = QtWidgets.QComboBox(DialogCalendario)
        self.ricercaappCombo.addItems(self.ricerca)
        self.ricercaappCombo.activated.connect(self.filtraAppuntamenti)
        self.ricercaappCombo.setGeometry(QtCore.QRect(530, 580, 161, 21))
        self.ricercaappCombo.setObjectName("ricercaappCombo")
        self.showdate_2 = QtWidgets.QLabel(DialogCalendario)
        self.showdate_2.setGeometry(QtCore.QRect(530, 540, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.showdate_2.setFont(font)
        self.showdate_2.setObjectName("showdate_2")
        self.chiudiappbtn = QtWidgets.QPushButton(DialogCalendario)
        self.chiudiappbtn.clicked.connect(self.chiudiAppuntamento)
        self.chiudiappbtn.setGeometry(QtCore.QRect(720, 470, 161, 41))
        self.chiudiappbtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.chiudiappbtn.setObjectName("chiudiappbtn")
        self.eliminaappbtn = QtWidgets.QPushButton(DialogCalendario)
        self.eliminaappbtn.setGeometry(QtCore.QRect(930, 470, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.eliminaappbtn.setFont(font)
        self.eliminaappbtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.eliminaappbtn.setObjectName("eliminaappbtn")
        self.homebtn = QtWidgets.QPushButton(DialogCalendario)
        self.homebtn.setGeometry(QtCore.QRect(900, 630, 151, 41))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")


        self.statistichebtn = QtWidgets.QPushButton(DialogCalendario)
        self.statistichebtn.setGeometry(QtCore.QRect(710, 640, 171, 41))
        self.statistichebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.statistichebtn.setObjectName("statistichebtn")


        self.homebtn.clicked.connect(self.returnToHome)
        self.nuovoappbtn.clicked.connect(self.openRegistrazione)
        self.eliminaappbtn.clicked.connect(self.eliminaAppuntamento)
        self.statistichebtn.clicked.connect(self.statisticheEsiti)

        self.retranslateUi(DialogCalendario)
        QtCore.QMetaObject.connectSlotsByName(DialogCalendario)

    def retranslateUi(self, DialogCalendario):
        _translate = QtCore.QCoreApplication.translate
        DialogCalendario.setWindowTitle(_translate("DialogCalendario", "Dialog"))
        self.label.setText(_translate("DialogCalendario", "GESTIONE DEGLI APPUNTAMENTI"))
        self.statistichebtn.setText(_translate("DialogCalendario", "Visualizza statistiche esiti"))
        self.nuovoappbtn.setText(_translate("DialogCalendario", "Nuovo Appuntamento"))
        item = self.AppuntamentiTable.horizontalHeaderItem(0)
        item.setText(_translate("DialogCalendario", "Codice"))
        item = self.AppuntamentiTable.horizontalHeaderItem(1)
        item.setText(_translate("DialogCalendario", "CF"))
        item = self.AppuntamentiTable.horizontalHeaderItem(2)
        item.setText(_translate("DialogCalendario", "Data"))
        item = self.AppuntamentiTable.horizontalHeaderItem(3)
        item.setText(_translate("DialogCalendario", "Stato"))
        item = self.AppuntamentiTable.horizontalHeaderItem(4)
        item.setText(_translate("DialogCalendario", "Esito"))
        self.showdate_2.setText(_translate("DialogCalendario", "Ricerca per:"))
        self.chiudiappbtn.setText(_translate("DialogCalendario", "Chiudi Appuntamento"))
        self.eliminaappbtn.setText(_translate("DialogCalendario", "Elimina Appuntamento"))
        self.homebtn.setText(_translate("DialogCalendario", "Home"))

    def openRegistrazione(self):
        from GestioneFarmacia.Gui.GestioneTamponi.registrazione import Ui_Registrazione
        self.registrazione = QtWidgets.QFrame()
        self.ui = Ui_Registrazione()
        self.ui.setupUi(self.registrazione)
        self.registrazione.show()

    def returnToHome(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    def getgiorno(self):  #prende la data selezionata sul calendario e la trasformo in una data Python convertita in stringa per usarla nei confronti
        giorno = self.calendarWidget.selectedDate().toPyDate().strftime("%y-%m-%d")
        return giorno

    def popolaCalendario(self):
        self.AppuntamentiTable.setRowCount(0)                       #fa partire da vuota la table
        data.downloadAppuntamenti()
        row = 0
        self.AppuntamentiTable.setRowCount(len(data.listaAppuntamenti))           #setto la quangtità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for appuntamento in data.listaAppuntamenti:

             if appuntamento.get_data().strftime("%y-%m-%d") == self.getgiorno():
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento.get_idapp()))) #nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento.get_cff()))  #nella colonna cf metto il cf dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(appuntamento.get_data().strftime("%y-%m-%d")))
                if appuntamento.get_stato() == False:   #in base allo stato dell'appuntamento faccuio comparire la scritta CONCLUSO o NON CONCLUSO
                  self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Non concluso"))
                  self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("Nessun Risultato"))
                else:
                  self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Concluso"))
                  if appuntamento.get_tampone().get_esito() == False: #in base allo stato faccio comparire la scritta POSITIVO O NEGATIVO
                      self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("NEGATIVO"))
                  else:
                      self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("POSITIVO"))
                row = row+1

    def filtraAppuntamenti(self):
        if self.ricercaappCombo.currentText() == "Non Concluso":
            self.visualizzaNonConclusi()
        elif self.ricercaappCombo.currentText() == "Concluso":
            self.visualizzaConclusi()
        elif self.ricercaappCombo.currentText() == '':
            self.AppuntamentiTable.setRowCount(0)

    def visualizzaNonConclusi(self):
        self.AppuntamentiTable.setRowCount(0)
        data.downloadAppuntamenti()
        row=0
        self.AppuntamentiTable.setRowCount(len(data.listaAppuntamenti))
        for appuntamento in data.listaAppuntamenti:
             if appuntamento.get_stato() == False:
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento.get_idapp()))) #nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento.get_cff()))  #nella colonna cf metto il cf dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(appuntamento.get_data().strftime("%y-%m-%d")))
                self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Non concluso"))
                self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("Nessun Risultato"))
                row = row+1

    def visualizzaConclusi(self):
        self.AppuntamentiTable.setRowCount(0)
        data.downloadAppuntamenti()
        row=0
        self.AppuntamentiTable.setRowCount(len(data.listaAppuntamenti))
        for appuntamento in data.listaAppuntamenti:
             if appuntamento.get_stato() == True:
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento.get_idapp()))) #nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento.get_cff()))  #nella colonna cf metto il cf dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(appuntamento.get_data().strftime("%y-%m-%d")))
                self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Concluso"))
                if appuntamento.get_tampone().get_esito() == False:
                    self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("NEGATIVO"))
                else:
                    self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("POSITIVO"))
                row = row+1

    def eliminaAppuntamento(self):
        from tkinter import messagebox
        cod = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 0)
        if cod is not None:
            data.downloadAppuntamenti()
            co = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 0).text()
            for a in data.listaAppuntamenti:

                if a.get_idapp() == int(co):
                    if a.get_stato() == False:
                        index = data.listaAppuntamenti.index(a)
                        data.listaAppuntamenti.pop(index)
                        data.uploadAppuntamenti()
                        messagebox.showinfo( "Avviso", "Appuntamento eliminato")
                        return

                    else:
                        messagebox.showinfo("Avviso", "Appuntamento già concluso, non si può eliminare!")
                        return

    def chiudiAppuntamento(self):
        import random
        from _datetime import datetime
        from tkinter import messagebox
        import random
        y = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 0)
        if y is not None:
            d = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 2).text()
            dataapp = datetime.strptime(d, '%y-%m-%d')
            if data.today >= dataapp:
                data.downloadAppuntamenti()
                y = self.AppuntamentiTable.item(self.AppuntamentiTable.currentRow(), 0).text()
                for a in data.listaAppuntamenti:
                    if a.get_idapp() == int(y):
                        if a.get_stato() == False:
                            a.set_isconcluso()
                            if random.randint(0, 1) == 1:
                                a.get_tampone().set_esito()
                                messagebox.showinfo("Avviso", "Tampone effettuato!")
                                data.uploadAppuntamenti()
                                return
                            else:
                                messagebox.showinfo("Avviso", "Tampone effettuato!")
                                data.uploadAppuntamenti()
                                return
                        else:
                            messagebox.showinfo("Avviso", "Il tampone è già stato somministrato!")
                            return
            else:
                messagebox.showinfo("Avviso", "Non puoi effettuare tamponi prima del giorno dell'appuntamento!")
                return
        else:
            messagebox.showinfo("Error", "Seleziona una riga non vuota")
            return


    def statisticheEsiti(self):
        self.st = Statistiche()
        self.st.plotPieEsiti()