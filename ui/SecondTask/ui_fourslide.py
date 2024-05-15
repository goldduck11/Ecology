# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fourslide.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 300, 101, 41))
        font = QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 310, 451, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.lineEdit.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 140, 371, 111))
        self.label.setPixmap(QPixmap(u"../../image/secondTask/secondFormyla.png"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 310, 151, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 761, 71))
        self.label_3.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setKerning(False)
        self.label_3.setFont(font2)
        self.label_3.setLineWidth(0)
        self.label_3.setMidLineWidth(0)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setMargin(0)
        self.label_3.setIndent(-1)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 340, 271, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442:", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0437\u0432\u0443\u043a\u043e\u0438\u0437\u043e\u043b\u044f\u0446\u0438\u044e \u043f\u0440\u043e\u0435\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u043e\u0433\u043e \u043e\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u044f</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442 \u043e\u043a\u0440\u0443\u0433\u043b\u0438\u0442\u044c \u0434\u043e 2-\u0445 \u0437\u043d\u0430\u043a\u043e\u0432 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439.", None))
    # retranslateUi

