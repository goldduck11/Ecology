import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from ui.FirstTask.FirstSlide.ui_firstSlide import Ui_MainWindow


class MyFirstWindow(QMainWindow):
	def __init__(self):
		super(MyFirstWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.show()

