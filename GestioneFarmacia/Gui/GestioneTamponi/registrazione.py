import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneTamponi.ClassiTamponi import Tampone, Cliente, Appuntamento
from GestioneFarmacia.Gui.GestioneTamponi.calendario import Ui_DialogCalendario
from GestioneFarmacia.GestioneSistema.data import data

gestore = Gestore()
class Ui_Registrazione(object):
    def setupUi(self, Form):
        self.Frame = Form
        self.tamponetipo = ['', "Molecolare", "Rapido"]
        self.registrazione = QtWidgets.QFrame()

        today = datetime.date.today()
        year = today.year
        self.giorni = []
        self.years = [str(year), str(year + 1)]
        for i in range(1, 32, 1):
            self.giorni.append(str(i))
        Form.setObjectName("Form")
        Form.resize(832, 729)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 200, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(110, 255, 146, 255));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(117, 255, 152, 255));")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(-6)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 260, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(119, 255, 153, 255));")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 320, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(130, 255, 161, 255));")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 380, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(148, 255, 175, 255));")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(60, 500, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(169, 255, 190, 255));")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(60, 560, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(169, 255, 190, 255));")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(60, 440, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(161, 255, 184, 255));")
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 210, 141, 31))
        self.lineEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit.setObjectName("lineEdit")
        self.cvle = QtWidgets.QLineEdit(Form)
        self.cvle.setGeometry(QtCore.QRect(240, 510, 141, 31))
        self.cvle.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.cvle.setObjectName("cvle")
        self.emaille = QtWidgets.QLineEdit(Form)
        self.emaille.setGeometry(QtCore.QRect(240, 450, 141, 31))
        self.emaille.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.emaille.setObjectName("emaille")
        self.indirizzole = QtWidgets.QLineEdit(Form)
        self.indirizzole.setGeometry(QtCore.QRect(240, 390, 141, 31))
        self.indirizzole.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.indirizzole.setObjectName("indirizzole")
        self.etale = QtWidgets.QLineEdit(Form)
        self.etale.setGeometry(QtCore.QRect(240, 330, 141, 31))
        self.etale.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.etale.setObjectName("etale")
        self.cognomele = QtWidgets.QLineEdit(Form)
        self.cognomele.setGeometry(QtCore.QRect(240, 270, 141, 31))
        self.cognomele.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.cognomele.setObjectName("cognomele")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(660, 620, 61, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconaindietro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.registrazione = QtWidgets.QPushButton(Form)
        self.registrazione.setGeometry(QtCore.QRect(480, 620, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.registrazione.setFont(font)
        self.registrazione.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registrazione.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconaregistrazione.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.registrazione.setIcon(icon1)
        self.registrazione.setIconSize(QtCore.QSize(45, 45))
        self.registrazione.setObjectName("registrazione")
        self.sessoCombo = QtWidgets.QComboBox(Form)
        self.sessoCombo.setGeometry(QtCore.QRect(240, 570, 141, 31))
        self.sessoCombo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 255));")
        self.sessoCombo.setObjectName("sessoCombo")
        self.sessoCombo.addItem("")
        self.sessoCombo.addItem("")
        self.sessoCombo.addItem("")
        self.sessoCombo.addItem("")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(60, 620, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(169, 255, 190, 255));")
        self.label_9.setObjectName("label_9")
        self.tamponeCombo = QtWidgets.QComboBox(Form)
        self.tamponeCombo.addItems(self.tamponetipo)
        self.tamponeCombo.setGeometry(QtCore.QRect(240, 630, 141, 31))
        self.tamponeCombo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 255));")
        self.tamponeCombo.setObjectName("tamponeCombo")
        self.tamponeCombo.addItem("")
        self.tamponeCombo.addItem("")
        self.tamponeCombo.addItem("")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(730, 220, 71, 41))
        self.label_10.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(197, 255, 211, 255));")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(600, 220, 71, 41))
        self.label_11.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(183, 255, 201, 255));")
        self.label_11.setObjectName("label_11")
        self.meseCombo = QtWidgets.QComboBox(Form)
        self.meseCombo.activated.connect(self.popolaCombo)
        self.meseCombo.setGeometry(QtCore.QRect(550, 260, 141, 31))
        self.meseCombo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 255));")
        self.meseCombo.setObjectName("meseCombo")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.meseCombo.addItem("")
        self.giornoCombo = QtWidgets.QComboBox(Form)
        self.giornoCombo.setGeometry(QtCore.QRect(720, 260, 91, 31))
        self.giornoCombo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 255));")
        self.giornoCombo.setObjectName("giornoCombo")
        self.annoCombo = QtWidgets.QComboBox(Form)
        self.annoCombo.addItems(self.years)
        self.annoCombo.setGeometry(QtCore.QRect(430, 260, 91, 31))
        self.annoCombo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 255));")
        self.annoCombo.setObjectName("annoCombo")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(450, 220, 71, 41))
        self.label_12.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(162, 255, 185, 255));")
        self.label_12.setObjectName("label_12")


        self.registrazione.clicked.connect(self.passaDati)

        self.pushButton.clicked.connect(self.returnToCalendario)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nome"))
        self.label_2.setText(_translate("Form", "Registrazione"))
        self.label_3.setText(_translate("Form", "Cognome"))
        self.label_4.setText(_translate("Form", "Età"))
        self.label_5.setText(_translate("Form", "Indirizzo"))
        self.label_6.setText(_translate("Form", "Codice Fiscale"))
        self.label_7.setText(_translate("Form", "Sesso"))
        self.label_8.setText(_translate("Form", "Email"))
        self.registrazione.setText(_translate("Form", " Registrati"))
        self.sessoCombo.setItemText(0, _translate("Form", " "))
        self.sessoCombo.setItemText(1, _translate("Form", "Maschio"))
        self.sessoCombo.setItemText(2, _translate("Form", "Femmina"))
        self.sessoCombo.setItemText(3, _translate("Form", "Altro"))
        self.label_9.setText(_translate("Form", "Tipo di Tampone"))
        self.tamponeCombo.setItemText(0, _translate("Form", " "))
        self.tamponeCombo.setItemText(1, _translate("Form", "Molecolare"))
        self.tamponeCombo.setItemText(2, _translate("Form", "Rapido"))
        self.label_10.setText(_translate("Form", "Giorno"))
        self.label_11.setText(_translate("Form", "Mese"))
        self.meseCombo.setItemText(0, _translate("Form", "01"))
        self.meseCombo.setItemText(1, _translate("Form", "02"))
        self.meseCombo.setItemText(2, _translate("Form", "03"))
        self.meseCombo.setItemText(3, _translate("Form", "04"))
        self.meseCombo.setItemText(4, _translate("Form", "05"))
        self.meseCombo.setItemText(5, _translate("Form", "06"))
        self.meseCombo.setItemText(6, _translate("Form", "07"))
        self.meseCombo.setItemText(7, _translate("Form", "08"))
        self.meseCombo.setItemText(8, _translate("Form", "09"))
        self.meseCombo.setItemText(9, _translate("Form", "10"))
        self.meseCombo.setItemText(10, _translate("Form", "11"))
        self.meseCombo.setItemText(11, _translate("Form", "12"))
        self.label_12.setText(_translate("Form", "Anno"))

    def returnToCalendario(self):
        self.Frame.close()

    def svutaForm(self):
        self.lineEdit.clear()
        self.cognomele.clear()
        self.cvle.clear()
        self.giornoCombo.clear()
        self.etale.clear()
        self.emaille.clear()
        self.indirizzole.clear()

    def passaDati(self):
        from tkinter import messagebox
        if self.lineEdit.text() != '' and self.cognomele.text() != '' and self.cvle.text() != '' and \
        self.giornoCombo.currentText() != '' and self.tamponeCombo.currentText() != ' ' and self.etale.text() != ''\
        and self.emaille.text() != '' and self.sessoCombo.currentText() != ' ' and self.indirizzole.text() != '':
            today = datetime.date.today()
            a = int(self.annoCombo.currentText())
            m = int(self.meseCombo.currentText())
            g = int(self.giornoCombo.currentText())
            giornoo = datetime.date(a, m, g)
            if giornoo >= today:
                data.downloadAppuntamenti()
                nome = self.lineEdit.text()
                cognome = self.cognomele.text()
                cf = self.cvle.text()
                eta = self.etale.text()
                mail = self.emaille.text()
                indirizzo = self.indirizzole.text()
                sesso = self.sessoCombo.currentText()

                tipo = self.tamponeCombo.currentText()
                tampone = Tampone(tipo)
                cliente = Cliente(nome, cognome, cf, eta, mail, sesso, indirizzo)
                newid = data.listaAppuntamenti[len(data.listaAppuntamenti)-1].get_idapp()+1
                appuntamento = Appuntamento(cliente, tampone, giornoo)
                appuntamento.set_idapp(newid)
                data.listaAppuntamenti.append(appuntamento)
                data.uploadAppuntamenti()
                messagebox.showinfo("Avviso", "Appuntamento aggiunto!")
                self.returnToCalendario()
            else:
                messagebox.showinfo("Error", "La data inserita deve essere sucessiva o uguale a quella odierna")
                return
        else:
            messagebox.showinfo("Error", "Riempi tutti i campi")
            return

    #Metodo che permette di popolare le combobox della scelta della data
    #Il numero di giorni disponibili alla scelta varia dinamicamente in base al mese selezionato
    def popolaCombo(self):
        self.giornoCombo.clear()
        temp = []
        if self.meseCombo.currentText() == "01":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "02":
           for i in range(0, 27, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "03":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "04":
           for i in range(0, 30, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "05":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "06":
           for i in range(0, 30, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "07":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "08":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "09":
           for i in range(0, 30, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "10":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "11":
           for i in range(0, 30, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)

        elif self.meseCombo.currentText() == "12":
           for i in range(0, 31, 1):
                temp.append(self.giorni[i])
           self.giornoCombo.addItems(temp)
