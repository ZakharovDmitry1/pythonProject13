import difflib
import sys
from random import choice, randint
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPixmap, QPalette
from PyQt5.QtWidgets import *
from PIL import Image, ImageDraw


def similarity(str1, str2):
    return difflib.SequenceMatcher(None, str1.lower(), str2.lower()).ratio() * 100


class MyWidget(QMainWindow, QSlider):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.run()

    def run(self):
        self.btn.clicked.connect(self.hello)

    def hello(self) -> None:
        text1, text2 = self.edit1.toPlainText().lower(), self.edit2.toPlainText().lower()
        text1 = text1.replace('  ', ' ')
        text2 = text2.replace('  ', ' ')
        sredn = (len(text1) + len(text2)) / 2
        count = 0
        for i in range(min(len(text1), len(text2))):
            if text1[i] == text2[i]:
                count += 1
        try:
            res = count * 10000 // sredn / 100
        except Exception:
            res = 100
        res = similarity(text1, text2) * 100 // 100
        print(self.box.value())

        if self.box.value() > res:
            self.label.setText(f"Текст похож на {res}%")
            self.label.setStyleSheet('QLabel {background-color: green;}')
        else:
            self.label.setText(f"Текст похож на {res}%")
            self.label.setStyleSheet('QLabel {background-color: red;}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
