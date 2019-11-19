# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_error(object):
    def setupUi(self, Dialog_error):
        Dialog_error.setObjectName("Dialog_error")
        Dialog_error.resize(477, 145)
        self.label = QtWidgets.QLabel(Dialog_error)
        self.label.setGeometry(QtCore.QRect(30, 30, 420, 39))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog_error)
        self.pushButton.setGeometry(QtCore.QRect(200, 90, 93, 31))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog_error)
        QtCore.QMetaObject.connectSlotsByName(Dialog_error)

    def retranslateUi(self, Dialog_error):
        _translate = QtCore.QCoreApplication.translate
        Dialog_error.setWindowTitle(_translate("Dialog_error", "Dialog"))
        self.label.setText(_translate("Dialog_error", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff0000;\">账号或密码错误，请重新输入！</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog_error", "确认"))
