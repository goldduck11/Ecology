import math
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from py.FirstTask.SeconSlide import secondFile
from py.PropertyFile.PropertySelection import PropertySelection
from ui.FirstTask.ThirdSlide.ui_thirdSlide import Ui_MainWindow

from data import tab_б, tab_2, tab_3


class MyFirstWindow(QMainWindow):
	text: str
	gerts: str
	B: float
	S: float
	alfa: float

	def __init__(self):
		super(MyFirstWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.show()
		self.ui.pushButton.clicked.connect(self.continueTask)

	def continueTask(self):
		self.text = str(self.ui.lineEdit.text())
		self.gerts = str(self.ui.comboBox.currentText())
		self.otn = str(self.ui.lineEdit_2.text())
		P = PropertySelection()
		if not self.text:
			self.msg = QMessageBox()
			self.msg.setIcon(QMessageBox.Critical)
			self.msg.setText("Ошибка!")
			self.msg.setInformativeText("Поле 'Ответ' должно быть заполнено!")  # Установка информационного текста
			self.msg.setWindowTitle("Ошибка")
			self.msg.setFixedWidth(400)
			self.msg.exec()  # Показываем QMessageBox
			return
		variant_number = int(P.get_Variant()) - 1

		# Проверьте, что variant_number является допустимым индексом столбца в DataFrame tab_б
		if variant_number + 1 in tab_б.columns:
			# Используйте .iloc[] для доступа к данным с использованием числовых индексов столбцов
			length_value = tab_б.iloc[0, variant_number]  # Длина соответствующая частоте variant_number
			width_value = tab_б.iloc[1, variant_number]  # Ширина соответствующая частоте variant_number
			height_value = tab_б.iloc[2, variant_number]  # Высота соответствующая частоте variant_number

			# Вычислите значение self.S используя полученные данные
			self.S = 2 * length_value * width_value + 2 * width_value * height_value + 2 * length_value * height_value
		else:
			print(f"Ошибка: Частота {variant_number} не найдена в столбцах DataFrame tab_б")
		if (int(self.gerts) <= 1000):
			self.alfa = tab_2.iloc[2, tab_2.columns.get_loc(int(self.gerts))]
			self.B = self.S * self.alfa / (1 - self.alfa)
		else:
			if (self.otn == None):
				self.msg = QMessageBox()
				self.msg.setIcon(QMessageBox.Critical)
				self.msg.setText("Ошибка!")
				self.msg.setInformativeText("Поле 'Влажность' должно быть заполнено!")
				self.msg.setWindowTitle("Ошибка")
				self.msg.setFixedWidth(400)
				self.msg.exec()  # Показываем QMessageBox
				return
			self.V = tab_б[P.get_Variant()].loc['длина'] * tab_б[P.get_Variant()].loc[
				'ширина'] * tab_б[P.get_Variant()].loc['высота']
			self.alfa = 1 - (1 - tab_2.iloc[2, tab_2.columns.get_loc(int(self.gerts))]) * math.pow(math.e, -tab_3.loc[
				self.otn, self.gerts] * (4 * self.V / self.S))
			self.B = self.S * self.alfa / (1 - self.alfa)
		if (round(self.B, 2) != round(float(self.text.replace(",", ".")), 2)):
			self.msg = QMessageBox()
			self.msg.setIcon(QMessageBox.Icon.Critical)
			self.msg.setText("Ошибка!")
			self.msg.setInformativeText("Был введён неверный ответ")  # Установка информационного текста
			self.msg.setWindowTitle("Ошибка")
			self.msg.setFixedWidth(400)
			self.msg.exec()  # Показываем QMessageBox
			return
		P.set_B(self.B)
		P.set_Gerts(self.gerts)
		P.set_Sogr(self.S)
		P.set_Alfa(self.alfa)
		self.destroy()
		self.msg = QMessageBox()
		self.msg.setIcon(QMessageBox.Icon.Information)
		self.msg.setText("Будьте внимательны!")
		self.msg.setInformativeText("Ответ был округлён до двух знаков после замятой!")
		self.msg.setWindowTitle("Ошибка")
		self.msg.setFixedWidth(400)
		self.msg.exec()
		self.newWindow = secondFile.MyFirstWindow()
		self.newWindow.show()
