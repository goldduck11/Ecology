# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'B.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(846, 559)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 70, 341, 81))
        self.label.setPixmap(QPixmap(u"../../image/secondTask/B.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 491, 31))
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 190, 441, 31))
        self.lineEdit.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 180, 101, 41))
        font1 = QFont()
        font1.setPointSize(17)
        self.label_3.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(660, 190, 151, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(680, 130, 101, 41))
        self.label_4.setFont(font1)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(720, 140, 91, 31))
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet(u"")
        self.comboBox.setMinimumContentsLength(0)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 250, 181, 41))
        self.label_5.setFont(font1)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(190, 260, 641, 131))
        self.comboBox_2.setFont(font1)
        self.comboBox_2.setStyleSheet(u"")
        self.comboBox_2.setMinimumContentsLength(0)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 390, 451, 61))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(460, 400, 41, 31))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 440, 381, 41))
        self.label_8.setFont(font1)
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(390, 450, 91, 31))
        self.comboBox_3.setFont(font1)
        self.comboBox_3.setStyleSheet(u"")
        self.comboBox_3.setMinimumContentsLength(0)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 480, 661, 41))
        self.label_9.setFont(font1)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(670, 480, 101, 41))
        self.label_10.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u043f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u0443\u044e \u0438\u0437\u043e\u043b\u0438\u0440\u0443\u0435\u043c\u043e\u0433\u043e \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0446:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"63", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"125", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"250", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"500", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"1000", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"2000", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"4000", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f:", None))
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0448\u0438\u043d\u043d\u044b\u0435 \u0437\u0430\u043b\u044b, \u0433\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0435, \u0438\u0441\u043f\u044b\u0442\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0435\u043d\u0434\u044b,\n"
"\u0432\u0435\u043d\u0442\u0438\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u043a\u0430\u043c\u0435\u0440\u044b, \u0446\u0435\u0445\u0438 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0439 \u043f\u0438\u0449\u0435\u0432\u043e\u0439\n"
"\u043f\u0440\u043e\u043c\u044b\u0448\u043b\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u0441 \u043e\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u044f\u043c\u0438,\n"
"\u043e\u0431\u043b\u0438\u0446\u043e\u0432\u0430\u043d\u043d\u044b\u043c\u0438 \u043c\u043e\u044e\u0449\u0435\u0439\u0441\u044f \u043f\u043b\u0438\u0442\u043a\u043e\u0439.", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0438 \u043c\u0435\u0442\u0430\u043b\u043b\u043e\u043e\u0431\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u044e\u0449\u0438\u0435 \u0446\u0435\u0445\u0438; \n"
"\u0446\u0435\u0445\u0438 \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043d\u043e\u0439 \u0441\u0431\u043e\u0440\u043a\u0438 \u0432 \u0430\u0432\u0438\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u0438\n"
"\u0441\u0443\u0434\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u043e\u043c\u044b\u0448\u043b\u0435\u043d\u043d\u043e\u0441\u0442\u0438", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0426\u0435\u0445\u0438 \u0434\u0435\u0440\u0435\u0432\u043e\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0438 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0439\n"
"\u0442\u0435\u043a\u0441\u0442\u0438\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u043e\u043c\u044b\u0448\u043b\u0435\u043d\u043d\u043e\u0441\u0442\u0438; \u043f\u043e\u0441\u0442\u044b \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f;\n"
"\u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u0439; \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440\u0441\u043a\u0438\u0435 \u0431\u044e\u0440\u043e; \n"
"\u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0439.", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0437\u0432\u0443\u043a\u043e\u043f\u043e\u0433\u043b\u043e\u0449\u0435\u043d\u0438\u044f:", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0432\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c \u0432\u043e\u0437\u0434\u0443\u0445\u0430:", None))
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"35", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"40", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"45", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"55", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"60", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"65", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"70", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("MainWindow", u"75", None))
        self.comboBox_3.setItemText(11, QCoreApplication.translate("MainWindow", u"80", None))
        self.comboBox_3.setItemText(12, QCoreApplication.translate("MainWindow", u"90", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c \u0437\u0430\u0442\u0443\u0445\u0430\u043d\u0438\u044f \u0437\u0432\u0443\u043a\u0430 \u0432 \u0432\u043e\u0437\u0434\u0443\u0445\u0435 \u043d\u0430 \u0435\u0434\u0438\u043d\u0438\u0446\u0443 \u0434\u043b\u0438\u043d\u044b, 1/\u043c:", None))
        self.label_10.setText("")
    # retranslateUi

