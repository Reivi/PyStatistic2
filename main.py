import math
import os

import openpyxl
import pyqtgraph as pg

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QFileDialog
from openpyxl.chart import Reference, BarChart
from openpyxl.styles import Font, Alignment

import loadUi
import sys


class ExampleApp(QtWidgets.QMainWindow, loadUi.Ui_MainWindow):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("PyStatistic")

        self.Spin_input_table.valueChanged.connect(self.change)

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

        self.window_Pi = pg.plot()
        self.Widget_Layout.addWidget(self.window_Pi)
        self.window_Pi.setBackground('w')
        self.window_Pi.showGrid(y=True)
        self.window_Pi.setMouseEnabled(x=False, y=False)

        self.action_Excel.triggered.connect(self.Export_to_Exel)


        self.Name_graf.setPlaceholderText('Название проекта')

    def plot(self, axisX, axisY,Pi):
        self.window.clear()
        self.window.setLabel('left', 'Количество')
        self.window.setLabel('bottom', 'Интервалы')
        xdict = dict(enumerate(axisX))
        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])
        ticks = [list(zip(range(7), (axisX)))]
        xax = self.window.getAxis('bottom')
        xax.setTicks(ticks)
        self.window.addItem(pg.BarGraphItem(x=list(xdict.keys()), height=axisY, width=0.6, brush='g'))
        self.window.setTitle(self.Name_graf.text(), size="25pt", color="black")

        self.window_Pi.clear()
        self.window_Pi.setLabel('left', 'Pi')
        self.window_Pi.setLabel('bottom', 'Интервалы')
        xax = self.window_Pi.getAxis('bottom')
        xax.setTicks(ticks)
        self.window_Pi.addItem(pg.BarGraphItem(x=list(xdict.keys()), height=Pi, width=0.6, brush='g'))
        self.window_Pi.setTitle(self.Name_graf.text(), size="25pt", color="black")

    def Export_to_Exel(self):
        self.get_data()
        my_wb = openpyxl.Workbook()
        my_sheet = my_wb.active
        c1 = my_sheet.cell(row=1, column=1)
        c1.value = "№ опыта"
        bold_font = Font(bold=True)
        c1.alignment = Alignment(horizontal='center')
        c1.font = bold_font
        c1 = my_sheet.cell(row=1, column=2)
        c1.value = "Данные"
        bold_font = Font(bold=True)
        c1.alignment = Alignment(horizontal='center')
        c1.font = bold_font
        error_dialog = QtWidgets.QErrorMessage()
        try:
            for i in range(self.Table_input.rowCount()):
                c1 = my_sheet.cell(row=i + 2, column=2)
                c1.value = float(self.Table_input.item(i, 0).text())
                c1.alignment = Alignment(horizontal='center')
                c1 = my_sheet.cell(row=i + 2, column=1)
                c1.value = i + 1
                c1.alignment = Alignment(horizontal='center')
        except:
            pass
        c1 = my_sheet.cell(row=1, column=4)
        c1.value = "Интервал"
        c1.font = bold_font
        c1 = my_sheet.cell(row=1, column=5)
        c1.value = "Количество"
        c1.font = bold_font
        c1 = my_sheet.cell(row=1, column=6)
        c1.value = "Pi"
        c1.font = bold_font
        c1.alignment = Alignment(horizontal='center')

        for i in range(7):
            c1 = my_sheet.cell(row=i + 2, column=4)
            try:
                c1.value = self.Table_result.item(i, 0).text()
            except:
                error_dialog.showMessage('Данные не обработаны!')
            c1.alignment = Alignment(horizontal='center')
            c1 = my_sheet.cell(row=i + 2, column=5)
            c1.value = float(self.Table_result.item(i, 1).text())
            c1.alignment = Alignment(horizontal='center')
            c1 = my_sheet.cell(row=i + 2, column=6)
            c1.value = float(self.Table_result.item(i, 2).text())
            c1.alignment = Alignment(horizontal='center')

        c1 = my_sheet.cell(row=1, column=9)
        c1.value = "Параметр"
        c1.font = bold_font
        c1 = my_sheet.cell(row=1, column=8)
        c1.value = "Название"
        c1.font = bold_font
        c1 = my_sheet.cell(row=2, column=8)
        c1.value = "Дисперсия"
        c1.font = bold_font
        c1 = my_sheet.cell(row=3, column=8)
        c1.value = "Сред. квад. окл."
        c1.font = bold_font
        c1 = my_sheet.cell(row=4, column=8)
        c1.value = "Среднее знач."
        c1.font = bold_font
        c1 = my_sheet.cell(row=5, column=8)
        c1.value = "Коэф. вариац."
        c1.font = bold_font
        c1 = my_sheet.cell(row=6, column=8)
        c1.value = "Мин."
        c1.font = bold_font
        c1 = my_sheet.cell(row=7, column=8)
        c1.value = "Макс."
        c1.font = bold_font

        for i in range(6):
            c1 = my_sheet.cell(row=i + 2, column=9)
            c1.value = self.Table_statistic.item(i, 1).text()
            c1.alignment = Alignment(horizontal='center')

        chart1 = BarChart()
        # установим тип - `вертикальные столбцы`
        chart1.type = "col"
        # установим стиль диаграммы (цветовая схема)
        chart1.style = 8

        chart1.y_axis.title = 'Количество'
        chart1.y_axis.delete = False
        chart1.x_axis.title = 'Интервалы'
        chart1.x_axis.delete = False
        chart1.width = 15
        chart1.height = 11
        chart1.title = self.Name_graf.text()
        # выберем 2 столбца с данными для оси `y`
        data = Reference(my_sheet, min_col=5, max_col=5, min_row=1, max_row=8)
        # теперь выберем категорию для оси `x`
        categor = Reference(my_sheet, min_col=4, max_col=4, min_row=2, max_row=8)
        # добавляем данные в объект диаграммы
        chart1.add_data(data, titles_from_data=True)
        # установим метки на объект диаграммы
        chart1.set_categories(categor)
        my_sheet.add_chart(chart1, "K2")

        chart2 = BarChart()
        # установим тип - `вертикальные столбцы`
        chart2.type = "col"
        # установим стиль диаграммы (цветовая схема)
        chart2.style = 8

        chart2.y_axis.title = 'Pi'
        chart2.y_axis.delete = False
        chart2.x_axis.title = 'Интервалы'
        chart2.x_axis.delete = False
        chart2.width = 15
        chart2.height = 11
        chart2.title = self.Name_graf.text()
        # выберем 2 столбца с данными для оси `y`
        data = Reference(my_sheet, min_col=6, max_col=6, min_row=1, max_row=8)
        # теперь выберем категорию для оси `x`
        categor = Reference(my_sheet, min_col=4, max_col=4, min_row=2, max_row=8)
        # добавляем данные в объект диаграммы
        chart2.add_data(data, titles_from_data=True)
        # установим метки на объект диаграммы
        chart2.set_categories(categor)
        my_sheet.add_chart(chart2, "K24")

        if self.Name_graf.text() != "":
            save_name = self.Name_graf.text() + ".xlsx"
        else:
            for i in range(20):
                if not os.path.exists("Data_Excel_" + str(i) + ".xlsx"):
                    save_name = "Data_Excel_" + str(i) + ".xlsx"
                    break
                else:
                    continue
                    break

        fileName, _ = QFileDialog.getSaveFileName(self, "Экспорт данных в Excel", save_name,
                                                  "Excel Files (*.xlsx);;All Files (*)")
        if fileName:
            my_wb.save(fileName)



    def date_statistic_set(self, variance, sred_kvad_otkl, sr_snaz, koev_variazii, maxX, minX):
        self.Table_statistic.setRowCount(10)
        self.Table_statistic.setColumnCount(2)
        self.Table_statistic.setHorizontalHeaderLabels(["Параметр", "Значение"])
        self.Table_statistic.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Table_statistic.setItem(0, 0, QTableWidgetItem("Дисперсия"))
        self.Table_statistic.setItem(1, 0, QTableWidgetItem("Среднее квад. откл."))
        self.Table_statistic.setItem(2, 0, QTableWidgetItem("Среднее значение"))
        self.Table_statistic.setItem(3, 0, QTableWidgetItem("Коэффициент вариации"))
        self.Table_statistic.setItem(4, 0, QTableWidgetItem("Минимальное"))
        self.Table_statistic.setItem(5, 0, QTableWidgetItem("Максимальное"))

        self.Table_statistic.setItem(0, 1, QTableWidgetItem(str(round(variance, 4))))
        self.Table_statistic.setItem(1, 1, QTableWidgetItem(str(round(sred_kvad_otkl, 4))))
        self.Table_statistic.setItem(2, 1, QTableWidgetItem(str(round(sr_snaz, 4))))
        self.Table_statistic.setItem(3, 1, QTableWidgetItem(str(round(koev_variazii, 4))))
        self.Table_statistic.setItem(4, 1, QTableWidgetItem(str(round(minX, 4))))
        self.Table_statistic.setItem(5, 1, QTableWidgetItem(str(round(maxX, 4))))

    def date_set(self, kol_interval, interval, Pi):

        self.Table_result.setRowCount(kol_interval)
        self.Table_result.setColumnCount(3)
        self.Table_result.setHorizontalHeaderLabels(["Интервал", "Количество", "Pi"])

        spam = [1 * 3 for i in range(kol_interval)]
        tatl = [1 * 3 for i in range(kol_interval)]
        for i in range(kol_interval):
            spam[i] = interval[i][2]
            tatl[i] = QTableWidgetItem(
                str("{}-{}".format(f"{interval[i][0]:.5}", f"{interval[i][1]:.5}"))).text()
            self.Table_result.setItem(i, 0, QTableWidgetItem(str(tatl[i])))
            self.Table_result.setItem(i, 1, QTableWidgetItem(str(interval[i][2])))
            self.Table_result.setItem(i, 2, QTableWidgetItem(str(round(Pi[i], 4))))
        self.plot(tatl, spam, Pi)

    def change(self):
        self.Table_input.setRowCount(int(self.Spin_input_table.text()))

    def get_data(self):

        average = 0
        summ = 0
        maxX = -sys.maxsize - 1
        minX = sys.maxsize
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
            sred_kvad_otkl = math.sqrt(variance)
            koev_variazii = sred_kvad_otkl / sr_snaz

            shir_interval = (maxX - minX) / kol_interval
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
                        if interval[b][0] <= float(self.Table_input.item(i, 0).text()) <= round(interval[b][1], 10):
                            numbers_in_interval += 1
                    except:
                        pass
                interval[b][2] = numbers_in_interval
                numbers_in_interval = 0

            Pi = [1 * 1 for i in range(kol_interval)]

            for i in range(kol_interval):
                Pi[i] = float((1 / len(Data)) * interval[i][2])

            self.date_set(kol_interval, interval, Pi)
            self.date_statistic_set(variance, sred_kvad_otkl, sr_snaz, koev_variazii, maxX, minX)


app = QtWidgets.QApplication([])
application = ExampleApp()
application.showMaximized()
application.show()

sys.exit(app.exec())
