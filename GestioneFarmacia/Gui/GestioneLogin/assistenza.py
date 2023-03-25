from PyQt5 import QtCore, QtGui, QtWidgets
from GestioneFarmacia.GestioneSistema.gestione import Gestore

# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()

class Ui_Assistenza(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(978, 705)
        Form.setStyleSheet("")
        self.Frame = Form
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(110, 140, 771, 421))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(190, 220, 190, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 70, 361, 101))
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
        self.tornaloginbtn.setGeometry(QtCore.QRect(560, 300, 93, 28))
        self.tornaloginbtn.setObjectName("tornaloginbtn")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(-10, -10, 1531, 941))
        self.frame_2.setStyleSheet("background-image: url("+gestore.returnPth()+"loghi-icone/logofarmacia.PNG)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()
        # evento click del bottone di ritorno al login
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

# metodo di ritorno alla gui del login
    def returnLogin(self):
        from GestioneFarmacia.Gui.GestioneLogin.login import Ui_Login
        self.login = QtWidgets.QFrame()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login)
        self.login.show()
        self.Frame.close()

