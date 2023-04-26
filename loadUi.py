# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 50, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Spin_input_table = QtWidgets.QSpinBox(self.centralwidget)
        self.Spin_input_table.setMinimum(20)
        self.Spin_input_table.setMaximum(200)
        self.Spin_input_table.setObjectName("Spin_input_table")
        self.horizontalLayout.addWidget(self.Spin_input_table)
        self.Obr_button = QtWidgets.QPushButton(self.centralwidget)
        self.Obr_button.setObjectName("Obr_button")
        self.horizontalLayout.addWidget(self.Obr_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Name_graf = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Name_graf.sizePolicy().hasHeightForWidth())
        self.Name_graf.setSizePolicy(sizePolicy)
        self.Name_graf.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.Name_graf.setText("")
        self.Name_graf.setReadOnly(False)
        self.Name_graf.setPlaceholderText("")
        self.Name_graf.setObjectName("Name_graf")
        self.verticalLayout.addWidget(self.Name_graf)
        self.Table_input = QtWidgets.QTableWidget(self.centralwidget)
        self.Table_input.setEnabled(True)
        self.Table_input.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.Table_input.setTabKeyNavigation(True)
        self.Table_input.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.Table_input.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.Table_input.setObjectName("Table_input")
        self.Table_input.setColumnCount(0)
        self.Table_input.setRowCount(0)
        self.verticalLayout.addWidget(self.Table_input)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Table_result = QtWidgets.QTableWidget(self.centralwidget)
        self.Table_result.setMinimumSize(QtCore.QSize(375, 0))
        self.Table_result.setMaximumSize(QtCore.QSize(400, 275))
        self.Table_result.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Table_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table_result.setObjectName("Table_result")
        self.Table_result.setColumnCount(0)
        self.Table_result.setRowCount(0)
        self.verticalLayout_2.addWidget(self.Table_result)
        self.Table_statistic = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table_statistic.sizePolicy().hasHeightForWidth())
        self.Table_statistic.setSizePolicy(sizePolicy)
        self.Table_statistic.setMinimumSize(QtCore.QSize(260, 0))
        self.Table_statistic.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Table_statistic.setSizeIncrement(QtCore.QSize(0, 0))
        self.Table_statistic.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Table_statistic.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Table_statistic.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Table_statistic.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table_statistic.setObjectName("Table_statistic")
        self.Table_statistic.setColumnCount(0)
        self.Table_statistic.setRowCount(0)
        self.Table_statistic.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.Table_statistic)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.Widget_Layout = QtWidgets.QVBoxLayout()
        self.Widget_Layout.setObjectName("Widget_Layout")
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.Widget_Layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_Excel = QtWidgets.QAction(MainWindow)
        self.action_Excel.setObjectName("action_Excel")
        self.import_Excel = QtWidgets.QAction(MainWindow)
        self.import_Excel.setObjectName("import_Excel")
        self.menu.addAction(self.action_Excel)
        self.menu.addAction(self.import_Excel)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Obr_button.setText(_translate("MainWindow", "Обработка"))
        self.menu.setTitle(_translate("MainWindow", "Опции"))
        self.action.setText(_translate("MainWindow", "Настройки"))
        self.action_Excel.setText(_translate("MainWindow", "Экспорт в Excel"))
        self.import_Excel.setText(_translate("MainWindow", "Импорт из Excel"))
