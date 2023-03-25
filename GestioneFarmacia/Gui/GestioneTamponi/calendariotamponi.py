from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from GestioneFarmacia.GestioneSistema.data import data
from GestioneFarmacia.GestioneSistema.gestione import Gestore


gestore = Gestore()


class Ui_DialogCalendario(object):
    def setupUi(self, DialogCalendario):
        self.Frame = DialogCalendario

        DialogCalendario.setObjectName("DialogCalendario")
        DialogCalendario.resize(1225, 800)
        DialogCalendario.setStyleSheet("QWidget#DialogCalendario{\n"
"background-color:qlineargradient(spread:pad, x1:0.058, y1:0.136364, x2:1, y2:1, stop:0 rgba(0, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.calendario = QtWidgets.QCalendarWidget(DialogCalendario)
        self.calendario.selectionChanged.connect(self.updateTask)
        self.calendario.setGeometry(QtCore.QRect(40, 200, 471, 481))
        self.calendario.setObjectName("calendario")
        self.showdate = QtWidgets.QLabel(DialogCalendario)
        self.showdate.setGeometry(QtCore.QRect(260, 710, 91, 41))
        self.showdate.setText("")
        self.showdate.setObjectName("showdate")
        self.nuovoaappbtn = QtWidgets.QPushButton(DialogCalendario)
        self.nuovoaappbtn.setGeometry(QtCore.QRect(690, 490, 151, 41))
        self.nuovoaappbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nuovoaappbtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.nuovoaappbtn.setObjectName("nuovoaappbtn")
        self.AppuntamentiTable = QtWidgets.QTableWidget(DialogCalendario)
        self.AppuntamentiTable.setGeometry(QtCore.QRect(530, 230, 631, 251))
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
        self.homebtn = QtWidgets.QPushButton(DialogCalendario)
        self.homebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homebtn.setGeometry(QtCore.QRect(940, 680, 151, 41))
        self.homebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        #ok
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconahome.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon)
        self.homebtn.setIconSize(QtCore.QSize(40, 40))
        self.homebtn.setObjectName("homebtn")
        self.label = QtWidgets.QLabel(DialogCalendario)
        self.label.setGeometry(QtCore.QRect(60, 70, 991, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.eliminaappbtn = QtWidgets.QPushButton(DialogCalendario)
        self.eliminaappbtn.setGeometry(QtCore.QRect(860, 490, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.eliminaappbtn.setFont(font)
        self.eliminaappbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminaappbtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.eliminaappbtn.setObjectName("eliminaappbtn")


        self.homebtn.clicked.connect(self.returnToHome)
        self.nuovoaappbtn.clicked.connect(self.openRegistrazione)


        self.retranslateUi(DialogCalendario)
        QtCore.QMetaObject.connectSlotsByName(DialogCalendario)

    def retranslateUi(self, DialogCalendario):
        _translate = QtCore.QCoreApplication.translate
        DialogCalendario.setWindowTitle(_translate("DialogCalendario", "Dialog"))
        self.nuovoaappbtn.setText(_translate("DialogCalendario", "Nuovo Appuntamento"))
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
        self.homebtn.setText(_translate("DialogCalendario", "Home"))
        self.label.setText(_translate("DialogCalendario", "Appuntamenti tamponi"))
        self.eliminaappbtn.setText(_translate("DialogCalendario", "Elimina Appuntamento"))

    def returnToHome(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menu)
        self.menu.show()
        self.Frame.close()

    def updateTask(self):
        self.AppuntamentiTable.setRowCount(0)                       #fa partire da vuota la table
        data.downloadAppuntamenti()
        row = 0
        self.AppuntamentiTable.setRowCount(len(data.listaAppuntamenti))           #setto la quantità di righe della table come uguale alla lunghezza della lista di appuntamenti
        for appuntamento in data.listaAppuntamenti:
             if appuntamento.get_data().strftime("%y-%m-%d") == self.getgiorno():
                self.AppuntamentiTable.setItem(row, 0, QTableWidgetItem(str(appuntamento.get_idapp()))) #nella colonna id appuntamneto metto l'id dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 1, QTableWidgetItem(appuntamento.get_cff()))  #nella colonna cf metto il cf dell'appuntamento i esimo
                self.AppuntamentiTable.setItem(row, 2, QTableWidgetItem(appuntamento.get_data().strftime("%y-%m-%d")))
                if appuntamento.get_stato() == False:   #in base allo stato dell'appuntamento faccuio comparire la scritta CONCLUSO o NON CONCLUSO
                  self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Non concluso"))
                else:
                  self.AppuntamentiTable.setItem(row, 3, QTableWidgetItem("Concluso"))

                if appuntamento.get_tampone().get_esito() == False: #in base allo stato faccio comparire la scritta POSITIVO O NEGATIVO
                  self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("NEGATIVO"))
                else:
                  self.AppuntamentiTable.setItem(row, 4, QTableWidgetItem("POSITIVO"))
                row = row+1

    def getgiorno(self):  #prende la data selezionata sul calendario e la trasformo in una data Python convertita in stringa per usarla nei confronti
        giorno = self.calendario.selectedDate().toPyDate().strftime("%y-%m-%d")
        return giorno


    def openRegistrazione(self):
        from GestioneFarmacia.Gui.GestioneTamponi.registrazionecliente import Ui_Form
        self.registrazione = QtWidgets.QFrame()
        self.ui = Ui_Form()
        self.ui.setupUi(self.registrazione)
        self.registrazione.show()
        self.Frame.close()


