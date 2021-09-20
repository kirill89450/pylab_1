from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Lab1")
        self.setGeometry(400, 200, 800, 600)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(100, 300)
        self.btn1.setText("1")
        self.box1 = QCheckBox("1", self)
        self.box1.move(145, 350)
        self.box1.stateChanged.connect(self.press_btn)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(200, 300)
        self.btn2.setText("2")

        self.box2 = QCheckBox("2", self)
        self.box2.move(245, 350)
        self.box2.stateChanged.connect(self.press_btn)

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.move(300, 300)
        self.btn3.setText("3")


        self.box3 = QCheckBox("3", self)
        self.box3.move(345, 350)
        self.box3.stateChanged.connect(self.press_btn)

        self.show()

    def press_btn(self):
        if self.sender() == self.box1:
            if self.box1.isChecked():
                self.btn1.hide()
            else:
                self.btn1.show()
        if self.sender() == self.box2:
            if self.box2.isChecked():
                self.btn2.hide()
            else:
                self.btn2.show()
        if self.sender() == self.box3:
            if self.box3.isChecked():
                self.btn3.hide()
            else:
                self.btn3.show()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
