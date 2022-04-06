from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import Qt, QSize, QTimer, QSize
from PyQt5.QtGui import QPixmap, QColor
from PyQt5 import QtWidgets

from PIL.ImageQt import ImageQt
from PIL import Image

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.X11BypassWindowManagerHint |
            Qt.WindowTransparentForInput
        )
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                Qt.LeftToRight, 
                Qt.AlignCenter,
                QSize(220, 32),
                QtWidgets.qApp.desktop().availableGeometry()
        ))

        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setAttribute(Qt.WA_NoChildEventsForParent, True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: #3a3b3c;')

        self.setWindowTitle("RuneAuras")

        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(600)
        self.timer.timeout.connect(self.main_loop)
        self.timer.start()

    def main_loop(self):
        label1 = QLabel(self)
        pixmap1 = QPixmap("img/turmoil.png").scaledToWidth(64)
        label1.setPixmap(pixmap1)
        label1.resize(pixmap1.width(), pixmap1.height())

        label2 = QLabel(self)
        pixmap2 = QPixmap("img/grimoire.png").scaledToWidth(64)
        label2.setPixmap(pixmap2)
        label2.resize(pixmap2.width(), pixmap2.height())
        label2.move(64,0)

        self.setGeometry(1600, 684, pixmap1.width()*2, pixmap1.height())
        self.show()


def make_window(cb):
    app = QApplication([])
    mywindow = MainWindow()
    app.exec_()