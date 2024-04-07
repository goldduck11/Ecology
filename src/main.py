import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from src.view.taskSelect import Ui_MainWindow
from src.view.ChooseOptionForm import ChooseOptionUi


class view(QMainWindow):
    def __init__(self):
        super(view, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = view()
    window.show()

    sys.exit(app.exec())
