from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QSize, QTimer, QSize, QPoint
from PyQt5.QtGui import QPixmap, QColor, QPainter
from PyQt5 import QtWidgets

from PIL.ImageQt import ImageQt
from PIL import Image

from settings import get_user_buffs
from buffdetection import find_buff

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
        self.setStyleSheet('background-color: rgba(24, 23, 36, 0.63);')

        self.setWindowOpacity(70)

        self.setWindowTitle("RuneAuras")

        self.iconWidth = 64

        self.icon_init()

        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(600)
        self.timer.timeout.connect(self.icon_updates)
        self.timer.start()


    def icon_generate(self, icon, offset, active):
        label = QLabel(self)
        pixmap = QPixmap(icon).scaledToWidth(self.iconWidth)
        if not active:
            opacity_effect = QGraphicsOpacityEffect()
            opacity_effect.setOpacity(0.3)
            label.setGraphicsEffect(opacity_effect)

        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())

        label.move((self.iconWidth * offset) - (4 * offset), 0)

        return label


    def icon_init(self):
        self.buffs = get_user_buffs()

        for i, buff in enumerate(self.buffs):
            active = find_buff(0.9, buff["img"])
            buff["label"] = self.icon_generate(buff["img"], i, active)

            print(f"{buff['name']} active: {active}")

        self.setGeometry(2233, 734, self.iconWidth * len(self.buffs), self.iconWidth)
        self.show()


    def icon_update(self, label, icon, active):
        pixmap = QPixmap(icon).scaledToWidth(self.iconWidth)
        
        opacity_effect = QGraphicsOpacityEffect()
        if not active:
            opacity_effect.setOpacity(0.3)
        else:
            opacity_effect.setOpacity(1)
        label.setGraphicsEffect(opacity_effect)


        label.setPixmap(pixmap)


    def icon_updates(self):
        for buff in self.buffs:
            active = find_buff(0.9, buff["img"])
            print(f"{buff['name']} active: {active}")
            self.icon_update(buff["label"], buff["img"], active)


def make_window():
    app = QApplication([])
    mywindow = MainWindow()
    app.exec_()