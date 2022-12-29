from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(882, 583)
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(0, -20, 951, 631))
        self.frame.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(350, 50, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(180, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Username = QtWidgets.QLineEdit(self.frame)
        self.Username.setGeometry(QtCore.QRect(310, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.frame)
        self.Password.setGeometry(QtCore.QRect(310, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Password.setFont(font)
        self.Password.setAccessibleName("")
        self.Password.setObjectName("Password")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(640, 370, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.ErrorMessage = QtWidgets.QLabel(self.frame)
        self.ErrorMessage.setGeometry(QtCore.QRect(40, 350, 551, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorMessage.setFont(font)
        self.ErrorMessage.setText("")
        self.ErrorMessage.setObjectName("ErrorMessage")

        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.Autenticazione)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.label.setText(_translate("Login", "LOGIN"))
        self.label_2.setText(_translate("Login", "Username"))
        self.label_3.setText(_translate("Login", "Password"))
        self.pushButton.setText(_translate("Login", "Login"))


    def Autenticazione(self):
        username = self.Username.text()
        password = self.Password.text()
        if(username=="ciao"):
            if(password=="ciao"):
                self.ErrorMessage.setText("LOGIN CONFERMATO")
                        #collegare con la gui del menu
            else:
                self.ErrorMessage.setText("PASSWORD ERRATA")
        else:
            self.ErrorMessage.setText("USERNAME O PASSWORD ERRATI")