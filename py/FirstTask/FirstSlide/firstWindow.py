import math
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from py.PropertyFile.PropertySelection import PropertySelection
from ui.FirstTask.FirstSlide.ui_firstSlide import Ui_MainWindow

from data import tab_а


class MyFirstWindow(QMainWindow):
	text: str
	gerts: str

	def __init__(self):
		super(MyFirstWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.show()
		self.ui.continueButton.clicked.connect(self.continueTask)

	def continueTask(self):
		self.text = str(self.ui.lineEdit.text())
		self.gerts = str(self.ui.comboBox.currentText())
		if not self.text:
			self.msg = QMessageBox()
			self.msg.setIcon(QMessageBox.Critical)
			self.msg.setText("Ошибка!")
			self.msg.setInformativeText("Поле 'Ответ' должно быть заполнено!")  # Установка информационного текста
			self.msg.setWindowTitle("Ошибка")
			self.msg.setMaximumWidth(400)
			self.msg.exec()  # Показываем QMessageBox
			return
		self.s = tab_а.loc[PropertySelection.get_Variant()][self.gerts] + 10 * math.log10()
