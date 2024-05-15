import math

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox

from data import tab_2, tab_3, tab_б, tab_г
from py.PropertyFile.PropertySelection import PropertySelection
from py.SecondTask.ui_firstSlide import FirstSlide
from ui.SecondTask.ui_B import Ui_MainWindow


class B(QMainWindow):
    variant_number: str
    text: str
    alfa0: int
    m: int
    B: float
    def __init__(self):
        super(B, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label_8.hide()
        self.ui.comboBox_3.hide()
        self.ui.label_9.hide()
        self.ui.label_10.hide()

        self.ui.pushButton.clicked.connect(self.continueTask)
        self.ui.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.ui.comboBox_2.currentIndexChanged.connect(self.on_combobox_changed)
        self.ui.comboBox_3.currentIndexChanged.connect(self.on_combobox_changed)

    @Slot(int)
    def on_combobox_changed(self, index):
        gerts = self.ui.comboBox.currentText()
        selected_value2 = self.ui.comboBox_2.currentIndex()
        selected_value3 = self.ui.comboBox_3.currentText()
        if 2000 <= int(gerts) <= 8000:
            self.ui.label_8.show()
            self.ui.comboBox_3.show()
            self.ui.label_9.show()
            self.ui.label_10.show()
        else:
            self.ui.label_8.hide()
            self.ui.comboBox_3.hide()
            self.ui.label_9.hide()
            self.ui.label_10.hide()
        if selected_value2 != 0:
            self.ui.label_7.setText(str(tab_2[int(gerts)][selected_value2 - 1]))
            self.alfa0 = tab_2[int(gerts)][selected_value2 - 1]
        if selected_value3 != '':
            if gerts == '63':
                gerts = '125'
            self.ui.label_10.setText(str(tab_3[int(gerts)][int(selected_value3)]))
            self.m = tab_3[int(gerts)][int(selected_value3)]

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

        gerts = self.ui.comboBox.currentText()
        alfa = 0
        length = tab_г.iloc[0, self.variant_number]  # Длина соответствующая частоте variant_numberant_number
        height = tab_г.iloc[1, self.variant_number]  # Высота соответствующая частоте variant_number
        length_value = tab_б.iloc[0, self.variant_number]  # Длина соответствующая частоте variant_number
        width_value = tab_б.iloc[1, self.variant_number]  # Ширина соответствующая частоте variant_number
        height_value = tab_б.iloc[2, self.variant_number]  # Высота соответствующая частоте variant_number

        # Вычислите значение self.S используя полученные данные
        self.S = 2 * length_value * width_value + 2 * width_value * height_value + 2 * length_value * height_value
        S = length * height
        P.set_Sorg(S)
        if 63 <= int(gerts) <= 1000:
            alfa = self.alfa0
        elif 2000 <= int(gerts) <= 8000:
            V = tab_б[0, self.variant_number] * tab_б[1, self.variant_number] * tab_б[2, self.variant_number]
            l_cr = 4 * V / S
            alfa = 1 - (1 - self.alfa0) * math.pow(math.e, -1 * self.m * l_cr)

        self.B = self.S * alfa/(1 - alfa)
        P.set_s(self.S)
        P.set_Gerts(gerts)

        if round(self.B, 2) == round(float(self.text.replace(",", ".")), 2):
            PropertySelection().set_B(self.B)
            self.newWindow = FirstSlide()
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