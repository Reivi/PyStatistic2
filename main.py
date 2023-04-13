from cmath import log

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import loadUi
import sys


class ExampleApp(QtWidgets.QMainWindow, loadUi.Ui_MainWindow):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.setupUi(self)

        self.Spin_input_table.valueChanged.connect(self.change)

        self.Table_result.setColumnCount(2)
        self.Table_result.setHorizontalHeaderLabels(["Интервал", "Количество"])

        self.Table_input.setColumnCount(1)
        self.Table_input.setRowCount(int(self.Spin_input_table.text()))
        self.Table_input.setHorizontalHeaderLabels(["Даннные"])

        self.Obr_button.clicked.connect(self.get_data)

        self.GraphWidget.setLabel(axis='left', text='Количество')
        self.GraphWidget.setLabel(axis='bottom', text='Интервал')
        self.GraphWidget.setBackground('w')

    def plot(self, axisY, interval):
        self.GraphWidget.plot(y=axisY, x=interval)

    def date_set(self, kol_interval, interval):
        self.Table_result.setRowCount(kol_interval)
        spam = [1 * 3 for i in range(kol_interval)]
        tatl = [1 * 3 for i in range(kol_interval)]
        for i in range(kol_interval):
            spam[i] = interval[i][2]
            tatl[i] = interval[i][0]
            print("x=", i, "y=", int(interval[i][1]))
            self.Table_result.setItem(i, 0, QTableWidgetItem(
                str("{}-{}".format("%.2f" % interval[i][0], "%.2f" % interval[i][1]))))
            self.Table_result.setItem(i, 1, QTableWidgetItem(str(interval[i][2])))
        tatl[kol_interval-1] = interval[kol_interval-1][1]
        self.GraphWidget.plot(tatl, spam)

    def change(self):
        self.Table_input.setRowCount(int(self.Spin_input_table.text()))

    def get_data(self):

        average = 0
        summ = 0
        maxX = -999999
        minX = 999999

        for i in range(self.Table_input.rowCount()):
            if self.Table_input.item(i, 0) is not None:
                print("Число ", self.Table_input.item(i, 0).text())

                try:
                    summ = float(self.Table_input.item(i, 0).text()) + summ
                    average += 1
                    if maxX < float(self.Table_input.item(i, 0).text()):
                        maxX = float(self.Table_input.item(i, 0).text())
                    if minX > float(self.Table_input.item(i, 0).text()):
                        minX = float(self.Table_input.item(i, 0).text())
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

                for i in range(self.Table_input.rowCount()):
                    if self.Table_input.item(i, 0) is not None:
                        try:
                            if interval[b][0] <= float(self.Table_input.item(i, 0).text()) <= interval[b][1]:
                                numbers_in_interval += 1
                        except:
                            pass
                interval[b][2] = numbers_in_interval
                numbers_in_interval = 0
            self.date_set(kol_interval, interval)


app = QtWidgets.QApplication([])
application = ExampleApp()
application.show()

sys.exit(app.exec())
