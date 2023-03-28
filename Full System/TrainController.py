import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track
#from TrainModel import TrainModel

class TrainController(QObject):
    
    trainPowertoTrainModel = pyqtSignal(Train)

    def __init__(self, trainModel):
        super().__init__()        
        self.TrainModel = trainModel
        self.TrainModel.actSpeedtoTrainController.connect(self.sendPower)

    def sendPower(self, actualSpeed):
        self.actualSpeed = actualSpeed
        self.trainPowertoTrainModel.emit(actualSpeed)
        print("sendPower called")

