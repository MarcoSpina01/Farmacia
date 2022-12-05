import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtWidgets

from GestioneFarmacia.Grafica.login import Ui_Login

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi()
    Login.show()
    sys.exit(app.exec_())
