import os
import random
import sys

import yadisk
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QDesktopWidget
from dotenv import load_dotenv

import gui

load_dotenv()
client = yadisk.Client(token=os.getenv("TOKEN"))
with client:
    file_list = []
    ext = [".jpg", ".jpeg", ".png", ".bmp"]

    for file in os.listdir(f"{os.getcwd()}/{os.getenv("DST")}"):
        if file.lower().endswith(tuple(ext)) and '~$' not in file:
            file_list.append(file)

    for file in list(client.listdir(os.getenv("SRC"))):
        if file.name not in file_list:
            client.download(
                f"{os.getenv("SRC")}/{file.name}", f"{os.getcwd()}/{os.getenv("DST")}/{file.name}")
            print(file.name)


def get_photo():
    return f"{os.getcwd()}/{os.getenv("DST")}/{random.choice(file_list)}"


def get_interval():
    return random.randint(3000, 9000)


class PhotoApp(QtWidgets.QMainWindow, gui.MainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)

        self.timer_1 = QtCore.QTimer()
        self.timer_1.setInterval(get_interval())
        self.timer_1.timeout.connect(lambda: self.frame_01.setPixmap(QtGui.QPixmap(get_photo())))
        self.timer_1.start()

        self.timer_2 = QtCore.QTimer()
        self.timer_2.setInterval(get_interval())
        self.timer_2.timeout.connect(lambda: self.frame_02.setPixmap(QtGui.QPixmap(get_photo())))
        self.timer_2.start()

        self.timer_3 = QtCore.QTimer()
        self.timer_3.setInterval(get_interval())
        self.timer_3.timeout.connect(lambda: self.frame_03.setPixmap(QtGui.QPixmap(get_photo())))
        self.timer_3.start()

        self.timer_4 = QtCore.QTimer()
        self.timer_4.setInterval(get_interval())
        self.timer_4.timeout.connect(lambda: self.frame_04.setPixmap(QtGui.QPixmap(get_photo())))
        self.timer_4.start()

        self.timer_5 = QtCore.QTimer()
        self.timer_5.setInterval(get_interval())
        self.timer_5.timeout.connect(lambda: self.frame_05.setPixmap(QtGui.QPixmap(get_photo())))
        self.timer_5.start()

        self.timer_6 = QtCore.QTimer()
        self.timer_6.setInterval(get_interval())
        self.timer_6.timeout.connect(lambda: self.frame_06.setPixmap(QtGui.QPixmap(get_photo())))
        self.timer_6.start()


def create_palette():
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(50, 50, 50))
    palette.setColor(QPalette.WindowText, Qt.darkGray)
    palette.setColor(QPalette.Base, QColor(30, 30, 30))
    palette.setColor(QPalette.AlternateBase, QColor(50, 50, 50))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(50, 50, 50))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(40, 130, 220))
    palette.setColor(QPalette.Highlight, QColor(40, 130, 220))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    return palette


stylesheet = """
    QMainWindow {
        background-image: url("C:/git/screen_divider/back_logo.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setPalette(create_palette())
    app.setStyleSheet(stylesheet)
    window = PhotoApp()
    display_monitor = 1
    monitor = QDesktopWidget().screenGeometry(display_monitor)
    window.move(monitor.left(), monitor.top())
    window.showFullScreen()  # window.show()
    app.exec_()


if __name__ == '__main__':
    main()
