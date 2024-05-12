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
	Lp: str
	units: int
	docade: int

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
			# Если десятичная точка не найдена, возвращаем само число как целое число
			return int(num)

	def continueTask(self):
		self.text = self.ui.lineEdit.text()
		P = PropertySelection()
		self.Lp = P.get_Lp()
		self.docade, self.units = self.extract_integer_part(self.Lp)
		for i in range(1, 4):
			if (self.Lp > 0):




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyFirstWindow()
    window.show()
    sys.exit(app.exec())



