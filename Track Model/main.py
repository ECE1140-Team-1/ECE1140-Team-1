import sys
from PyQt6 import QtCore, QtGui, QtWidgets
sys.path.append('../Full System')

from TrackModelUI import TrackModelUI
from TestUI import TestUI
import TrackParser

track = TrackParser.parseTrack('TrackLayout.csv')

app = QtWidgets.QApplication(sys.argv)
testui = TestUI(track)
model = TrackModelUI(track)

testui.show()
model.show()

app.exec()