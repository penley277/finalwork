# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_read.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_read(object):
    def setupUi(self, Dialog_read):
        Dialog_read.setObjectName("Dialog_read")
        Dialog_read.resize(613, 665)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        Dialog_read.setFont(font)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog_read)
        self.textBrowser.setGeometry(QtCore.QRect(30, 110, 551, 531))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog_read)
        self.label.setGeometry(QtCore.QRect(30, 70, 138, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_read)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_read)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog_read)
        self.pushButton.setGeometry(QtCore.QRect(460, 70, 93, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog_read)
        QtCore.QMetaObject.connectSlotsByName(Dialog_read)

    def retranslateUi(self, Dialog_read):
        _translate = QtCore.QCoreApplication.translate
        Dialog_read.setWindowTitle(_translate("Dialog_read", "Dialog"))
        self.label.setText(_translate("Dialog_read", "请输入书号："))
        self.label_2.setText(_translate("Dialog_read", "在线浏览"))
        self.pushButton.setText(_translate("Dialog_read", "浏览"))
