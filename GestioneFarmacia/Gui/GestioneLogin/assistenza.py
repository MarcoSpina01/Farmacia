
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Assistenza(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1121, 752)
        Form.setStyleSheet("background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(144, 115, 145, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(100, 70, 911, 601))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(226, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(300, 10, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 170, 611, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 240, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tornaloginbtn = QtWidgets.QPushButton(self.frame)
        self.tornaloginbtn.setGeometry(QtCore.QRect(690, 450, 93, 28))
        self.tornaloginbtn.setObjectName("tornaloginbtn")
        self.tornaloginbtn.clicked.connect(self.returnLogin)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Assistenza farmacia:"))
        self.label_2.setText(_translate("Form", "Per eventuali domande, dubbi o errori contattaci alla mail:"))
        self.label_3.setText(_translate("Form", "farmaciacasereccia@gmail.com"))
        self.tornaloginbtn.setText(_translate("Form", "Torna al Login"))

    def returnLogin(self):
        from GestioneFarmacia.Gui.GestioneLogin.login import Ui_Login
        self.login = QtWidgets.QFrame()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login)
        self.login.show()
        self.frame.close()