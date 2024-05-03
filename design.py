from PyQt5 import QtCore, QtWidgets


class MainWindow(object):
    def __init__(self):
        self.grid_layout = None
        self.central_widget = None
        self.frame_01 = None
        self.frame_02 = None
        self.frame_03 = None
        self.frame_04 = None

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1920, 1080)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("gridLayout")

        self.frame_01 = QtWidgets.QLabel(self.central_widget)
        self.frame_01.setMinimumSize(QtCore.QSize(960, 540))
        self.frame_01.setMaximumSize(QtCore.QSize(1920, 1080))
        self.frame_01.setAutoFillBackground(True)
        self.frame_01.setScaledContents(True)
        self.frame_01.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_01.setObjectName("frame_01")
        self.grid_layout.addWidget(self.frame_01, 0, 0, 1, 1)

        self.frame_02 = QtWidgets.QLabel(self.central_widget)
        self.frame_02.setMinimumSize(QtCore.QSize(960, 540))
        self.frame_02.setMaximumSize(QtCore.QSize(1920, 1080))
        self.frame_02.setAutoFillBackground(True)
        self.frame_02.setScaledContents(True)
        self.frame_02.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_02.setObjectName("frame_02")
        self.grid_layout.addWidget(self.frame_02, 0, 1, 1, 1)

        self.frame_03 = QtWidgets.QLabel(self.central_widget)
        self.frame_03.setMinimumSize(QtCore.QSize(960, 540))
        self.frame_03.setMaximumSize(QtCore.QSize(1920, 1080))
        self.frame_03.setAutoFillBackground(True)
        self.frame_03.setScaledContents(True)
        self.frame_03.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_03.setObjectName("frame_03")
        self.grid_layout.addWidget(self.frame_03, 1, 0, 1, 1)

        self.frame_04 = QtWidgets.QLabel(self.central_widget)
        self.frame_04.setMinimumSize(QtCore.QSize(960, 540))
        self.frame_04.setMaximumSize(QtCore.QSize(1920, 1080))
        self.frame_04.setAutoFillBackground(True)
        self.frame_04.setScaledContents(True)
        self.frame_04.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_04.setObjectName("frame_04")
        self.grid_layout.addWidget(self.frame_04, 1, 1, 1, 1)

        main_window.setCentralWidget(self.central_widget)

        self.translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Photo Slideshow"))
        self.frame_01.setText(_translate("MainWindow", "Photo_01"))
        self.frame_02.setText(_translate("MainWindow", "Photo_02"))
        self.frame_03.setText(_translate("MainWindow", "Photo_03"))
        self.frame_04.setText(_translate("MainWindow", "Photo_04"))
