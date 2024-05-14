import math
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from py.PropertyFile.PropertySelection import PropertySelection
from ui.FirstTask.FourthSlide.ui_fourthSlide import Ui_MainWindow

from data import tab_4_plus, tab_4_minus


class MyFirstWindow(QMainWindow):
	text: str
	gerts: str
	Lp: float
	units: int
	docade: int
	L: float

	def __init__(self):
		super(MyFirstWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.show()
		self.ui.pushButton.clicked.connect(self.continueTask)

	def extract_integer_part(self, num):
		# Преобразуем число в строку
		num_str = str(num)

		# Находим позицию десятичной точки
		decimal_position = num_str.find('.')

		if decimal_position != -1:
			# Если десятичная точка найдена
			integer_part = num_str[:decimal_position - 1]  # Извлекаем все символы до десятичной точки

			# Преобразуем извлеченную целую часть в целое число
			if integer_part.isdigit():
				new_number = int(integer_part)
				единицы = int(num_str[decimal_position - 1])
				return new_number, единицы
			else:
				return None  # Если в извлеченной целой части есть символы кроме цифр, возвращаем None
		else:
			integer_part = num_str[:-1]  # Извлекаем все символы до десятичной точки

			# Преобразуем извлеченную целую часть в целое число
			if integer_part.isdigit():
				new_number = int(integer_part)
				единицы = int(num_str[-1:])
				return new_number, единицы
			else:
				return None  # Если в извлеченной целой части есть символы кроме цифр, возвращаем None

	def continueTask(self):
		self.text = self.ui.lineEdit.text()
		P = PropertySelection()
		self.Lp = P.get_Lp()
		self.docade, self.units = self.extract_integer_part(self.Lp)
		print(tab_4_plus.iloc[self.docade, self.units])
		self.L = self.Lp + 10 * math.log10(
			tab_4_plus.iloc[self.docade, self.units] * ((1.2 / 8 * math.pi) + (1.1 / 18 * math.pi) + (1.0 / 32 * math.pi)) + (
						4 * 3 / P.get_B()))
		print(round(self.L, 2))
		if (round(self.L, 2) != round(float(self.text.replace(",", ".")), 2)):
			self.msg = QMessageBox()
			self.msg.setIcon(QMessageBox.Icon.Critical)
			self.msg.setText("Ошибка!")
			self.msg.setInformativeText("Был введён неверный ответ")  # Установка информационного текста
			self.msg.setWindowTitle("Ошибка")
			self.msg.setFixedWidth(400)
			self.msg.exec()  # Показываем QMessageBox
			return

		print("Верный вариант 3")
