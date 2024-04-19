import sys
from py.FirstTask.FirstSlide import firstWindow

from PySide6.QtWidgets import QApplication, QMainWindow

from py.PropertyFile.PropertySelection import PropertySelection
from ui.selectVariant.ui_VariantSelectDesignerUI import Ui_MainWindow

class MyWindow(QMainWindow):
    textVariant: str
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.VariantSelectButton.clicked.connect(self.select_variant)

    def select_variant(self):
        self.textVariant = str(self.ui.BoxSelectVariant.currentText())
        p = PropertySelection().set_Variant(self.textVariant)
        firstWindow.MyFirstWindow()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


