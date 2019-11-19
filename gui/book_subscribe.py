# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_subscribe.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_subscribe(object):
    def setupUi(self, Dialog_subscribe):
        Dialog_subscribe.setObjectName("Dialog_subscribe")
        Dialog_subscribe.resize(362, 245)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        Dialog_subscribe.setFont(font)
        self.label = QtWidgets.QLabel(Dialog_subscribe)
        self.label.setGeometry(QtCore.QRect(140, 30, 131, 30))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_subscribe)
        self.lineEdit.setGeometry(QtCore.QRect(70, 120, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog_subscribe)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 120, 22))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_subscribe)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 170, 93, 29))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog_subscribe)
        self.pushButton.setGeometry(QtCore.QRect(200, 170, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog_subscribe)
        QtCore.QMetaObject.connectSlotsByName(Dialog_subscribe)

    def retranslateUi(self, Dialog_subscribe):
        _translate = QtCore.QCoreApplication.translate
        Dialog_subscribe.setWindowTitle(_translate("Dialog_subscribe", "Dialog"))
        self.label.setText(_translate("Dialog_subscribe", "图书预约"))
        self.label_2.setText(_translate("Dialog_subscribe", "请输入书号："))
        self.pushButton_2.setText(_translate("Dialog_subscribe", "确认"))
        self.pushButton.setText(_translate("Dialog_subscribe", "取消"))
