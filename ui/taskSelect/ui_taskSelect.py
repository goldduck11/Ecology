# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskSelect.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.task_selection_lable = QLabel(self.centralwidget)
        self.task_selection_lable.setObjectName(u"task_selection_lable")
        self.task_selection_lable.setGeometry(QRect(40, 40, 561, 91))
        font = QFont()
        font.setPointSize(20)
        self.task_selection_lable.setFont(font)
        self.task_1 = QPushButton(self.centralwidget)
        self.task_1.setObjectName(u"task_1")
        self.task_1.setGeometry(QRect(220, 150, 181, 31))
        self.task_2 = QPushButton(self.centralwidget)
        self.task_2.setObjectName(u"task_2")
        self.task_2.setGeometry(QRect(220, 220, 181, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0438 \u043f\u0440\u043e\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432 \u0437\u0430\u0449\u0438\u0442\u044b \u043e\u0442 \u0448\u0443\u043c\u0430", None))
        self.task_selection_lable.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0437\u0430\u043d\u044f\u0442\u0438\u0439", None))
        self.task_1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 1", None))
        self.task_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 2", None))
    # retranslateUi

