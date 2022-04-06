import sys
import time

from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, main_loop):
        QMainWindow.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.WindowTransparentForInput
        )
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(220, 32),
                QtWidgets.qApp.desktop().availableGeometry()
        ))

        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.setAttribute(QtCore.Qt.WA_NoChildEventsForParent, True)

        self.setWindowTitle("RuneAuras")

        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(600) # in milliseconds, so 5000 = 5 seconds
        self.timer.timeout.connect(main_loop)
        self.timer.start()

def make_window(cb):
    app = QApplication([])
    mywindow = MainWindow(cb)
    mywindow.show()
    app.exec_()