# Form implementation generated from reading ui file 'FaultDisplay.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 186)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.WindowHeading = QtWidgets.QLabel(parent=self.centralwidget)
        self.WindowHeading.setGeometry(QtCore.QRect(0, 0, 581, 51))
        self.WindowHeading.setStyleSheet("font-size: 25pt")
        self.WindowHeading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.WindowHeading.setObjectName("WindowHeading")
        self.LineHeading = QtWidgets.QLabel(parent=self.centralwidget)
        self.LineHeading.setGeometry(QtCore.QRect(0, 60, 151, 51))
        self.LineHeading.setStyleSheet("font-size: 18pt;")
        self.LineHeading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LineHeading.setObjectName("LineHeading")
        self.BlockHeading = QtWidgets.QLabel(parent=self.centralwidget)
        self.BlockHeading.setGeometry(QtCore.QRect(150, 60, 181, 51))
        self.BlockHeading.setStyleSheet("font-size: 18pt;")
        self.BlockHeading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.BlockHeading.setObjectName("BlockHeading")
        self.TypeHeading = QtWidgets.QLabel(parent=self.centralwidget)
        self.TypeHeading.setGeometry(QtCore.QRect(340, 60, 241, 51))
        self.TypeHeading.setStyleSheet("font-size: 18pt;")
        self.TypeHeading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TypeHeading.setObjectName("TypeHeading")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(140, 60, 20, 121))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 581, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(330, 60, 20, 121))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.LineSelect = QtWidgets.QComboBox(parent=self.centralwidget)
        self.LineSelect.setGeometry(QtCore.QRect(30, 120, 103, 32))
        self.LineSelect.setObjectName("LineSelect")
        self.BlockSelect = QtWidgets.QComboBox(parent=self.centralwidget)
        self.BlockSelect.setGeometry(QtCore.QRect(190, 120, 103, 32))
        self.BlockSelect.setObjectName("BlockSelect")
        self.FaultLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.FaultLabel.setGeometry(QtCore.QRect(340, 110, 241, 61))
        self.FaultLabel.setStyleSheet("font-size:15pt")
        self.FaultLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.FaultLabel.setObjectName("FaultLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.WindowHeading.setText(_translate("MainWindow", "Track Faults"))
        self.LineHeading.setText(_translate("MainWindow", "Line"))
        self.BlockHeading.setText(_translate("MainWindow", "Block"))
        self.TypeHeading.setText(_translate("MainWindow", "Fault Type"))
        self.FaultLabel.setText(_translate("MainWindow", ""))

        # add options to the dropdown
        self.LineSelect.addItems(['Red', 'Green', 'Blue'])
        self.LineSelect.currentTextChanged.connect(self.lineChanged)

    def lineChanged(self):
        self.BlockSelect.clear()

        if self.LineSelect.currentText() == 'Red':
            self.BlockSelect.addItems(map(str, range(1, 77)))
        elif self.LineSelect.currentText() == 'Green':
            self.BlockSelect.addItems(map(str, range(1, 151)))
        else:
            self.BlockSelect.addItems(map(str, range(1, 16)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())