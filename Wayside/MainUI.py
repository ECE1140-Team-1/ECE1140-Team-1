import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, uic
from Track_Configuration import Ui_TrackConfig
from blockwidget import Ui_Section
from pathlib import Path
from Wayside_Main_B import Ui_MainWindow
from test2 import Ui_testpopup

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Wayside Main UI')

        #set all switch buttons to disabled
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)
        self.ga.setEnabled(False)
        self.gb.setEnabled(False)

        #switch button colors
        self.automaticmode.setDown(True)
        self.ca.clicked.connect(lambda: self.toggleColor(self.ca, self.cb))
        self.ca.setStyleSheet('background-color: SkyBlue')
        self.cb.clicked.connect(lambda: self.toggleColor(self.cb, self.ca))
        self.cb.setStyleSheet('background-color: white; color: gray')
        self.ga.clicked.connect(lambda: self.toggleColor(self.ga, self.gb))
        self.ga.setStyleSheet('background-color: SkyBlue')
        self.gb.clicked.connect(lambda: self.toggleColor(self.gb, self.ga))
        self.gb.setStyleSheet('background-color: white; color: gray')

        #pop up windows
        self.trackconfiguration.clicked.connect(self.configurationWindow)
        self.pusha.clicked.connect(self.blocksWindow)
        self.pushb.clicked.connect(self.blocksWindow)
        self.pushc.clicked.connect(self.blocksWindow)
        self.pushd.clicked.connect(self.blocksWindow)
        self.pushe.clicked.connect(self.blocksWindow)
        self.pushf.clicked.connect(self.blocksWindow)
        self.pushg.clicked.connect(self.blocksWindow)
        self.pushh.clicked.connect(self.blocksWindow)
        self.pushi.clicked.connect(self.blocksWindow)
        self.pushj.clicked.connect(self.blocksWindow)

        #set up gate buttons
        self.maintenancemode.toggled.connect(self.maintenanceMode)
        self.automaticmode.toggled.connect(self.automaticMode)

        #active trains
        self.aicon.setPixmap(QPixmap('redtrain.png'))
        counts = 2
        self.activetrains.display(counts)

        #lights
        self.reda.setPixmap(QPixmap('redlight.png'))
        self.greenb.setPixmap(QPixmap('greenlight.png'))

    #function for maintenance mode 
    def maintenanceMode(self):   
        self.ca.setEnabled(True)
        self.cb.setEnabled(True)
        self.ga.setEnabled(True)
        self.gb.setEnabled(True)

    def automaticMode(self):
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)
        self.ga.setEnabled(False)
        self.gb.setEnabled(False)

    #function for pop up window for track configuration
    def configurationWindow(self):
        self.tc = TrackConfig()
        self.tc.show()

    #function for pop up window for seeing blocks in sections
    def blocksWindow(self):
        self.bl = Ui_Section()
        self.bl.show()

    #function for toggle switch colors but see if you can do labels instead of buttons??
    def toggleColor(self, button1, button2): #adams
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue; color: black')
        button2.setStyleSheet('background-color: white; color: gray')

    #function for number of active trains
    #somehow counts the number of times the red train label comes up
    def activeTrains(self, counts):
        self.activetrains.display(counts)

class TrackConfig(QtWidgets.QMainWindow, Ui_TrackConfig):
    def __init__(self, *args, obj=None, **kwargs):
        super(TrackConfig, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Track Configuration')

        self.uploadplc.clicked.connect(self.readplc)

        self.ladderlogic.setDown(True)

    def readplc(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                #print("data: ", data)
                self.plcdisplay.setText(data)

class Ui_Section(QtWidgets.QMainWindow, Ui_Section):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ui_Section, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Block Information')

class Ui_testpopup(QtWidgets.QMainWindow, Ui_testpopup):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ui_testpopup, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Block Information')

        #set up drop down menus
        self.section.currentTextChanged.connect(self.setBlockOptions)

        #toggle lights
        self.reda.toggled.connect(self.changeLights)
        self.yellowa.toggled.connect(self.changeLights)
        self.greena.toggled.connect(self.changeLights)
        self.redb.toggled.connect(self.changeLights)
        self.yellowb.toggled.connect(self.changeLights)
        self.greenb.toggled.connect(self.changeLights)

    def setBlockOptions(self):
        content = self.section.currentText()
        if content == 'A':
            self.block.clear()
            self.block.addItems(['1' , '2', '3'])
        elif content == 'B':
            self.block.clear()
            self.block.addItems(['4', '5', '6'])
        elif content == 'C':
            self.block.clear()
            self.block.addItems(['7', '8', '9'])
        elif content == 'D':
            self.block.clear()
            self.block.addItems(['10', '11', '12'])
        elif content == 'E':
            self.block.clear()
            self.block.addItems(['13', '14', '15'])
        elif content == 'F':
            self.block.clear()
            self.block.addItems(['16', '17', '18', '19', '20'])
        elif content == 'G':
            self.block.clear()
            self.block.addItems(['21', '22', '23'])
        elif content == 'H':
            self.block.clear()
            self.block.addItems(['24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45'])
        elif content == 'I':
            self.block.clear()
            self.block.addItems(['46', '47', '48'])
        elif content == 'J':
            self.block.clear()
            self.block.addItems(['49', '50', '51', '52', '53', '54'])

    def changeLights(self):
        #gate = self.crossingbox.currentText()
        redbuttona = self.reda.isChecked()
        yellowbuttona = self.yellowa.isChecked()
        greenbuttona = self.greena.isChecked()
        redbuttonb = self.redb.isChecked()
        yellowbuttonb = self.yellowb.isChecked()
        greenbuttonb = self.greenb.isChecked()
        #if gate == '1':
        if redbuttona == True:
            window.reda.setPixmap(QPixmap('redlight.png'))
            window.yellowa.setPixmap(QPixmap('offlight.png'))
            window.greena.setPixmap(QPixmap('offlight.png'))
            window.gatepositiona.setText('Active')
        elif yellowbuttona == True:
            window.reda.setPixmap(QPixmap('offlight.png'))
            window.yellowa.setPixmap(QPixmap('yellowlight.png'))
            window.greena.setPixmap(QPixmap('offlight.png'))
            window.gatepositiona.setText('Active')
        elif greenbuttona == True:
            window.reda.setPixmap(QPixmap('offlight.png'))
            window.yellowa.setPixmap(QPixmap('offlight.png'))
            window.greena.setPixmap(QPixmap('greenlight.png'))
            window.gatepositiona.setText('Inactive')
        if redbuttonb == True:
            window.redb.setPixmap(QPixmap('redlight.png'))
            window.yellowb.setPixmap(QPixmap('offlight.png'))
            window.greenb.setPixmap(QPixmap('offlight.png'))
            window.gatepositionb.setText('Active')
        elif yellowbuttonb == True:
            window.redb.setPixmap(QPixmap('offlight.png'))
            window.yellowb.setPixmap(QPixmap('yellowlight.png'))
            window.greenb.setPixmap(QPixmap('offlight.png'))
            window.gatepositionb.setText('Active')
        elif greenbuttonb == True:
            window.redb.setPixmap(QPixmap('offlight.png'))
            window.yellowb.setPixmap(QPixmap('offlight.png'))
            window.greenb.setPixmap(QPixmap('greenlight.png'))
            window.gatepositionb.setText('Inactive')

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
test = Ui_testpopup()
window.show()
test.show()
app.exec()