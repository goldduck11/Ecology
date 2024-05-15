from PySide6.QtWidgets import QMainWindow, QMessageBox

from ui.SecondTask.ui_fourslide import Ui_MainWindow

from py.PropertyFile.PropertySelection import PropertySelection


class FourSlide(QMainWindow):
    def __init__(self):
        super(FourSlide, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.continueTask)

    def continueTask(self):
        self.text = str(self.ui.lineEdit.text())
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
        self.variant_number = int(P.get_Variant()) - 1

        R = round(P.get_R(), 2)
        R1 = round(P.get_R1(), 2)
        R0 = round(P.get_R0(), 2)

        Rorg = R + R1 - R0

        if round(Rorg, 2) == round(float(self.text.replace(",", ".")), 2):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setInformativeText("Вы успешно прошли тестирование!")  # Установка информационного текста
            self.msg.setWindowTitle("Поздравляем")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ошибка!")
            self.msg.setInformativeText("Неверный ответ!")  # Установка информационного текста
            self.msg.setWindowTitle("Ошибка")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox