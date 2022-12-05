import sys
import numpy as np
import torch
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtTest

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from detect import ThreadClass
from guide import Ui_Dialog


class Ui_MainWindow(QWidget):

    start_stop_signal = 0

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('img/logo.png'))
        MainWindow.resize(920, 634)
        MainWindow.setStyleSheet("background-color:rgb(52, 53, 56)")

        self.alarm_red = QPixmap('img/red-alarm.png')
        self.alarm_black = QPixmap('img/black-alarm.png')
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.leftarea = QtWidgets.QVBoxLayout()
        self.leftarea.setObjectName("leftarea")
        
        self.playground = QtWidgets.QLabel(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playground.sizePolicy().hasHeightForWidth())
        
        self.playground.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.playground.setFont(font)
        self.playground.setStyleSheet("color: rgb(255, 255, 255);\n""padding: 3px 3px 3px 3px;")
        self.playground.setObjectName("playground")
        
        self.leftarea.addWidget(self.playground)
        
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        
        self.leftarea.addWidget(self.line1)
        
        self.screen = QtWidgets.QLabel(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen.sizePolicy().hasHeightForWidth())
        
        self.screen.setSizePolicy(sizePolicy)
        self.screen.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.screen.setAlignment(Qt.AlignCenter)
        self.screen.setObjectName("screen")
        
        self.leftarea.addWidget(self.screen)
        
        self.controls = QtWidgets.QLabel(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controls.sizePolicy().hasHeightForWidth())
        
        self.controls.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.controls.setFont(font)
        self.controls.setStyleSheet("color: rgb(255, 255, 255);\n""padding: 3px 3px 3px 3px;")
        self.controls.setObjectName("controls")
        
        self.leftarea.addWidget(self.controls)
        
        self.line4 = QtWidgets.QFrame(self.centralwidget)
        self.line4.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line4.setObjectName("line4")
        
        self.leftarea.addWidget(self.line4)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.start = QtWidgets.QPushButton(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        
        self.start.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.start.setFont(font)
        self.start.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.start.setObjectName("start")
        self.start.clicked.connect(self.start_button)
        
        self.horizontalLayout_3.addWidget(self.start)
        
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        
        self.stop.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.stop.setFont(font)
        self.stop.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.stop.setObjectName("stop")
        self.stop.clicked.connect(self.stop_button)
        
        self.horizontalLayout_3.addWidget(self.stop)
        
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        
        self.reset.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.reset.setFont(font)
        self.reset.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(self.reset_button)
        
        self.horizontalLayout_3.addWidget(self.reset)
        
        self.browseweight = QtWidgets.QPushButton(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseweight.sizePolicy().hasHeightForWidth())
        
        self.browseweight.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.browseweight.setFont(font)
        self.browseweight.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.browseweight.setObjectName("browseweight")
        self.browseweight.clicked.connect(self.browse_weight_button)
        
        self.horizontalLayout_3.addWidget(self.browseweight)
        
        self.guide = QtWidgets.QPushButton(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guide.sizePolicy().hasHeightForWidth())
        
        self.guide.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.guide.setFont(font)
        self.guide.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.guide.setText("")
        self.guide.setObjectName("guide")
        self.guide.setIcon(QtGui.QIcon('img/info-guide.png'))
        self.guide.clicked.connect(self.guide_button)
        
        self.horizontalLayout_3.addWidget(self.guide)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.horizontalLayout_3.addItem(spacerItem)
        
        self.alarm = QtWidgets.QLabel(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alarm.sizePolicy().hasHeightForWidth())
        
        self.alarm.setSizePolicy(sizePolicy)
        self.alarm.setText("")
        self.alarm.setObjectName("alarm")
        
        self.horizontalLayout_3.addWidget(self.alarm)
        
        self.leftarea.addLayout(self.horizontalLayout_3)
        
        self.horizontalLayout.addLayout(self.leftarea)
        
        self.rightarea = QtWidgets.QVBoxLayout()
        self.rightarea.setObjectName("rightarea")
        
        self.gpu = QtWidgets.QLabel(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpu.sizePolicy().hasHeightForWidth())
        
        self.gpu.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.gpu.setFont(font)
        self.gpu.setStyleSheet("color: rgb(255, 255, 255);\n""padding: 3px 3px 3px 3px;")
        self.gpu.setObjectName("gpu")
        
        self.rightarea.addWidget(self.gpu)
        
        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        
        self.rightarea.addWidget(self.line2)
        
        self.gpuname = QtWidgets.QLabel(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpuname.sizePolicy().hasHeightForWidth())
        
        self.gpuname.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        self.gpuname.setFont(font)
        self.gpuname.setStyleSheet("color: rgb(255, 255, 255);\n""padding: 3px 3px 3px 3px;")
        self.gpuname.setObjectName("gpuname")
        
        self.rightarea.addWidget(self.gpuname)
        
        self.information = QtWidgets.QLabel(self.centralwidget)
        self.information.setEnabled(True)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.information.sizePolicy().hasHeightForWidth())
        
        self.information.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.information.setFont(font)
        self.information.setStyleSheet("color: rgb(255, 255, 255);\n""padding: 3px 3px 3px 3px;")
        self.information.setObjectName("information")
        
        self.rightarea.addWidget(self.information)
        
        self.line3 = QtWidgets.QFrame(self.centralwidget)
        self.line3.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        
        self.rightarea.addWidget(self.line3)
        
        self.info = QtWidgets.QPlainTextEdit(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        
        self.info.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.info.setFont(font)
        self.info.setStyleSheet("color: rgb(255, 255, 255);")
        self.info.setObjectName("info")
        self.info.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        
        self.rightarea.addWidget(self.info)
        
        self.source = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.source.setFont(font)
        self.source.setStyleSheet("color: rgb(255, 255, 255);\n""padding: 3px 3px 3px 3px;")
        self.source.setObjectName("source")
        
        self.rightarea.addWidget(self.source)
        
        self.line5 = QtWidgets.QFrame(self.centralwidget)
        self.line5.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line5.setObjectName("line5")
        
        self.rightarea.addWidget(self.line5)
        
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.browse.setFont(font)
        self.browse.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.browse.setObjectName("browse")
        self.browse.clicked.connect(self.browse_button)
        
        self.rightarea.addWidget(self.browse)
        
        self.camera = QtWidgets.QPushButton(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.camera.setFont(font)
        self.camera.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        self.camera.setObjectName("camera")
        self.camera.clicked.connect(self.camera_button)
        
        self.rightarea.addWidget(self.camera)
        
        self.horizontalLayout.addLayout(self.rightarea)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Checking if CUDA if available
        if torch.cuda.is_available() == True:
            
            # Getting the Graphic Card Details
            device = torch.cuda.get_device_properties(0)
            card_name = device.name
            card_name = card_name.replace('Laptop', '')
            card_name = card_name.replace('GPU', '')
            card_size = device.total_memory / 1024 ** 2
            string = card_name + '\n' + str(card_size) + ' MB'

            # Showing the details of Card
            self.gpuname.setText(string)

            # Showing torch version
            string = 'torch verison ' + str(torch.__version__) + '\n'
            self.info.insertPlainText(string)

            # Disabling all buttons
            self.info.insertPlainText('Please select weight...\n')

            self.start.setEnabled(False)
            self.start.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            self.stop.setEnabled(False)
            self.stop.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            self.reset.setEnabled(False)
            self.reset.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            self.browse.setEnabled(False)
            self.browse.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            self.camera.setEnabled(False)
            self.camera.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")
        
        else:

            # Showing Critial Message
            msg = QMessageBox()
            msg.setWindowTitle('CRITICAL')
            msg.setText('CUDA')
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('CUDA not available for PyTorch!')

            x = msg.exec_()
            sys.exit()

    def guide_button(self):
        self.guide_window = QtWidgets.QDialog()
        self.guide_ui = Ui_Dialog()
        self.guide_ui.setupUi(self.guide_window)
        self.guide_window.show()
    
    def start_button(self):
        self.info.insertPlainText('Starting Predictions...\nPlease Wait...\n')
        self.set_start_stop_signal(1)

        # Disabling Button
        self.start.setEnabled(False)
        self.start.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        # Enabling Button
        self.stop.setEnabled(True)
        self.stop.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        # Alarm Display
        self.alarm.setPixmap(self.alarm_black)

    def stop_button(self):
        self.info.insertPlainText('Stoping Predictions...\nPlease Wait...\n')
        self.set_start_stop_signal(0)

        # Disabling Button
        self.stop.setEnabled(False)
        self.stop.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        # Enabling Button
        self.start.setEnabled(True)
        self.start.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        # Alarm Clear
        # self.alarm.clear()
        # self.alarm.setPixmap(self.alarm_black)

    def reset_button(self):
        self.set_start_stop_signal(0)

        # Terminating the Thread
        self.model_thread.stop()

        # Clearing the info and screen
        self.info.clear()

        # Adding basic things in info
        self.info.insertPlainText('torch verison ' + str(torch.__version__) + '\n')
        self.info.insertPlainText('Please select weight...\n')

        # Weights
        self.weights = ''

        # Enabling Button
        self.browseweight.setEnabled(True)
        self.browseweight.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        # Disabling Button
        self.start.setEnabled(False)
        self.start.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        self.stop.setEnabled(False)
        self.stop.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        self.reset.setEnabled(False)
        self.reset.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        self.browse.setEnabled(False)
        self.browse.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        self.camera.setEnabled(False)
        self.camera.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        QtTest.QTest.qWait(1000)

        # Reseting the screen
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(QtGui.QColor("black"))
        self.screen.setPixmap(canvas)

        # Alarm Clear
        self.alarm.clear()

    def browse_weight_button(self):
        weight_file = QFileDialog.getOpenFileName(self, "Choose Weight", "", "PT Files (*.pt)")
        file = QUrl.fromLocalFile(weight_file[0])

        # Selected weight file
        if weight_file[0] != '':
            self.info.insertPlainText('Weight - ' + file.fileName() + '\n')
            self.info.insertPlainText('(' + weight_file[0] + ')\n')
            self.weights = weight_file[0]

            # Enabling Buttons
            self.browse.setEnabled(True)
            self.browse.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            self.camera.setEnabled(True)
            self.camera.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            # Disabling Button
            self.browseweight.setEnabled(False)
            self.browseweight.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            self.info.insertPlainText('Please select source...\n')

    def browse_button(self):
        # Choosing Video File
        video_file = QFileDialog.getOpenFileName(self, "Select Video", "", "Video Files (*.mp4)")

        # Checking if file is not empty
        if video_file[0] != '':
            self.info.insertPlainText('Loading Video...\nPlease Wait...\n')

            # Enabling Buttons
            self.start.setEnabled(True)
            self.start.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            self.reset.setEnabled(True)
            self.reset.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            # Disabling Buttons
            self.camera.setEnabled(False)
            self.camera.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            self.browse.setEnabled(False)
            self.browse.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

            # Creating new Thread and calling it
            self.model_thread = ThreadClass(parent = None, source = video_file[0], weights = self.weights, base_class = self)
            self.model_thread.start()
            self.model_thread.info_signal.connect(self.signal_from_threadclass_info)
            self.model_thread.pic_signal.connect(self.signal_from_threadclass_pic)
            self.model_thread.alarm_signal.connect(self.signal_from_threadclass_alarm)


    def camera_button(self):
        # Adding information to info
        self.info.insertPlainText('Loading Camera....\nPlease Wait....\n')

        # Enabling Buttons
        self.start.setEnabled(True)
        self.start.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        self.reset.setEnabled(True)
        self.reset.setStyleSheet("background-color: rgb(85, 255, 0);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        # Disabling Buttons
        self.camera.setEnabled(False)
        self.camera.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        self.browse.setEnabled(False)
        self.browse.setStyleSheet("background-color: rgb(152, 152, 152);\n""border-color: rgb(0, 0, 0);\n""color: rgb(255, 255, 255);")

        # Creating new Thread and calling it
        self.model_thread = ThreadClass(parent = None, source = '0', weights = self.weights, base_class = self)
        self.model_thread.start()
        self.model_thread.info_signal.connect(self.signal_from_threadclass_info)
        self.model_thread.pic_signal.connect(self.signal_from_threadclass_pic)
        self.model_thread.alarm_signal.connect(self.signal_from_threadclass_alarm)

    def signal_from_threadclass_info(self, signal):
        self.info.insertPlainText(signal)

    def signal_from_threadclass_pic(self, signal):
        self.screen.setPixmap(QPixmap.fromImage(signal))

    def signal_from_threadclass_alarm(self, signal):
        # 0 - No Alarm (Black)
        # 1 - Alarm (Red)
        if signal == 0:
            self.alarm.setPixmap(self.alarm_black)
        else:
            self.alarm.setPixmap(self.alarm_red)

    def get_start_stop_signal(self):
        return self.start_stop_signal

    def set_start_stop_signal(self, value):
        self.start_stop_signal = value

    def get_screen_width(self):
        return self.screen.width()

    def get_screen_height(self):
        return self.screen.height()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Object Detection"))
        self.playground.setText(_translate("MainWindow", "PLAYGROUND"))
        self.screen.setText(_translate("MainWindow", "TextLabel"))
        self.controls.setText(_translate("MainWindow", "CONTROLS"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.browseweight.setText(_translate("MainWindow", "BROWSE WEIGHT"))
        self.gpu.setText(_translate("MainWindow", "GPU"))
        self.gpuname.setText(_translate("MainWindow", "NVIDIA GeForce RTX 3050Ti\n""2022"))
        self.information.setText(_translate("MainWindow", "INFORMATION"))
        self.source.setText(_translate("MainWindow", "SOURCE"))
        self.browse.setText(_translate("MainWindow", "BROWSE"))
        self.camera.setText(_translate("MainWindow", "CAMERA"))


if __name__ == "__main__":
    import sys

    # if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    #     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    # if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    #     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
