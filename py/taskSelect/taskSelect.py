import sys

from py.FirstTask.FirstSlide import firstWindow

from PySide6.QtWidgets import QApplication, QMainWindow
from ui.taskSelect.ui_taskSelect import Ui_MainWindow

class New(QMainWindow):
    def __init__(self):
        super(New, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def btn_two_clicked(self):
        self.ui = firstWindow.Ui_MainWindow
        self.ui.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = New()
    window.show()
    sys.exit(app.exec())