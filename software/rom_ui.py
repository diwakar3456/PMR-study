# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_fileQNMhXV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_Romiumetry(object):
    def setupUi(self, Romiumetry):
        if not Romiumetry.objectName():
            Romiumetry.setObjectName(u"Romiumetry")
        Romiumetry.resize(1109, 643)
        Romiumetry.setStyleSheet(u"background-color: rgb(91, 91, 91);\n"
"")
        self.centralwidget = QWidget(Romiumetry)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushbuttonstop = QPushButton(self.centralwidget)
        self.pushbuttonstop.setObjectName(u"pushbuttonstop")
        self.pushbuttonstop.setGeometry(QRect(830, 460, 229, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushbuttonstop.setFont(font)
        self.pushbuttonstop.setStyleSheet(u"color: rgb(128, 102, 157);\n"
"background-color: rgb(243, 221, 255);\n"
"border-radius: 8px;")
        self.pushbuttoncalibrate = QPushButton(self.centralwidget)
        self.pushbuttoncalibrate.setObjectName(u"pushbuttoncalibrate")
        self.pushbuttoncalibrate.setGeometry(QRect(830, 510, 229, 41))
        self.pushbuttoncalibrate.setFont(font)
        self.pushbuttoncalibrate.setStyleSheet(u"color: rgb(128, 102, 157);\n"
"background-color: rgb(243, 221, 255);\n"
"border-radius: 8px;")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 10, 751, 541))
        self.pushbuttonstart = QPushButton(self.centralwidget)
        self.pushbuttonstart.setObjectName(u"pushbuttonstart")
        self.pushbuttonstart.setGeometry(QRect(830, 410, 229, 41))
        self.pushbuttonstart.setFont(font)
        self.pushbuttonstart.setStyleSheet(u"color: rgb(128, 102, 157);\n"
"background-color: rgb(243, 221, 255);\n"
"border-radius: 8px;")
        self.circularProgressBarbase = QFrame(self.centralwidget)
        self.circularProgressBarbase.setObjectName(u"circularProgressBarbase")
        self.circularProgressBarbase.setGeometry(QRect(780, 40, 320, 320))
        self.circularProgressBarbase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarbase.setFrameShadow(QFrame.Raised)
        self.circularprogress = QFrame(self.circularProgressBarbase)
        self.circularprogress.setObjectName(u"circularprogress")
        self.circularprogress.setGeometry(QRect(0, 0, 300, 300))
        self.circularprogress.setStyleSheet(u"QFrame{\n"
"	border-radius:150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 255, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularprogress.setFrameShape(QFrame.NoFrame)
        self.circularprogress.setFrameShadow(QFrame.Raised)
        self.circularbg = QFrame(self.circularProgressBarbase)
        self.circularbg.setObjectName(u"circularbg")
        self.circularbg.setGeometry(QRect(1, 0, 300, 300))
        self.circularbg.setStyleSheet(u"QFrame{\n"
"border-radius:150px;\n"
"	background-color: rgba(77, 77, 127,120);\n"
"}")
        self.circularbg.setFrameShape(QFrame.NoFrame)
        self.circularbg.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.circularProgressBarbase)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(15, 15, 270, 270))
        self.frame.setStyleSheet(u"QFrame{\n"
"border-radius: 135px;\n"
"background-color: rgb(77, 77, 127);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.labeltitle = QLabel(self.frame)
        self.labeltitle.setObjectName(u"labeltitle")
        self.labeltitle.setGeometry(QRect(80, 30, 118, 25))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.labeltitle.setFont(font1)
        self.labeltitle.setStyleSheet(u"background-color:none;\n"
"color: rgb(247, 240, 49);")
        self.labeltitle.setAlignment(Qt.AlignCenter)
        self.labelangle = QLabel(self.frame)
        self.labelangle.setObjectName(u"labelangle")
        self.labelangle.setGeometry(QRect(50, 100, 170, 71))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(48)
        self.labelangle.setFont(font2)
        self.labelangle.setStyleSheet(u"background-color:none;\n"
"color: rgb(76, 227, 111);")
        self.labelangle.setAlignment(Qt.AlignCenter)
        self.labeljoint = QLabel(self.frame)
        self.labeljoint.setObjectName(u"labeljoint")
        self.labeljoint.setGeometry(QRect(120, 60, 42, 25))
        self.labeljoint.setFont(font1)
        self.labeljoint.setStyleSheet(u"background-color:none;\n"
"color: rgb(143, 174, 235);")
        self.labeljoint.setAlignment(Qt.AlignCenter)
        self.labelmovement = QLabel(self.frame)
        self.labelmovement.setObjectName(u"labelmovement")
        self.labelmovement.setGeometry(QRect(50, 200, 171, 25))
        self.labelmovement.setFont(font1)
        self.labelmovement.setStyleSheet(u"background-color:none;\n"
"color: rgb(255, 123, 123);")
        self.labelmovement.setAlignment(Qt.AlignCenter)
        self.circularbg.raise_()
        self.circularprogress.raise_()
        self.frame.raise_()
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 580, 731, 41))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(125, 125, 125);")

        self.horizontalLayout.addWidget(self.label_6)

        self.lineedithospitalnumber = QLineEdit(self.widget)
        self.lineedithospitalnumber.setObjectName(u"lineedithospitalnumber")
        self.lineedithospitalnumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout.addWidget(self.lineedithospitalnumber)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(125, 125, 125);")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineeditmovement = QLineEdit(self.widget)
        self.lineeditmovement.setObjectName(u"lineeditmovement")
        self.lineeditmovement.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_5.addWidget(self.lineeditmovement)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(125, 125, 125);")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineeditjoint = QLineEdit(self.widget)
        self.lineeditjoint.setObjectName(u"lineeditjoint")
        self.lineeditjoint.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_4.addWidget(self.lineeditjoint)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        Romiumetry.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Romiumetry)
        self.statusbar.setObjectName(u"statusbar")
        Romiumetry.setStatusBar(self.statusbar)

        self.retranslateUi(Romiumetry)

        QMetaObject.connectSlotsByName(Romiumetry)
    # setupUi

    def retranslateUi(self, Romiumetry):
        Romiumetry.setWindowTitle(QCoreApplication.translate("Romiumetry", u"MainWindow", None))
        self.pushbuttonstop.setText(QCoreApplication.translate("Romiumetry", u"Stop Assessment", None))
        self.pushbuttoncalibrate.setText(QCoreApplication.translate("Romiumetry", u"Calibrate", None))
        self.pushbuttonstart.setText(QCoreApplication.translate("Romiumetry", u"Start Assessment", None))
        self.labeltitle.setText(QCoreApplication.translate("Romiumetry", u"ROMIUMETER", None))
        self.labelangle.setText(QCoreApplication.translate("Romiumetry", u"90", None))
        self.labeljoint.setText(QCoreApplication.translate("Romiumetry", u"Neck", None))
        self.labelmovement.setText(QCoreApplication.translate("Romiumetry", u"Right Lateral Flexion", None))
        self.label_6.setText(QCoreApplication.translate("Romiumetry", u"Hospital Number:", None))
        self.label_5.setText(QCoreApplication.translate("Romiumetry", u"Movement:", None))
        self.label_4.setText(QCoreApplication.translate("Romiumetry", u"Joint:", None))
    # retranslateUi

