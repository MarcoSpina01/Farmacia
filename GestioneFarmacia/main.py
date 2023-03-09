import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from GestioneFarmacia.GestioneVendite.Farmaco import Farmaco
from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto
from GestioneFarmacia.Gui.GestioneLogin.login import Ui_Login

if __name__ == "__main__":

    app = QApplication([])
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())