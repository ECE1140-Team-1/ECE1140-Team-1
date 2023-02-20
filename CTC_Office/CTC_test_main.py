# Form implementation generated from reading ui file 'E:\ECE1140-Team-1\CTC_Office\CTC_test.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

switchStateButtons = [
    "green_C1", "green_C2", "green_G1", "green_G2", "green_J1_1", "green_J1_2", "green_J2_1", "green_J2_2", "green_M1", "green_M2", "green_N1", "green_N2",
    "red_C1", "red_C2", "red_E1", "red_E2", "red_H1_1", "red_H1_2", "red_H2_1", "red_H2_2", "red_H3_1", "red_H3_2", "red_H4_1", "red_H4_2", "red_J1", "red_J2"
]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 743)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.locationText = QtWidgets.QLabel(parent=self.centralwidget)
        self.locationText.setGeometry(QtCore.QRect(130, 110, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.locationText.setFont(font)
        self.locationText.setObjectName("locationText")
        self.enterLocation = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.enterLocation.setGeometry(QtCore.QRect(400, 110, 91, 28))
        self.enterLocation.setObjectName("enterLocation")
        self.enterSpeed = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.enterSpeed.setGeometry(QtCore.QRect(340, 160, 91, 28))
        self.enterSpeed.setText("")
        self.enterSpeed.setObjectName("enterSpeed")
        self.speedText = QtWidgets.QLabel(parent=self.centralwidget)
        self.speedText.setGeometry(QtCore.QRect(130, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.speedText.setFont(font)
        self.speedText.setObjectName("speedText")
        self.mph = QtWidgets.QLabel(parent=self.centralwidget)
        self.mph.setGeometry(QtCore.QRect(440, 160, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mph.setFont(font)
        self.mph.setObjectName("mph")
        self.InputsBox = QtWidgets.QFrame(parent=self.centralwidget)
        self.InputsBox.setGeometry(QtCore.QRect(100, 20, 411, 51))
        self.InputsBox.setAutoFillBackground(False)
        self.InputsBox.setStyleSheet("background-color: #B8B8B8\n""")
        self.InputsBox.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.InputsBox.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.InputsBox.setObjectName("InputsBox")
        self.Inputs = QtWidgets.QLabel(parent=self.InputsBox)
        self.Inputs.setGeometry(QtCore.QRect(170, 0, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Inputs.setFont(font)
        self.Inputs.setStyleSheet("color: black")
        self.Inputs.setObjectName("Inputs")
        self.OutputsBox_18 = QtWidgets.QFrame(parent=self.centralwidget)
        self.OutputsBox_18.setGeometry(QtCore.QRect(100, 240, 411, 51))
        self.OutputsBox_18.setAutoFillBackground(False)
        self.OutputsBox_18.setStyleSheet("background-color: #B8B8B8")
        self.OutputsBox_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.OutputsBox_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.OutputsBox_18.setObjectName("OutputsBox_18")
        self.Outputs_2 = QtWidgets.QLabel(parent=self.OutputsBox_18)
        self.Outputs_2.setGeometry(QtCore.QRect(170, 0, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Outputs_2.setFont(font)
        self.Outputs_2.setStyleSheet("color: black")
        self.Outputs_2.setObjectName("Outputs_2")
        self.authority = QtWidgets.QLabel(parent=self.centralwidget)
        self.authority.setGeometry(QtCore.QRect(160, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.authority.setFont(font)
        self.authority.setObjectName("authority")
        self.suggSpeedOutput = QtWidgets.QLabel(parent=self.centralwidget)
        self.suggSpeedOutput.setGeometry(QtCore.QRect(330, 320, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.suggSpeedOutput.setFont(font)
        self.suggSpeedOutput.setObjectName("suggSpeedOutput")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 360, 471, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.greenLine_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.greenLine_2.setGeometry(QtCore.QRect(150, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.greenLine_2.setFont(font)
        self.greenLine_2.setObjectName("greenLine_2")
        self.redLineText = QtWidgets.QLabel(parent=self.centralwidget)
        self.redLineText.setGeometry(QtCore.QRect(390, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.redLineText.setFont(font)
        self.redLineText.setObjectName("redLineText")
        self.lineSelect = QtWidgets.QComboBox(parent=self.centralwidget)
        self.lineSelect.setGeometry(QtCore.QRect(300, 110, 82, 28))
        self.lineSelect.setObjectName("lineSelect")
        self.lineSelect.addItem("")
        self.lineSelect.addItem("")
        self.lineText = QtWidgets.QLabel(parent=self.centralwidget)
        self.lineText.setGeometry(QtCore.QRect(320, 80, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineText.setFont(font)
        self.lineText.setObjectName("lineText")
        self.blockText = QtWidgets.QLabel(parent=self.centralwidget)
        self.blockText.setGeometry(QtCore.QRect(420, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.blockText.setFont(font)
        self.blockText.setObjectName("blockText")
        self.enterButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(430, 200, 83, 29))
        self.enterButton.setObjectName("enterButton")
        self.clearButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(330, 200, 83, 29))
        self.clearButton.setObjectName("clearButton")
        self.autoSelect = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.autoSelect.setGeometry(QtCore.QRect(290, 650, 78, 22))
        self.autoSelect.setObjectName("autoSelect")
        self.manualSelect = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.manualSelect.setGeometry(QtCore.QRect(370, 650, 61, 22))
        self.manualSelect.setObjectName("manualSelect")
        self.maintenanceSelect = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.maintenanceSelect.setGeometry(QtCore.QRect(440, 650, 91, 22))
        self.maintenanceSelect.setObjectName("maintenanceSelect")
        self.modesText = QtWidgets.QLabel(parent=self.centralwidget)
        self.modesText.setGeometry(QtCore.QRect(240, 650, 41, 16))
        self.modesText.setObjectName("modesText")
        self.red_C2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_C2.setGeometry(QtCore.QRect(450, 420, 80, 24))
        self.red_C2.setObjectName("red_C2")
        self.red_C1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_C1.setGeometry(QtCore.QRect(370, 420, 80, 24))
        self.red_C1.setObjectName("red_C1")
        self.red_H1_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_H1_2.setGeometry(QtCore.QRect(450, 480, 80, 24))
        self.red_H1_2.setObjectName("red_H1_2")
        self.red_H1_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_H1_1.setGeometry(QtCore.QRect(370, 480, 80, 24))
        self.red_H1_1.setObjectName("red_H1_1")
        self.red_E2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_E2.setGeometry(QtCore.QRect(450, 450, 80, 24))
        self.red_E2.setObjectName("red_E2")
        self.red_E1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_E1.setGeometry(QtCore.QRect(370, 450, 80, 24))
        self.red_E1.setObjectName("red_E1")
        self.red_H4_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_H4_2.setGeometry(QtCore.QRect(450, 570, 80, 24))
        self.red_H4_2.setObjectName("red_H4_2")
        self.red_H3_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_H3_2.setGeometry(QtCore.QRect(450, 540, 80, 24))
        self.red_H3_2.setObjectName("red_H3_2")
        self.red_H3_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_H3_1.setGeometry(QtCore.QRect(370, 540, 80, 24))
        self.red_H3_1.setObjectName("red_H3_1")
        self.red_J2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_J2.setGeometry(QtCore.QRect(450, 600, 80, 24))
        self.red_J2.setObjectName("red_J2")
        self.red_H2_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_H2_2.setGeometry(QtCore.QRect(450, 510, 80, 24))
        self.red_H2_2.setObjectName("red_H2_2")
        self.red_H2_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_H2_1.setGeometry(QtCore.QRect(370, 510, 80, 24))
        self.red_H2_1.setObjectName("red_H2_1")
        self.red_J1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_J1.setGeometry(QtCore.QRect(370, 600, 80, 24))
        self.red_J1.setObjectName("red_J1")
        self.red_H4_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.red_H4_1.setGeometry(QtCore.QRect(370, 570, 80, 24))
        self.red_H4_1.setObjectName("red_H4_1")
        self.green_G2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_G2.setGeometry(QtCore.QRect(210, 450, 80, 24))
        self.green_G2.setObjectName("green_G2")
        self.green_C2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_C2.setGeometry(QtCore.QRect(210, 420, 80, 24))
        self.green_C2.setObjectName("green_C2")
        self.green_C1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_C1.setGeometry(QtCore.QRect(130, 420, 80, 24))
        self.green_C1.setObjectName("green_C1")
        self.green_J1_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_J1_2.setGeometry(QtCore.QRect(210, 480, 80, 24))
        self.green_J1_2.setObjectName("green_J1_2")
        self.green_N1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_N1.setGeometry(QtCore.QRect(130, 570, 80, 24))
        self.green_N1.setObjectName("green_N1")
        self.green_J2_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_J2_2.setGeometry(QtCore.QRect(210, 510, 80, 24))
        self.green_J2_2.setObjectName("green_J2_2")
        self.green_N2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_N2.setGeometry(QtCore.QRect(210, 570, 80, 24))
        self.green_N2.setObjectName("green_N2")
        self.green_J1_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_J1_1.setGeometry(QtCore.QRect(130, 480, 80, 24))
        self.green_J1_1.setObjectName("green_J1_1")
        self.green_M1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_M1.setGeometry(QtCore.QRect(130, 540, 80, 24))
        self.green_M1.setObjectName("green_M1")
        self.green_J2_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_J2_1.setGeometry(QtCore.QRect(130, 510, 80, 24))
        self.green_J2_1.setObjectName("green_J2_1")
        self.green_G1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_G1.setGeometry(QtCore.QRect(130, 450, 80, 24))
        self.green_G1.setObjectName("green_G1")
        self.green_M2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.green_M2.setGeometry(QtCore.QRect(210, 540, 80, 24))
        self.green_M2.setObjectName("green_M2")
        self.red_text_C = QtWidgets.QLabel(parent=self.centralwidget)
        self.red_text_C.setGeometry(QtCore.QRect(330, 420, 16, 16))
        self.red_text_C.setObjectName("red_text_C")
        self.red_text_E = QtWidgets.QLabel(parent=self.centralwidget)
        self.red_text_E.setGeometry(QtCore.QRect(330, 450, 16, 16))
        self.red_text_E.setObjectName("red_text_E")
        self.red_text_H1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.red_text_H1.setGeometry(QtCore.QRect(330, 480, 16, 16))
        self.red_text_H1.setObjectName("red_text_H1")
        self.red_textH2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.red_textH2.setGeometry(QtCore.QRect(330, 510, 16, 16))
        self.red_textH2.setObjectName("red_textH2")
        self.red_textH3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.red_textH3.setGeometry(QtCore.QRect(330, 540, 16, 16))
        self.red_textH3.setObjectName("red_textH3")
        self.red_text_H4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.red_text_H4.setGeometry(QtCore.QRect(330, 570, 16, 16))
        self.red_text_H4.setObjectName("red_text_H4")
        self.red_text_J = QtWidgets.QLabel(parent=self.centralwidget)
        self.red_text_J.setGeometry(QtCore.QRect(330, 600, 16, 16))
        self.red_text_J.setObjectName("red_text_J")
        self.green_text_N = QtWidgets.QLabel(parent=self.centralwidget)
        self.green_text_N.setGeometry(QtCore.QRect(90, 570, 16, 16))
        self.green_text_N.setObjectName("green_text_N")
        self.green_text_C = QtWidgets.QLabel(parent=self.centralwidget)
        self.green_text_C.setGeometry(QtCore.QRect(90, 420, 16, 16))
        self.green_text_C.setObjectName("green_text_C")
        self.green_text_M = QtWidgets.QLabel(parent=self.centralwidget)
        self.green_text_M.setGeometry(QtCore.QRect(90, 540, 16, 16))
        self.green_text_M.setObjectName("green_text_M")
        self.green_text_G = QtWidgets.QLabel(parent=self.centralwidget)
        self.green_text_G.setGeometry(QtCore.QRect(90, 450, 16, 16))
        self.green_text_G.setObjectName("green_text_G")
        self.green_text_J1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.green_text_J1.setGeometry(QtCore.QRect(90, 480, 16, 16))
        self.green_text_J1.setObjectName("green_text_J1")
        self.green_text_J2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.green_text_J2.setGeometry(QtCore.QRect(90, 510, 16, 16))
        self.green_text_J2.setObjectName("green_text_J2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 21))
        self.menubar.setObjectName("menubar")
        self.menuCTC_Dispatcher_Test_UI = QtWidgets.QMenu(parent=self.menubar)
        self.menuCTC_Dispatcher_Test_UI.setObjectName("menuCTC_Dispatcher_Test_UI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCTC_Dispatcher_Test_UI.menuAction())

        #switch which mode the test UI is in
        self.autoSelect.clicked.connect(self.autoSwitch)
        self.autoSelect.clicked.connect(self.otherModes)
        self.manualSelect.clicked.connect(self.manualSwitch)
        self.manualSelect.clicked.connect(self.otherModes)
        self.maintenanceSelect.clicked.connect(self.maintenanceSwitch)
        self.maintenanceSelect.clicked.connect(self.maintenanceMode)
        self.autoSelect.setChecked(True) #always initially in auto mode

        #set initial switch states
        self.green_C1.clicked.connect(lambda: self.toggleColor(self.green_C1))
        self.green_C2.clicked.connect(lambda: self.toggleColor(self.green_C2))

        #suggested speed set
        self.enterButton.clicked.connect(self.showSuggSpeed)

        #clear button clears all text fields
        self.clearButton.clicked.connect(self.clearInputs)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def toggleColor(self, button):
        #button = self.sender()
        if button.styleSheet() == 'background-color: white':
            button.setStyleSheet('background-color: blue')
            if button == self.green_C1:
                self.green_C1.setStyleSheet('background-color: white')
            else:
                self.green_C2.setStyleSheet('background-color: white')
        else:
            button.setStyleSheet('background-color: white')

    def switchStates(self):
        if self.green_C1.isChecked:
            self.green_C1.setStyleSheet("background-color: #ADD8E6")
            self.green_C2.setStyleSheet("background-color: None")
        else:
            self.green_C1.setStyleSheet("background-color: None")
            self.green_C2.setStyleSheet("background-color: #ADD8E6")


    def maintenanceMode(self):
        self.enterLocation.setEnabled(False)
        self.enterSpeed.setEnabled(False)
        self.lineSelect.setEnabled(False)
        self.enterButton.setEnabled(False)
        self.clearButton.setEnabled(False)

        self.green_C1.setEnabled(True)
        self.green_C2.setEnabled(True)
        self.green_G1.setEnabled(True)
        self.green_G2.setEnabled(True)
        self.green_J1_1.setEnabled(True)
        self.green_J1_2.setEnabled(True)
        self.green_J2_1.setEnabled(True)
        self.green_J2_2.setEnabled(True)
        self.green_M1.setEnabled(True)
        self.green_M2.setEnabled(True)
        self.green_N1.setEnabled(True)
        self.green_N2.setEnabled(True)

        self.red_C1.setEnabled(True)
        self.red_C2.setEnabled(True)
        self.red_E1.setEnabled(True)
        self.red_E2.setEnabled(True)
        self.red_H1_1.setEnabled(True)
        self.red_H1_2.setEnabled(True)
        self.red_H2_1.setEnabled(True)
        self.red_H2_2.setEnabled(True)
        self.red_H3_1.setEnabled(True)
        self.red_H3_2.setEnabled(True)
        self.red_H4_1.setEnabled(True)
        self.red_H4_2.setEnabled(True)
        self.red_J1.setEnabled(True)
        self.red_J2.setEnabled(True)


    def otherModes(self):
        self.enterLocation.setEnabled(True)
        self.enterSpeed.setEnabled(True)
        self.lineSelect.setEnabled(True)
        self.enterButton.setEnabled(True)
        self.clearButton.setEnabled(True)

        self.green_C1.setEnabled(False)
        self.green_C2.setEnabled(False)
        self.green_G1.setEnabled(False)
        self.green_G2.setEnabled(False)
        self.green_J1_1.setEnabled(False)
        self.green_J1_2.setEnabled(False)
        self.green_J2_1.setEnabled(False)
        self.green_J2_2.setEnabled(False)
        self.green_M1.setEnabled(False)
        self.green_M2.setEnabled(False)
        self.green_N1.setEnabled(False)
        self.green_N2.setEnabled(False)

        self.red_C1.setEnabled(False)
        self.red_C2.setEnabled(False)
        self.red_E1.setEnabled(False)
        self.red_E2.setEnabled(False)
        self.red_H1_1.setEnabled(False)
        self.red_H1_2.setEnabled(False)
        self.red_H2_1.setEnabled(False)
        self.red_H2_2.setEnabled(False)
        self.red_H3_1.setEnabled(False)
        self.red_H3_2.setEnabled(False)
        self.red_H4_1.setEnabled(False)
        self.red_H4_2.setEnabled(False)
        self.red_J1.setEnabled(False)
        self.red_J2.setEnabled(False)

    def clearInputs(self):
        self.enterLocation.setText("{0}".format(""))
        self.enterSpeed.setText("{0}".format(""))
        self.suggSpeedOutput.setText("Suggested Speed: --mph")
        self.authority.setText("Authority: --mi")

    def showSuggSpeed(self):
        entSpeed = self.enterSpeed.text()
        self.suggSpeedOutput.setText("Suggested Speed: {0}mph".format(entSpeed))
        self.enterLocation.setText("{0}".format(""))
        self.enterSpeed.setText("{0}".format(""))

    def autoSwitch(self):
        self.manualSelect.setChecked(False)
        self.maintenanceSelect.setChecked(False)
        self.greenLine_2.setStyleSheet("background-color: none")
        self.greenLine_2.setStyleSheet("color: black")
        self.redLineText.setStyleSheet("background-color: none")
        self.redLineText.setStyleSheet("color: black")

    def manualSwitch(self):
        self.autoSelect.setChecked(False)
        self.maintenanceSelect.setChecked(False)
        self.greenLine_2.setStyleSheet("background-color: none")
        self.greenLine_2.setStyleSheet("color: black")
        self.redLineText.setStyleSheet("background-color: none")
        self.redLineText.setStyleSheet("color: black")

    def maintenanceSwitch(self):
        self.manualSelect.setChecked(False)
        self.autoSelect.setChecked(False)
        self.greenLine_2.setStyleSheet("background-color: green")
        self.greenLine_2.setStyleSheet("color: green")
        self.redLineText.setStyleSheet("background-color: pink")
        self.redLineText.setStyleSheet("color: red")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.locationText.setText(_translate("MainWindow", "Enter Train Location:"))
        self.speedText.setText(_translate("MainWindow", "Enter Suggested Speed:"))
        self.mph.setText(_translate("MainWindow", "mph"))
        self.Inputs.setText(_translate("MainWindow", "Inputs"))
        self.Outputs_2.setText(_translate("MainWindow", "Outputs"))
        self.authority.setText(_translate("MainWindow", "Authority: --mi"))
        self.suggSpeedOutput.setText(_translate("MainWindow", "Suggested Speed: --mph"))
        self.greenLine_2.setText(_translate("MainWindow", "Green Line"))
        self.redLineText.setText(_translate("MainWindow", "Red Line"))
        self.lineSelect.setItemText(0, _translate("MainWindow", "Green"))
        self.lineSelect.setItemText(1, _translate("MainWindow", "Red"))
        self.lineText.setText(_translate("MainWindow", "Line"))
        self.blockText.setText(_translate("MainWindow", "Block"))
        self.enterButton.setText(_translate("MainWindow", "Enter"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.autoSelect.setText(_translate("MainWindow", "Automatic"))
        self.manualSelect.setText(_translate("MainWindow", "Manual"))
        self.maintenanceSelect.setText(_translate("MainWindow", "Maintenance"))
        self.modesText.setText(_translate("MainWindow", "Modes:"))
        self.red_C2.setText(_translate("MainWindow", "9-Yard"))
        self.red_C1.setText(_translate("MainWindow", "9-10"))
        self.red_H1_2.setText(_translate("MainWindow", "27-76"))
        self.red_H1_1.setText(_translate("MainWindow", "27-28"))
        self.red_E2.setText(_translate("MainWindow", "1-16"))
        self.red_E1.setText(_translate("MainWindow", "15-16"))
        self.red_H4_2.setText(_translate("MainWindow", "43-67"))
        self.red_H3_2.setText(_translate("MainWindow", "38-71"))
        self.red_H3_1.setText(_translate("MainWindow", "38-39"))
        self.red_J2.setText(_translate("MainWindow", "52-66"))
        self.red_H2_2.setText(_translate("MainWindow", "32-72"))
        self.red_H2_1.setText(_translate("MainWindow", "32-33"))
        self.red_J1.setText(_translate("MainWindow", "52-53"))
        self.red_H4_1.setText(_translate("MainWindow", "43-44"))
        self.green_G2.setText(_translate("MainWindow", "29-150"))
        self.green_C2.setText(_translate("MainWindow", "1-13"))
        self.green_C1.setText(_translate("MainWindow", "12-13"))
        self.green_J1_2.setText(_translate("MainWindow", "57-58"))
        self.green_N1.setText(_translate("MainWindow", "85-86"))
        self.green_J2_2.setText(_translate("MainWindow", "Yard-63"))
        self.green_N2.setText(_translate("MainWindow", "85-100"))
        self.green_J1_1.setText(_translate("MainWindow", "57-Yard"))
        self.green_M1.setText(_translate("MainWindow", "76-77"))
        self.green_J2_1.setText(_translate("MainWindow", "62-63"))
        self.green_G1.setText(_translate("MainWindow", "29-30"))
        self.green_M2.setText(_translate("MainWindow", "77-101"))
        self.red_text_C.setText(_translate("MainWindow", "C"))
        self.red_text_E.setText(_translate("MainWindow", "E"))
        self.red_text_H1.setText(_translate("MainWindow", "H"))
        self.red_textH2.setText(_translate("MainWindow", "H"))
        self.red_textH3.setText(_translate("MainWindow", "H"))
        self.red_text_H4.setText(_translate("MainWindow", "H"))
        self.red_text_J.setText(_translate("MainWindow", "J"))
        self.green_text_N.setText(_translate("MainWindow", "N"))
        self.green_text_C.setText(_translate("MainWindow", "C"))
        self.green_text_M.setText(_translate("MainWindow", "M"))
        self.green_text_G.setText(_translate("MainWindow", "G"))
        self.green_text_J1.setText(_translate("MainWindow", "J"))
        self.green_text_J2.setText(_translate("MainWindow", "J"))
        self.menuCTC_Dispatcher_Test_UI.setTitle(_translate("MainWindow", "CTC Dispatcher - Test UI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
