import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from py.SecondTask.ui_B import B
from ui.taskSelect.ui_taskSelect import Ui_MainWindow
from py.FirstTask.FirstSlide.firstWindow import firstSlide
from py.SecondTask.ui_firstSlide import FirstSlide


class New(QMainWindow):
    def __init__(self):
        super(New, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.task_1.clicked.connect(self.first_task)
        self.ui.task_2.clicked.connect(self.second_task)

    def first_task(self):
        self.new_window = firstSlide()
        self.new_window.show()
        self.destroy()

    def second_task(self):
        self.new_window = B()
        self.new_window.show()
        self.destroy()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = New()
    window.show()
    sys.exit(app.exec())