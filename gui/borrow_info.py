# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrow_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_borrow_info(object):
    def setupUi(self, Dialog_borrow_info):
        Dialog_borrow_info.setObjectName("Dialog_borrow_info")
        Dialog_borrow_info.resize(471, 382)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        Dialog_borrow_info.setFont(font)
        self.label = QtWidgets.QLabel(Dialog_borrow_info)
        self.label.setGeometry(QtCore.QRect(170, 20, 131, 30))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_borrow_info)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 140, 22))
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(Dialog_borrow_info)
        self.tableView.setGeometry(QtCore.QRect(40, 110, 391, 191))
        self.tableView.setObjectName("tableView")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_borrow_info)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 320, 93, 29))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog_borrow_info)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 320, 93, 29))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Dialog_borrow_info)
        self.pushButton.setGeometry(QtCore.QRect(300, 320, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog_borrow_info)
        QtCore.QMetaObject.connectSlotsByName(Dialog_borrow_info)

    def retranslateUi(self, Dialog_borrow_info):
        _translate = QtCore.QCoreApplication.translate
        Dialog_borrow_info.setWindowTitle(_translate("Dialog_borrow_info", "Dialog"))
        self.label.setText(_translate("Dialog_borrow_info", "借阅查询"))
        self.label_2.setText(_translate("Dialog_borrow_info", "当前借阅情况："))
        self.pushButton_2.setText(_translate("Dialog_borrow_info", "部分续借"))
        self.pushButton_3.setText(_translate("Dialog_borrow_info", "全部续借"))
        self.pushButton.setText(_translate("Dialog_borrow_info", "取消"))
