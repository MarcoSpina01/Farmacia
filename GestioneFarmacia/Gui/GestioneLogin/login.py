from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from GestioneFarmacia.GestioneSistema.gestione import Gestore

# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()
class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(930, 686)
        self.Frame = Login
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(-20, -20, 1331, 931))
        self.frame.setStyleSheet("background-image: url("+gestore.returnPth()+"loghi-icone/logofarmacia.PNG)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 100, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Assistenzabtn = QtWidgets.QPushButton(self.frame)
        self.Assistenzabtn.setGeometry(QtCore.QRect(800, 500, 131, 41))
        self.Assistenzabtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Assistenzabtn.setObjectName("Assistenzabtn")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(570, 500, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 620, 91, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.visualizzapwbtn = QtWidgets.QCheckBox(self.frame)
        self.visualizzapwbtn.setGeometry(QtCore.QRect(230, 610, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.visualizzapwbtn.setFont(font)
        self.visualizzapwbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualizzapwbtn.setObjectName("visualizzapwbtn")
        self.Username = QtWidgets.QLineEdit(self.frame)
        self.Username.setGeometry(QtCore.QRect(200, 490, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 490, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(90, 540, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Password = QtWidgets.QLineEdit(self.frame)
        self.Password.setGeometry(QtCore.QRect(200, 540, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Password.setFont(font)
        self.Password.setAccessibleName("")
        self.Password.setObjectName("Password")
        self.ErrorMessage = QtWidgets.QLabel(self.frame)
        self.ErrorMessage.setGeometry(QtCore.QRect(570, 120, 351, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorMessage.setFont(font)
        self.ErrorMessage.setStyleSheet("backgroundcolor:trasparent")
        self.ErrorMessage.setText("")
        self.ErrorMessage.setObjectName("ErrorMessage")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)

        # bottone associato alla validazione di username e password
        self.pushButton.clicked.connect(self.autenticazione)
        # bottone associato all'apertura della gui di assistenza
        self.Assistenzabtn.clicked.connect(self.openAssistenza)
        # bottone associato al click della checkbox per la visualizzazione della password
        self.visualizzapwbtn.clicked.connect(self.gestionePassword)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.label.setText(_translate("Login", "LOGIN"))
        self.Assistenzabtn.setText(_translate("Login", "Contatta assistenza"))
        self.label_4.setText(_translate("Login", "Password e/o Username smarriti?"))
        self.pushButton.setText(_translate("Login", "Accedi"))
        self.visualizzapwbtn.setText(_translate("Login", "Visualizza Password"))
        self.label_2.setText(_translate("Login", "Username"))
        self.label_3.setText(_translate("Login", "Password"))

    # metodo che permette di ottenere e controllare username e password dalle lineedit
    # in caso di inserimento corretto delle credenziali verrà aperto il menu principale
    def autenticazione(self):
        username = self.Username.text()
        password = self.Password.text()
        if (username == "username"):
            if (password == "password"):
                self.openMenu()
            else:
                self.ErrorMessage.setText("PASSWORD ERRATA")
        else:
            self.ErrorMessage.setText("USERNAME O PASSWORD ERRATI")

    # metodo per l'apertura dell'assistenza
    def openAssistenza(self):
        from GestioneFarmacia.Gui.GestioneLogin.assistenza import Ui_Assistenza
        self.Assistenza = QtWidgets.QFrame()
        self.ui = Ui_Assistenza()
        self.ui.setupUi(self.Assistenza)
        self.Assistenza.show()
        self.Frame.close()

    # metodo che controlla la checkbox, se è selezionata fa vedere la password, in caso contario la nasconde
    def gestionePassword(self):
        if (self.visualizzapwbtn.isChecked()):
            self.Password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.Password.setEchoMode(QtWidgets.QLineEdit.Password)

    # metodo per l'apertura del menu
    def openMenu(self):
        from GestioneFarmacia.Gui.GestioneLogin.menu import Ui_Menu
        self.Menu = QtWidgets.QFrame()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.Menu)
        self.Menu.show()
        self.Frame.close()
