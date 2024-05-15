# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstslide.ui'
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
        self.label_2.setGeometry(QRect(40, 270, 101, 41))
        font = QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 280, 451, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.lineEdit.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 80, 501, 111))
        self.label.setPixmap(QPixmap(u"../../image/secondTask/firstFormyla.png"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(590, 280, 151, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 491, 61))
        self.label_3.setFont(font1)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem(u"\u041f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440\u0441\u043a\u0438\u0445 \u0431\u044e\u0440\u043e, \u0440\u0430\u0441\u0447\u0435\u0442\u0447\u0438\u043a\u043e\u0432,\n"
"\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442\u043e\u0432 \u0432\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043c\u0430\u0448\u0438\u043d,\n"
"\u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u0439 \u0434\u043b\u044f \u0442\u0435\u043e\u0440\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0440\u0430\u0431\u043e\u0442.")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(180, 350, 611, 91))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet(u"")
        self.comboBox_2.setMinimumContentsLength(0)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 340, 171, 41))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 460, 261, 41))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 460, 61, 41))
        self.label_7.setFont(font)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(120, 310, 271, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442:", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0442\u0440\u0435\u0431\u0443\u0435\u043c\u0443\u044e \u0437\u0432\u0443\u043a\u043e\u0438\u0437\u043e\u043b\u044f\u0446\u0438\u044e \u043e\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f, \u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u043a\u043e\u043c\u043d\u0430\u0442\u044b.", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0431\u0438\u043d\u044b \u043d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u0439 \u0438 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f\n"
"\u0431\u0435\u0437 \u0440\u0435\u0447\u0435\u0432\u043e\u0439 \u0441\u0432\u044f\u0437\u0438 \u043f\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0443.", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0431\u0438\u043d\u044b \u043d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u0439 \u0438 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f\n"
"\u0441 \u0440\u0435\u0447\u0435\u0432\u043e\u0439 \u0441\u0432\u044f\u0437\u0438 \u043f\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0443.", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u0438 \u0443\u0447\u0430\u0441\u0442\u043a\u0438 \u0442\u043e\u0447\u043d\u043e\u0439 \u0441\u0431\u043e\u0440\u043a\u0438,\n"
"\u043c\u0430\u0448\u0438\u043d\u043e\u043f\u0438\u0441\u043d\u044b\u0435 \u0431\u044e\u0440\u043e.", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u0439 \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f\n"
"\u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0445 \u0440\u0430\u0431\u043e\u0442, \u0434\u043b\u044f \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f \n"
"\u0448\u0443\u043c\u043d\u044b\u0445 \u0430\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0432, \u0432\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043c\u0430\u0448\u0438\u043d.", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u044b\u0435 \u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u043c\u0435\u0441\u0442\u0430 \u0438 \u0440\u0430\u0431\u043e\u0447\u0438\u0435 \u0437\u043e\u043d\u044b \u0432\n"
"\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f\u0445 \u0438 \u043d\u0430 \n"
"\u0442\u0435\u0440\u0440\u0438\u0442\u043e\u0440\u0438\u0438 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044f.", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0435\u0435 \u043c\u0435\u0441\u0442\u043e:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0446 \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u043c\u0435\u0441\u0442\u0430:", None))
        self.label_7.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442 \u043e\u043a\u0440\u0443\u0433\u043b\u0438\u0442\u044c \u0434\u043e 2-\u0445 \u0437\u043d\u0430\u043a\u043e\u0432 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439.", None))
    # retranslateUi

