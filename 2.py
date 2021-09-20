from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Lab1")
        self.setGeometry(400, 200, 800, 600)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(350, 300)
        self.btn.setText("Вычислить")
        self.btn.clicked.connect(self.press_btn)

        self.lebel_r = QtWidgets.QLineEdit(self)
        self.lebel_r.setGeometry(350, 275, 100, 20)

        self.text=QtWidgets.QLabel(self)
        self.text.setText("Введите выражение")
        self.text.setGeometry(350, 250,110,20)

        self.text1 = QtWidgets.QLabel(self)
        self.text1.setText("Ваш ответ")
        self.text1.setGeometry(475, 250, 110, 20)

        self.text2 = QtWidgets.QLabel(self)
        self.text2.setText("0")
        self.text2.setGeometry(475, 275, 110, 20)

        self.show()
    def press_btn(self):
        self.text2.setText(str(eval(self.lebel_r.text())))





def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
