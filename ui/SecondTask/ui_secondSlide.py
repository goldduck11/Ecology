# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secondSlide.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 350, 101, 41))
        font = QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 360, 471, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.lineEdit.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 70, 551, 111))
        self.label.setPixmap(QPixmap(u"../../image/secondTask/threeFormyla.png"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 360, 151, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 300, 281, 41))
        self.label_4.setFont(font)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(290, 310, 201, 31))
        self.lineEdit_2.setFont(font1)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(370, 420, 381, 41))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet(u"")
        self.comboBox_2.setMinimumContentsLength(0)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 470, 321, 41))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 420, 341, 41))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(340, 480, 71, 31))
        self.label_7.setFont(font)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(640, 300, 131, 31))
        self.lineEdit_3.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 250, 641, 41))
        self.label_8.setFont(font)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(550, 210, 201, 31))
        self.lineEdit_4.setFont(font1)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 200, 541, 41))
        self.label_9.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 761, 71))
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
        self.label_10.setGeometry(QRect(110, 390, 271, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442:", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0441\u043b\u043e\u044f \u0417\u041f\u041c \u0432 \u043c\u043c:", None))
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0438\u0442\u044b \u043c\u0438\u043d\u0435\u0440\u0430\u043b\u043e\u0432\u0430\u0442\u043d\u044b\u0435 \u043d\u0430 \u0444\u0435\u043d\u043e\u043b\u044c\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u043a\u0435", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0425\u043e\u043b\u0441\u0442 \u0438\u0437 \u0441\u0443\u043f\u0435\u0440\u0442\u043e\u043d\u043a\u043e\u0433\u043e \u0441\u0442\u0435\u043a\u043b\u043e\u0432\u043e\u043b\u043e\u043a\u043d\u0430", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0425\u043e\u043b\u0441\u0442 \u0438\u0437 \u0441\u0443\u043f\u0435\u0440\u0442\u043e\u043d\u043a\u043e\u0433\u043e \u0431\u0430\u0437\u0430\u043b\u044c\u0442\u043e\u0432\u043e\u0433\u043e \u0432\u043e\u043b\u043e\u043a\u043d\u0430", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0410\u0422\u041c-1", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0438\u0443\u0440\u0438\u0442\u0430\u043d\u043e\u0432\u044b\u0439 \u044d\u043b\u0430\u0441\u0442\u0438\u0447\u043d\u044b\u0439 \u043f\u043e\u0440\u043e\u043f\u043b\u0430\u0441\u0442 \u043c\u0430\u0440\u043a\u0438 \u041f\u041f\u0423-\u042d\u0422", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0437\u0430\u0442\u0443\u0445\u0430\u043d\u0438\u044f, 1/\u043c:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0432\u0443\u043a\u043e\u043f\u043e\u0433\u043b\u043e\u0449\u0430\u044e\u0449\u0438\u0439 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b:", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u043d\u0430\u044f \u043f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u0437\u0432\u0443\u043a\u043e\u043f\u043e\u0433\u043b\u043e\u0449\u0430\u044e\u0449\u0435\u0433\u043e \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u043d\u0430\u044f \u043f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430 \u043e\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0434\u043e\u0431\u0430\u0432\u043e\u0447\u043d\u0443\u044e \u0437\u0432\u0443\u043a\u043e\u0438\u0437\u043e\u043b\u044f\u0446\u0438\u044e \u0437\u0430 \u0441\u0447\u0435\u0442 \u043d\u0430\u043d\u0435\u0441\u0435\u043d\u0438\u044f <br/>\u0441\u043b\u043e\u044f \u0437\u0432\u0443\u043a\u043e\u043f\u043e\u0433\u043b\u043e\u0449\u0430\u044e\u0449\u0435\u0433\u043e \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430 (\u0417\u041f\u041c)</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442 \u043e\u043a\u0440\u0443\u0433\u043b\u0438\u0442\u044c \u0434\u043e 2-\u0445 \u0437\u043d\u0430\u043a\u043e\u0432 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439.", None))
    # retranslateUi

