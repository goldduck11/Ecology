import math

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox

from data import tab_6
from py.PropertyFile.PropertySelection import PropertySelection
from py.SecondTask.ui_threeSlide import threeSlide
from ui.SecondTask.ui_secondSlide import Ui_MainWindow


class secondSlide(QMainWindow):
    betta: float
    def __init__(self):
        super(secondSlide, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.continueTask)
        self.ui.comboBox_2.currentIndexChanged.connect(self.on_combobox_changed)

    @Slot(int)
    def on_combobox_changed(self, index):
        gerts = PropertySelection().get_Gerts()
        selected_value = self.ui.comboBox_2.currentIndex()
        if selected_value == 0: return
        self.betta = tab_6[int(gerts)][selected_value - 1]
        self.ui.label_7.setText(str(self.betta))

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

        m_n = self.ui.lineEdit_4.text()
        if not m_n:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ошибка!")
            self.msg.setInformativeText(
                "Поле 'Поверхностная плотность материала ограждения' должно быть заполнено!")  # Установка информационного текста
            self.msg.setWindowTitle("Ошибка")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox
            return

        if m_n.isdigit() == False:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ошибка!")
            self.msg.setInformativeText(
                "Поле 'Поверхностная плотность материала ограждения' некорректно заполнено!")  # Установка информационного текста
            self.msg.setWindowTitle("Ошибка")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox
            return

        m_nc = self.ui.lineEdit_3.text()
        if not m_nc:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ошибка!")
            self.msg.setInformativeText(
                "Поле 'Поверхностная плотность звукопоглощающего материала' должно быть заполнено!")  # Установка информационного текста
            self.msg.setWindowTitle("Ошибка")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox
            return

        if m_nc.isdigit() == False:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ошибка!")
            self.msg.setInformativeText(
                "Поле 'Поверхностная плотность звукопоглощающего материала' некорректно заполнено!")  # Установка информационного текста
            self.msg.setWindowTitle("Ошибка")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox
            return

        omega = float(self.ui.lineEdit_2.text().replace(",", "."))
        if not omega:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ошибка!")
            self.msg.setInformativeText(
                "Поле 'Толщина слоя ЗПМ в мм' должно быть заполнено!")  # Установка информационного текста
            self.msg.setWindowTitle("Ошибка")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox
            return

        R1 = 8.7 * float(self.betta) * float(omega) + 20 * math.log10((float(m_n) + float(m_nc)) / float(m_n))

        P.set_R1(R1)

        if round(R1, 2) == round(float(self.text.replace(",", ".")), 2):
            self.newWindow = threeSlide()
            self.newWindow.show()
            self.destroy()
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Ошибка!")
            self.msg.setInformativeText("Неверный ответ!")  # Установка информационного текста
            self.msg.setWindowTitle("Ошибка")
            self.msg.setFixedWidth(400)
            self.msg.exec()  # Показываем QMessageBox