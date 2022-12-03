import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    textlable = QLabel(widget)
    textlable.setText("ciao")
    widget.setGeometry(100,100,400,200)
    widget.setWindowTitle("Gesione Farmacia")
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
