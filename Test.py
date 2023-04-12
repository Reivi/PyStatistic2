import sys
from math import log

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QGridLayout,
    QHBoxLayout, QApplication,
    QTabWidget, QPushButton, QGroupBox, QLabel, QTableWidget, QSpinBox, QTableWidgetItem
)
# pyuic5 loadUi.ui -o loadUi.py

class Welcome(QGroupBox):  # - QWidget
    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)

        self.setStyleSheet('background-color: #aaf5f5;')
        self.setTitle("&Обработка данных")

        self.grid_layout = QGridLayout(self)
        self.grid_layout.addWidget(
            QLabel("<h1>График</h1>"), 0, 0, Qt.AlignCenter)

        # Создаём таблицу. 1 столбец, число строк имзеняемое, начиная с 1
        self.tableRange = QTableWidget(self)
        self.tableRange.setColumnCount(2)

        self.tableRange.setHorizontalHeaderLabels(["Интервал", "Количество"])
        self.tableRange.move(300, 50)
        self.tableRange.resize(245, 850)

        # Создаём spinbox для изменения числа строк таблицы
        self.spin = QSpinBox(self)
        self.spin.move(10, 20)
        self.spin.setMaximum(50)
        self.spin.setMinimum(15)
        self.spin.valueChanged.connect(self.change)

        # Создаём таблицу. 1 столбец, число строк имзеняемое, начиная с 1
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.setRowCount(int(self.spin.text()))
        self.table.setHorizontalHeaderLabels(["Даннные"])
        self.table.move(10, 50)
        self.table.resize(160, 850)

        # Делаем кнопку, по нажатию которой мы должны передаём данные дальше в обработку
        self.btn = QPushButton("Обработать данные", self)
        self.btn.move(120, 20)
        self.btn.resize(30, 30)
        self.btn.clicked.connect(self.get_data)
        self.btn.adjustSize()

    def date_set(self, kol_interval, interval):
        self.tableRange.setRowCount(kol_interval)

        for i in range(kol_interval):
            self.tableRange.setItem(i, 0, QTableWidgetItem(
                str("{}-{}".format("%.2f" % interval[i][0], "%.2f" % interval[i][1]))))
            self.tableRange.setItem(i, 1, QTableWidgetItem(str(interval[i][2])))

    def change(self):
        self.table.setRowCount(int(self.spin.text()))

    def get_data(self):

        average = 0
        summ = 0
        maxX = -999999
        minX = 999999

        for i in range(self.table.rowCount()):
            if self.table.item(i, 0) is not None:
                print("Число ", self.table.item(i, 0).text())

                try:
                    average += 1
                    summ = float(self.table.item(i, 0).text()) + summ
                    if maxX < float(self.table.item(i, 0).text()):
                        maxX = float(self.table.item(i, 0).text())
                    if minX > float(self.table.item(i, 0).text()):
                        minX = float(self.table.item(i, 0).text())
                except:
                    pass

        if average != 0:

            kol_interval = int(1 + abs(log(average, 2)))
            print("Количество интервалов = ", kol_interval)
            shir_interval = (maxX - minX) / kol_interval
            print("Ширина интервала = ", shir_interval)
            interval = [[0] * 3 for i in range(kol_interval)]
            interval[0][0] = minX
            interval[0][1] = (interval[0][0] + shir_interval)
            numbers_in_interval = 0

            for i in range(1, kol_interval):
                interval[i][0] = interval[i - 1][1]
                interval[i][1] = (interval[i][0] + shir_interval)

            for b in range(kol_interval):

                for i in range(self.table.rowCount()):
                    if self.table.item(i, 0) is not None:
                        try:
                            if interval[b][0] <= float(self.table.item(i, 0).text()) <= interval[b][1]:
                                numbers_in_interval += 1
                        except:
                            pass
                interval[b][2] = numbers_in_interval
                numbers_in_interval = 0

            for i in range(kol_interval):
                print(i + 1, "Интервал", end=": ")
                print("%.2f" % interval[i][0], end="----")
                print("%.2f" % interval[i][1], end=" Количество чисел в интервале: ")
                print(interval[i][2])

            self.date_set(kol_interval, interval)


class Tab1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('background-color: #ffaabd;')

        self.cucm_welcome = Welcome()

        grid_layout = QHBoxLayout(self)

        grid_layout.addWidget(self.cucm_welcome, stretch=5)


class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        #        self.setFixedSize(MAIN_APP_WIDTH, MAIN_APP_HEIGHT)
        self.setFixedSize(1900, 980)
        self.setWindowTitle("App")

        tab1 = Tab1()

        self.main_tabs = QTabWidget()
        self.main_tabs.setStyleSheet('background-color: #ccffbd;')
        self.main_tabs.addTab(tab1, "Tab 1")
        self.main_tabs.addTab(QLabel('Доп. функционал'), "Tab 2")

        grid_layout = QGridLayout(self.centralWidget)
        grid_layout.addWidget(self.main_tabs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApplication()
    ex.show()
    sys.exit(app.exec_())
