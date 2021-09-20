from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Lab1")
        self.setGeometry(400, 200, 800, 600)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(350, 300)
        self.btn.setText("-->")
        self.btn.clicked.connect(self.press_btn)

        self.lebel_r = QtWidgets.QLineEdit(self)
        self.lebel_r.setGeometry(500, 300, 100, 20)

        self.lebel_l = QtWidgets.QLineEdit(self)
        self.lebel_l.setGeometry(200, 300, 100, 20)

        self.show()

    def press_btn(self):
        if self.btn.text() ==  "-->":
            self.btn.setText("<--")
            self.lebel_r.setText(self.lebel_l.text())
            self.lebel_l.setText("")

        else:
            self.lebel_l.setText(self.lebel_r.text())
            self.lebel_r.setText("")
            self.btn.setText("-->")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
