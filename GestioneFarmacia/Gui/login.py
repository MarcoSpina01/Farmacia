import sys
import wx
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from GestioneFarmacia.Gui.assistenza import Ui_Assistenza


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1122, 753)
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(-20, -30, 1161, 811))
        self.frame.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(211, 123, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(460, 110, 251, 51))
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
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(230, 200, 691, 421))
        self.frame_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(228, 255, 226, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(490, 260, 91, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.ErrorMessage = QtWidgets.QLabel(self.frame_2)
        self.ErrorMessage.setGeometry(QtCore.QRect(20, 270, 351, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorMessage.setFont(font)
        self.ErrorMessage.setStyleSheet("backgroundcolor:trasparent")
        self.ErrorMessage.setText("")
        self.ErrorMessage.setObjectName("ErrorMessage")
        self.Username = QtWidgets.QLineEdit(self.frame_2)
        self.Username.setGeometry(QtCore.QRect(130, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.frame_2)
        self.Password.setGeometry(QtCore.QRect(130, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Password.setFont(font)
        self.Password.setAccessibleName("")
        self.Password.setObjectName("Password")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Assistenzabtn = QtWidgets.QPushButton(self.frame)
        self.Assistenzabtn.setGeometry(QtCore.QRect(910, 690, 131, 41))
        self.Assistenzabtn.setObjectName("Assistenzabtn")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(660, 690, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.Autenticazione)
        self.Assistenzabtn.clicked.connect(self.openAssistenza)
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def openAssistenza(self):
        self.Assistenza = QtWidgets.QFrame()
        self.ui = Ui_Assistenza()
        self.ui.setupUi(self.Assistenza)
        self.Assistenza.show()
        self.frame.close()

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.label.setText(_translate("Login", "LOGIN"))
        self.pushButton.setText(_translate("Login", "Accedi"))
        self.label_2.setText(_translate("Login", "Username"))
        self.label_3.setText(_translate("Login", "Password"))
        self.Assistenzabtn.setText(_translate("Login", "Contatta assistenza"))
        self.label_4.setText(_translate("Login", "Password e/o Username smarriti?"))

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