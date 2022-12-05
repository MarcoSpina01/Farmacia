

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def Login(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(140, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEditUsername = QtWidgets.QLineEdit(Login)
        self.lineEditUsername.setGeometry(QtCore.QRect(120, 70, 113, 22))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(Login)
        self.lineEditPassword.setGeometry(QtCore.QRect(120, 110, 113, 22))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(40, 70, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 61, 16))
        self.label_2.setObjectName("label_2")

        self.pushButton.clicked(self.cliccaBottone)


        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.pushButton.setText(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Username"))
        self.label_2.setText(_translate("Login", "Password"))



    def cliccaBottone(self):
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()

        print(username + " " + password)
