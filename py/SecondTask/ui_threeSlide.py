from PySide6.QtWidgets import QMainWindow

from ui.SecondTask.ui_threeSlide import Ui_MainWindow


class threeSlide(QMainWindow):
    def __init__(self):
        super(threeSlide, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)