from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 353)
        Dialog.setStyleSheet("background-color: rgb(52, 53, 56);")
        Dialog.setWindowIcon(QtGui.QIcon('img/info-guide.png'))
        
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label = QtWidgets.QLabel(Dialog)
        
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GUIDE"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>1. First select the weight file with the help of Browse Weight button.<span style=\" font-size:9pt; color:#55ff00;\"><br>(Note: Weight files have .pt extension)</span></p><p>2. Select the source i.e Video or Camera.<span style=\" font-size:9pt; color:#55ff00;\"><br>(Note: It may take few seconds to load the source)</span></p><p>3. Press START button to start Predictions.<span style=\" font-size:9pt; color:#55ff00;\"><br>(Note: Depending upon the GPU of your system FPS will differ.</span><span style=\" font-size:9pt; color:#55ff00;\"><br>Once you press the start button the alarm will appear.</span><span style=\" font-size:9pt; color:#55ff00;\"><br>The alarm will turn red as soon as it detects gun or knife in the frame)</span></p><p>4. Press STOP button to stop Predictions.<span style=\" font-size:9pt; color:#55ff00;\"><br>(Note: You can start predictions again by pressing start button)</span></p><p>5. Press RESET button to reset the loaded source.<span style=\" font-size:9pt; color:#55ff00;\"><br>(Note: The alarm will disappear)</span></p><p align=\"center\"><span style=\" font-size:9pt;\">The Application uses Pytorch and only supports CUDA as it\'s backend.</span><span style=\" font-size:9pt;\"><br>It also uses OpenCV to load the frame and draw boxes around the detected objects in the frame.</span></p></body></html>"))
