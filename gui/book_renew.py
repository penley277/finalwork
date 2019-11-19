# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_renew.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_renew(object):
    def setupUi(self, Dialog_renew):
        Dialog_renew.setObjectName("Dialog_renew")
        Dialog_renew.resize(362, 228)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        Dialog_renew.setFont(font)
        self.label = QtWidgets.QLabel(Dialog_renew)
        self.label.setGeometry(QtCore.QRect(140, 30, 131, 30))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_renew)
        self.lineEdit.setGeometry(QtCore.QRect(70, 120, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog_renew)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 120, 22))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_renew)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 170, 93, 29))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog_renew)
        self.pushButton.setGeometry(QtCore.QRect(190, 170, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog_renew)
        QtCore.QMetaObject.connectSlotsByName(Dialog_renew)

    def retranslateUi(self, Dialog_renew):
        _translate = QtCore.QCoreApplication.translate
        Dialog_renew.setWindowTitle(_translate("Dialog_renew", "Dialog"))
        self.label.setText(_translate("Dialog_renew", "部分续借"))
        self.label_2.setText(_translate("Dialog_renew", "请输入书号："))
        self.pushButton_2.setText(_translate("Dialog_renew", "确认"))
        self.pushButton.setText(_translate("Dialog_renew", "取消"))
