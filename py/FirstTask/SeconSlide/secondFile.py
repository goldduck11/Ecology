import math
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from py.FirstTask.ThirdSlide import thirdWIndow
from py.PropertyFile.PropertySelection import PropertySelection
from ui.FirstTask.FirstSlide.ui_firstSlide import Ui_MainWindow


from data import tab_а


class secondSlide(QMainWindow):
	X: float
	text: str
	L: float
	Lp: float

	def __init__(self):
		super(secondSlide, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.label.setPixmap(QPixmap("../../image/firstTask/firstSlide/photo_2024-05-15_21-24-20.jpg"))

		self.ui.continueButton.clicked.connect(self.continueTask)

	def continueTask(self):
		self.X = float(self.ui.lineEdit_2.text())
		self.text = self.ui.lineEdit.text()
		P = PropertySelection()
		if (self.X == None):
			self.msg = QMessageBox()
			self.msg.setIcon(QMessageBox.Critical)
			self.msg.setText("Ошибка!")
			self.msg.setInformativeText("Поле 'X' должно быть заполнено!")  # Установка информационного текста
			self.msg.setWindowTitle("Ошибка")
			self.msg.setFixedWidth(400)
			self.msg.exec()  # Показываем QMessageBox
			return
		gerts_index = int(P.get_Gerts())  # Получаем индекс строки в виде числа
		variant_index = int(P.get_Variant())  # Получаем числовой индекс столбца
		if gerts_index in tab_а.columns and variant_index in tab_а.index:
			print(tab_а.loc[variant_index, gerts_index])
			self.Lp = tab_а.loc[variant_index, gerts_index]
			self.L = self.Lp + 10 * math.log10(
				(self.X * 1 / (2 * math.pi * math.pow(2, 2))) + (4 / P.get_B()))
			print(self.L)
		else:
			print("Ошибка: Некорректные индексы строк или столбцов")
		if (round(self.L, 2) != round(float(self.text.replace(",", ".")), 2)):
			self.msg = QMessageBox()
			self.msg.setIcon(QMessageBox.Critical)
			self.msg.setText("Ошибка!")
			self.msg.setInformativeText("Неверный ответ!")  # Установка информационного текста
			self.msg.setWindowTitle("Ошибка")
			self.msg.setFixedWidth(400)
			self.msg.exec()  # Показываем QMessageBox
			return
		P.set_Lp(self.Lp)
		self.destroy()
		self.newWindow = thirdWIndow.thirdSlide()
		self.newWindow.show()
		print("Правильный ответ!")