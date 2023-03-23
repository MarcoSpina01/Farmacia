from PyQt5 import QtCore, QtGui, QtWidgets

from GestioneFarmacia.GestioneSistema.data import data
from GestioneFarmacia.GestioneSistema.gestione import Gestore

gestore = Gestore()

class Ui_Archivio(object):
    def setupUi(self, Form):
        self.Frame = Form
        Form.setObjectName("Form")
        Form.resize(827, 495)
        Form.setStyleSheet("")
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
        self.tableWidgetclienti.setColumnCount(0)
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
        self.Ricercaarticolobtn_2 = QtWidgets.QPushButton(Form)
        self.Ricercaarticolobtn_2.setGeometry(QtCore.QRect(610, 450, 91, 41))
        self.Ricercaarticolobtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ricercaarticolobtn_2.setStyleSheet("border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Ricercaarticolobtn_2.setIcon(icon1)
        self.Ricercaarticolobtn_2.setObjectName("Ricercaarticolobtn_2")
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
        self.ricercamagazzinotb_2 = QtWidgets.QLineEdit(Form)
        self.ricercamagazzinotb_2.setGeometry(QtCore.QRect(410, 460, 191, 21))
        self.ricercamagazzinotb_2.setObjectName("ricercamagazzinotb_2")
        self.tableWidgetesiti = QtWidgets.QTableWidget(Form)
        self.tableWidgetesiti.setGeometry(QtCore.QRect(410, 280, 391, 161))
        self.tableWidgetesiti.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetesiti.setObjectName("tableWidgetesiti")
        self.tableWidgetesiti.setColumnCount(0)
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


        self.homebtn.clicked.connect(self.returnToHome)
        self.creaArchivioOrdini()
        self.popolaOrdini()


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
        self.Ricercaarticolobtn_2.setText(_translate("Form", "  Ricerca"))
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




