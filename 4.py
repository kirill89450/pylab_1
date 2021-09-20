from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox

import sys

lang = {'A': '.-', 'B': '-...',

        'C': '-.-.', 'D': '-..', 'E': '.',

        'F': '..-.', 'G': '--.', 'H': '....',

        'I': '..', 'J': '.---', 'K': '-.-',

        'L': '.-..', 'M': '--', 'N': '-.',

        'O': '---', 'P': '.--.', 'Q': '--.-',

        'R': '.-.', 'S': '...', 'T': '-',

        'U': '..-', 'V': '...-', 'W': '.--',

        'X': '-..-', 'Y': '-.--', 'Z': '--..'}
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Lab1")
        self.setGeometry(400, 200, 800, 600)





        x = 0
        y = 200

        for i in range(65,91):  # от 50 до 700
            x += 50
            if i ==78 :
                y += 70
                x = 50

            self.button = QtWidgets.QPushButton(self)
            self.button.setGeometry(x, y, 50, 50)
            self.button.setText(chr(i))
            self.button.clicked.connect(self.press_btn)

        self.text = QtWidgets.QLabel(self)
        self.text.setText("")
        self.text.setGeometry(50, 350, 650, 30)
        self.text.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')


        self.show()

    def press_btn(self):
        self.text.setText(self.text.text()+lang[self.sender().text()])






def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
