# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(377, 540)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.f_le = QtWidgets.QLineEdit(Form)
        self.f_le.setObjectName("f_le")
        self.horizontalLayout.addWidget(self.f_le)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.e_le = QtWidgets.QLineEdit(Form)
        self.e_le.setObjectName("e_le")
        self.horizontalLayout_2.addWidget(self.e_le)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.matrix_btn = QtWidgets.QPushButton(Form)
        self.matrix_btn.setMaximumSize(QtCore.QSize(123, 16777215))
        self.matrix_btn.setObjectName("matrix_btn")
        self.verticalLayout.addWidget(self.matrix_btn, 0, QtCore.Qt.AlignHCenter)
        self.export_btn = QtWidgets.QPushButton(Form)
        self.export_btn.setMaximumSize(QtCore.QSize(123, 16777215))
        self.export_btn.setObjectName("export_btn")
        self.verticalLayout.addWidget(self.export_btn, 0, QtCore.Qt.AlignHCenter)
        self.export_te = QtWidgets.QPlainTextEdit(Form)
        self.export_te.setMinimumSize(QtCore.QSize(0, 81))
        self.export_te.setMaximumSize(QtCore.QSize(16777215, 81))
        self.export_te.setObjectName("export_te")
        self.verticalLayout.addWidget(self.export_te)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ТПР Лаб 2 Чичканов Стоянов"))
        self.label.setText(_translate("Form", "Кол-во S"))
        self.label_2.setText(_translate("Form", "Кол-во П"))
        self.matrix_btn.setText(_translate("Form", "Вывести таблицу"))
        self.export_btn.setText(_translate("Form", "Решить"))

