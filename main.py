import os
import sys
import random
import design

from PyQt5 import QtCore, QtWidgets, QtGui


class PhotoApp(QtWidgets.QMainWindow, design.MainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(lambda: self.browse_folder())
        self.timer.start()

    def browse_folder(self):
        directory = "path"

        file_list = []
        if directory:
            for file_name in os.listdir(directory):
                file_list.append(file_name)

            self.frame_01.setPixmap(QtGui.QPixmap(f'{directory}/{random.choice(file_list)}'))
            self.frame_02.setPixmap(QtGui.QPixmap(f'{directory}/{random.choice(file_list)}'))
            self.frame_03.setPixmap(QtGui.QPixmap(f'{directory}/{random.choice(file_list)}'))
            self.frame_04.setPixmap(QtGui.QPixmap(f'{directory}/{random.choice(file_list)}'))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PhotoApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
