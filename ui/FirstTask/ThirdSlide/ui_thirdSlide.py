# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thirdSlide.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 360, 451, 31))
        font = QFont()
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 350, 101, 41))
        self.label_2.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(640, 360, 111, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(520, 250, 91, 31))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"")
        self.comboBox.setMinimumContentsLength(0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 240, 101, 41))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 300, 131, 41))
        self.label_4.setFont(font)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 310, 451, 31))
        self.lineEdit_2.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 130, 231, 71))
        self.label.setPixmap(QPixmap(u"../../../image/firstTask/thirdSlide/thirdImage.png"))
        self.label.setScaledContents(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043e \u0434\u043e \u0434\u0432\u0443\u0445 \u0437\u043d\u0430\u043a\u043e\u0432 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"63", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"125", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"250", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"500", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"1000", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"2000", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"4000", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"8000", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0446:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.label.setText("")
    # retranslateUi

