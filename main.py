import math

import openpyxl
import pyqtgraph as pg

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from openpyxl.chart import Reference, BarChart
from openpyxl.styles import Font, Alignment

import loadUi
import sys


class ExampleApp(QtWidgets.QMainWindow, loadUi.Ui_MainWindow):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.setupUi(self)

        self.Spin_input_table.valueChanged.connect(self.change)

        self.Table_result.setColumnCount(2)
        self.Table_result.setHorizontalHeaderLabels(["Интервал", "Количество"])
        self.Table_result.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.Table_result.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        self.Table_input.setColumnCount(1)
        self.Table_input.setRowCount(int(self.Spin_input_table.text()))
        self.Table_input.setHorizontalHeaderLabels(["Даннные"])
        self.Table_input.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.Table_input.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        self.Table_statistic.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.Table_statistic.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        self.Obr_button.clicked.connect(self.get_data)

        self.window = pg.plot()
        self.Widget_Layout.addWidget(self.window)
        self.window.setBackground('w')
        self.window.showGrid(y=True)
        self.window.setMouseEnabled(x=False, y=False)

        self.action_Excel.triggered.connect(self.Export_to_Exel)

    def plot(self, axisX, axisY):
        self.window.clear()
        xdict = dict(enumerate(axisX))
        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])
        ticks = [list(zip(range(7), (axisX)))]
        xax = self.window.getAxis('bottom')
        xax.setTicks(ticks)
        self.window.addItem(pg.BarGraphItem(x=list(xdict.keys()), height=axisY, width=0.6, brush='g'))

    def Export_to_Exel(self):
        self.get_data()
        my_wb = openpyxl.Workbook()
        my_sheet = my_wb.active
        c1 = my_sheet.cell(row=1, column=1)
        c1.value = "Данные"
        bold_font = Font(bold=True)
        c1.alignment = Alignment(horizontal='center')
        c1.font = bold_font
        error_dialog = QtWidgets.QErrorMessage()
        try:
            for i in range(len(Data)):
                c1 = my_sheet.cell(row=i + 2, column=1)
                c1.value = Data[i]
                c1.alignment = Alignment(horizontal='center')
        except:
            error_dialog.showMessage('Данные не обработаны!')

        c1 = my_sheet.cell(row=1, column=3)
        c1.value = "Интервал"
        c1.font = bold_font
        c1 = my_sheet.cell(row=1, column=4)
        c1.value = "Количество"
        c1.font = bold_font

        for i in range(7):
            c1 = my_sheet.cell(row=i + 2, column=3)
            try:
                c1.value = QTableWidgetItem(
                    str("{}-{}".format("%.2f" % interval[i][0], "%.2f" % interval[i][1]))).text()
            except:
                error_dialog.showMessage('Данные не обработаны!')
            c1.alignment = Alignment(horizontal='center')
            c1 = my_sheet.cell(row=i + 2, column=4)
            c1.value = interval[i][2]
            c1.alignment = Alignment(horizontal='center')



        chart1 = BarChart()
        # установим тип - `вертикальные столбцы`
        chart1.type = "col"
        # установим стиль диаграммы (цветовая схема)
        chart1.style = 8

        chart1.title = "Столбчатая диаграмма"

        chart1.y_axis.title = 'Количество'
        chart1.y_axis.delete = False
        chart1.x_axis.title = 'Интервалы'
        chart1.x_axis.delete = False
        # выберем 2 столбца с данными для оси `y`
        data = Reference(my_sheet, min_col=4, max_col=4, min_row=1, max_row=8)
        # теперь выберем категорию для оси `x`
        categor = Reference(my_sheet, min_col=3, max_col=3, min_row=2, max_row=8)
        # добавляем данные в объект диаграммы
        chart1.add_data(data, titles_from_data=True)
        # установим метки на объект диаграммы
        chart1.set_categories(categor)
        # добавим диаграмму на лист, в ячейку "A10"
        my_sheet.add_chart(chart1, "D10")

        my_wb.save("Data_Excel.xlsx")

    def date_statistic_set(self, variance, sred_kvad_otkl, sr_snaz, koev_variazii, maxX, minX):
        self.Table_statistic.setRowCount(10)
        self.Table_statistic.setColumnCount(2)
        self.Table_statistic.setHorizontalHeaderLabels(["Название", "Значение"])
        self.Table_statistic.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Table_statistic.setItem(0, 0, QTableWidgetItem("Дисперсия"))
        self.Table_statistic.setItem(1, 0, QTableWidgetItem("Сред. квад. окл."))
        self.Table_statistic.setItem(2, 0, QTableWidgetItem("Среднее знач."))
        self.Table_statistic.setItem(3, 0, QTableWidgetItem("Коэф. вариац."))
        self.Table_statistic.setItem(4, 0, QTableWidgetItem("Мин."))
        self.Table_statistic.setItem(5, 0, QTableWidgetItem("Макс."))

        self.Table_statistic.setItem(0, 1, QTableWidgetItem(str(f"{variance:.6}")))
        self.Table_statistic.setItem(1, 1, QTableWidgetItem(str(f"{sred_kvad_otkl:.6}")))
        self.Table_statistic.setItem(2, 1, QTableWidgetItem(str(f"{sr_snaz:.6}")))
        self.Table_statistic.setItem(3, 1, QTableWidgetItem(str(f"{koev_variazii:.6}")))
        self.Table_statistic.setItem(4, 1, QTableWidgetItem(str(f"{minX:.6}")))
        self.Table_statistic.setItem(5, 1, QTableWidgetItem(str(f"{maxX:.6}")))

    def date_set(self, kol_interval, interval):
        self.Table_result.setRowCount(kol_interval)

        spam = [1 * 3 for i in range(kol_interval)]
        tatl = [1 * 3 for i in range(kol_interval)]
        for i in range(kol_interval):
            spam[i] = interval[i][2]
            tatl[i] = QTableWidgetItem(
                str("{}-{}".format("%.2f" % interval[i][0], "%.2f" % interval[i][1]))).text()
            self.Table_result.setItem(i, 0, QTableWidgetItem(
                str("{}-{}".format("%.2f" % interval[i][0], "%.2f" % interval[i][1]))))
            self.Table_result.setItem(i, 1, QTableWidgetItem(str(interval[i][2])))

        self.plot(tatl, spam)

    def change(self):
        self.Table_input.setRowCount(int(self.Spin_input_table.text()))

    def get_data(self):

        average = 0
        summ = 0
        maxX = -sys.maxsize - 1
        minX = sys.maxsize
        global Data
        Data = []

        for i in range(self.Table_input.rowCount()):
            if self.Table_input.item(i, 0) is not None:
                try:
                    Data.append(float(self.Table_input.item(i, 0).text()))
                    summ = float(self.Table_input.item(i, 0).text()) + summ
                    average += 1
                    if maxX < float(self.Table_input.item(i, 0).text()):
                        maxX = float(self.Table_input.item(i, 0).text())
                    if minX > float(self.Table_input.item(i, 0).text()):
                        minX = float(self.Table_input.item(i, 0).text())

                except:
                    pass

        if average != 0:
            kol_interval = 7  # int(1 + abs(log(average, 2)))
            sr_snaz = summ / len(Data)

            deviations = [(x - sr_snaz) ** 2 for x in Data]

            variance = sum(deviations) / len(Data)
            print("Дисперсия = ", variance)
            sred_kvad_otkl = math.sqrt(variance)
            print("Среднее квад. откл.",sred_kvad_otkl)
            koev_variazii= sred_kvad_otkl/sr_snaz

            shir_interval = (maxX - minX) / kol_interval
            global interval
            interval = [[0] * 3 for i in range(kol_interval)]
            interval[0][0] = minX
            interval[0][1] = (interval[0][0] + shir_interval)
            numbers_in_interval = 0

            for i in range(1, kol_interval):
                interval[i][0] = interval[i - 1][1]
                interval[i][1] = (interval[i][0] + shir_interval)

            for b in range(kol_interval):
                for i in range(self.Table_input.rowCount()):
                    try:
                        if interval[b][0] <= float(self.Table_input.item(i, 0).text()) <= interval[b][1]:
                            numbers_in_interval += 1
                    except:
                        pass
                interval[b][2] = numbers_in_interval
                numbers_in_interval = 0
            if interval[kol_interval - 1][2] == 0: interval[kol_interval - 1][2] += 1

            self.date_set(kol_interval, interval)
            self.date_statistic_set(variance, sred_kvad_otkl, sr_snaz,koev_variazii, maxX, minX)
        return variance, sred_kvad_otkl, sr_snaz,koev_variazii, maxX, minX



app = QtWidgets.QApplication([])
application = ExampleApp()
application.showMaximized()
application.show()

sys.exit(app.exec())
