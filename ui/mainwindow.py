# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 338)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 3, 1, 1)
        self.le_input2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_input2.setObjectName("le_input2")
        self.gridLayout_2.addWidget(self.le_input2, 4, 0, 1, 1)
        self.lbl_input = QtWidgets.QLabel(self.centralwidget)
        self.lbl_input.setObjectName("lbl_input")
        self.gridLayout_2.addWidget(self.lbl_input, 0, 0, 1, 1)
        self.tb_result = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_result.setEnabled(True)
        self.tb_result.setObjectName("tb_result")
        self.gridLayout_2.addWidget(self.tb_result, 8, 0, 1, 4)
        self.pb_vergleiche = QtWidgets.QPushButton(self.centralwidget)
        self.pb_vergleiche.setAutoDefault(False)
        self.pb_vergleiche.setDefault(True)
        self.pb_vergleiche.setFlat(False)
        self.pb_vergleiche.setObjectName("pb_vergleiche")
        self.gridLayout_2.addWidget(self.pb_vergleiche, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 9, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 8, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 1, 1, 1)
        self.le_input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_input1.setObjectName("le_input1")
        self.gridLayout_2.addWidget(self.le_input1, 3, 0, 1, 1)
        self.lbl_ergebnis = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ergebnis.setObjectName("lbl_ergebnis")
        self.gridLayout_2.addWidget(self.lbl_ergebnis, 7, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_input.setText(_translate("MainWindow", "Daten"))
        self.pb_vergleiche.setText(_translate("MainWindow", "vergleiche"))
        self.lbl_ergebnis.setText(_translate("MainWindow", "Ergebnis"))
