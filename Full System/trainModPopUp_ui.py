# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trainModPopUp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(418, 269)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.trainLength = QLabel(self.centralwidget)
        self.trainLength.setObjectName(u"trainLength")
        self.trainLength.setGeometry(QRect(20, 20, 291, 31))
        self.trainLength.setStyleSheet(u"")
        self.trainWidth = QLabel(self.centralwidget)
        self.trainWidth.setObjectName(u"trainWidth")
        self.trainWidth.setGeometry(QRect(20, 60, 291, 31))
        self.passengers = QLabel(self.centralwidget)
        self.passengers.setObjectName(u"passengers")
        self.passengers.setGeometry(QRect(20, 100, 291, 31))
        self.currentMass = QLabel(self.centralwidget)
        self.currentMass.setObjectName(u"currentMass")
        self.currentMass.setGeometry(QRect(20, 140, 291, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 418, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.trainLength.setText(QCoreApplication.translate("MainWindow", u"Train Length:", None))
        self.trainWidth.setText(QCoreApplication.translate("MainWindow", u"Train Width:", None))
        self.passengers.setText(QCoreApplication.translate("MainWindow", u"Passengers:", None))
        self.currentMass.setText(QCoreApplication.translate("MainWindow", u"Current Mass: ", None))
    # retranslateUi
