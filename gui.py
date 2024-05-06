from PyQt5 import QtCore, QtWidgets


class MainWindow(object):
    def __init__(self):
        self.grid_layout = None
        self.central_widget = None
        self.frame_01 = None
        self.frame_02 = None
        self.frame_03 = None
        self.frame_04 = None
        self.frame_05 = None
        self.frame_06 = None
        self.frame_07 = None
        self.frame_08 = None
        self.frame_09 = None

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1920, 1080)
        width = 615
        height = 410
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("gridLayout")

        self.frame_01 = QtWidgets.QLabel(self.central_widget)
        self.frame_01.setMaximumSize(QtCore.QSize(width, height))
        self.frame_01.setScaledContents(True)
        self.frame_01.setObjectName("frame_01")
        self.grid_layout.addWidget(self.frame_01, 0, 0, 1, 1)

        self.frame_02 = QtWidgets.QLabel(self.central_widget)
        self.frame_02.setMaximumSize(QtCore.QSize(width, height))
        self.frame_02.setScaledContents(True)
        self.frame_02.setObjectName("frame_02")
        self.grid_layout.addWidget(self.frame_02, 0, 1, 1, 1)

        self.frame_03 = QtWidgets.QLabel(self.central_widget)
        self.frame_03.setMaximumSize(QtCore.QSize(width, height))
        self.frame_03.setScaledContents(True)
        self.frame_03.setObjectName("frame_03")
        self.grid_layout.addWidget(self.frame_03, 0, 2, 1, 1)

        self.frame_04 = QtWidgets.QLabel(self.central_widget)
        self.frame_04.setMaximumSize(QtCore.QSize(width, height))
        self.frame_04.setScaledContents(True)
        self.frame_04.setObjectName("frame_04")
        self.grid_layout.addWidget(self.frame_04, 1, 0, 1, 1)

        self.frame_05 = QtWidgets.QLabel(self.central_widget)
        self.frame_05.setMaximumSize(QtCore.QSize(width, height))
        self.frame_05.setScaledContents(True)
        self.frame_05.setObjectName("frame_05")
        self.grid_layout.addWidget(self.frame_05, 1, 1, 1, 1)

        self.frame_06 = QtWidgets.QLabel(self.central_widget)
        self.frame_06.setMaximumSize(QtCore.QSize(width, height))
        self.frame_06.setScaledContents(True)
        self.frame_06.setObjectName("frame_06")
        self.grid_layout.addWidget(self.frame_06, 1, 2, 1, 1)

        main_window.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(main_window)


stylesheet = """
    MainWindow {
        background-image: url("C:/git/screen_divider/back_img.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""