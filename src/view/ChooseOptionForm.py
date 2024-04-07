# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChooseOptionForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class ChooseOptionUi(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.VariantTextField = QLabel(self.centralwidget)
        self.VariantTextField.setObjectName(u"VariantTextField")
        self.VariantTextField.setGeometry(QRect(200, 110, 231, 31))
        font = QFont()
        font.setPointSize(15)
        self.VariantTextField.setFont(font)
        self.VariantSelectButton = QPushButton(self.centralwidget)
        self.VariantSelectButton.setObjectName(u"VariantSelectButton")
        self.VariantSelectButton.setGeometry(QRect(260, 220, 91, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.VariantSelectButton.setFont(font1)
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0438 \u043f\u0440\u043e\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432 \u0437\u0430\u0449\u0438\u0442\u044b \u043e\u0442 \u0448\u0443\u043c\u0430", None))
        self.VariantTextField.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0432\u043e\u0439 \u0432\u0430\u0440\u0438\u0430\u043d\u0442", None))
        self.VariantSelectButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
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

