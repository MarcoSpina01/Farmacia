from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneTamponi.ClassiTamponi import Cliente, Tampone, Appuntamento
import random

gestore = Gestore()
cliente = Cliente()
tampone = Tampone()
appuntamento = Appuntamento()

class Ui_Form(object):
    def setupUi(self, Form):
        self.Frame = Form
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
        self.registrazionebtn = QtWidgets.QPushButton(Form)
        self.registrazionebtn.setGeometry(QtCore.QRect(480, 620, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.registrazionebtn.setFont(font)
        self.registrazionebtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registrazionebtn.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth()+"loghi-icone/iconaregistrazione.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.registrazionebtn.setIcon(icon1)
        self.registrazionebtn.setIconSize(QtCore.QSize(45, 45))
        self.registrazionebtn.setObjectName("registrazionebtn")
        self.sessocb = QtWidgets.QComboBox(Form)
        self.sessocb.setGeometry(QtCore.QRect(240, 570, 141, 31))
        self.sessocb.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 255));")
        self.sessocb.setObjectName("sessocb")
        self.sessocb.addItem("")
        self.sessocb.addItem("")
        self.sessocb.addItem("")
        self.sessocb.addItem("")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(60, 620, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(169, 255, 190, 255));")
        self.label_9.setObjectName("label_9")
        self.sessocb_2 = QtWidgets.QComboBox(Form)
        self.sessocb_2.setGeometry(QtCore.QRect(240, 630, 141, 31))
        self.sessocb_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 255));")
        self.sessocb_2.setObjectName("sessocb_2")
        self.sessocb_2.addItem("")
        self.sessocb_2.addItem("")
        self.sessocb_2.addItem("")
        self.datalabel = QtWidgets.QLabel(Form)
        self.datalabel.setGeometry(QtCore.QRect(450, 130, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.datalabel.setFont(font)
        self.datalabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(156, 255, 181, 255));")
        self.datalabel.setAlignment(QtCore.Qt.AlignCenter)
        self.datalabel.setObjectName("datalabel")


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
        self.registrazionebtn.setText(_translate("Form", " Registrati"))
        self.sessocb.setItemText(0, _translate("Form", "..."))
        self.sessocb.setItemText(1, _translate("Form", "Maschio"))
        self.sessocb.setItemText(2, _translate("Form", "Femmina"))
        self.sessocb.setItemText(3, _translate("Form", "Altro"))
        self.label_9.setText(_translate("Form", "Tipo di Tampone"))
        self.sessocb_2.setItemText(0, _translate("Form", "..."))
        self.sessocb_2.setItemText(1, _translate("Form", "Molecolare"))
        self.sessocb_2.setItemText(2, _translate("Form", "Rapido"))
        self.datalabel.setText(_translate("Form", ""))

    def returnToCalendario(self):
        from GestioneFarmacia.Gui.GestioneTamponi.calendariotamponi import Ui_DialogCalendario
        self.calendario = QtWidgets.QFrame()
        self.ui = Ui_DialogCalendario()
        self.ui.setupUi(self.calendario)
        self.calendario.show()
        self.Frame.close()

    def prendiDatiCliente(self):
        self.cliente.nome = self.lineEdit.text()
        self.cliente.cognome = self.cognomele.text()
        self.cliente.eta = self.etale.text()
        self.cliente.indirizzo = self.indirizzole.text()
        self.cliente.email = self.emaille.text()
        self.cliente.cf = self.cvle.text()
        self.cliente.sesso = self.sessocb.currentText()

    def prendiTampone(self):
        self.tampone.tipo = self.sessocb_2.currentText()
        self.tampone.prezzo = 10
        a = random.randint(1, 2)
        if a == 1:
            self.tampone.esito = False
        else:
            self.tampone.esito = True

    def associaAppuntamento(self):
        self.appuntamento.cliente = self.cliente
        self.appuntamento.tampone = self.tampone

