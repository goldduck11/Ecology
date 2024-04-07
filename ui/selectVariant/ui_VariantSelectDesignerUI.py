# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VariantSelectDesignerUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QComboBox, QLabel, QMenuBar, QPushButton, QStatusBar,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.VariantTextField = QLabel(self.centralwidget)
        self.VariantTextField.setObjectName(u"VariantTextField")
        self.VariantTextField.setGeometry(QRect(190, 130, 231, 31))
        font = QFont()
        font.setPointSize(15)
        self.VariantTextField.setFont(font)
        self.VariantSelectButton = QPushButton(self.centralwidget)
        self.VariantSelectButton.setObjectName(u"VariantSelectButton")
        self.VariantSelectButton.setGeometry(QRect(260, 220, 91, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.VariantSelectButton.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 631, 61))
        font2 = QFont()
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.BoxSelectVariant = QComboBox(self.centralwidget)
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.addItem("")
        self.BoxSelectVariant.setObjectName(u"BoxSelectVariant")
        self.BoxSelectVariant.setGeometry(QRect(260, 170, 91, 41))
        self.BoxSelectVariant.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.VariantTextField.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0432\u043e\u0439 \u0432\u0430\u0440\u0438\u0430\u043d\u0442", None))
        self.VariantSelectButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0410\u0421\u0427\u0401\u0422 \u0418 \u041f\u0420\u041e\u0415\u041a\u0422\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u0415 \u0421\u0420\u0415\u0414\u0421\u0422\u0412 \u0417\u0410\u0429\u0418\u0422\u042b \u041e\u0422 \u0428\u0423\u041c\u0410", None))
        self.BoxSelectVariant.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.BoxSelectVariant.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.BoxSelectVariant.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.BoxSelectVariant.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.BoxSelectVariant.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.BoxSelectVariant.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.BoxSelectVariant.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.BoxSelectVariant.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.BoxSelectVariant.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.BoxSelectVariant.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

    # retranslateUi

