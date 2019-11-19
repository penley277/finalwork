# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_return.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_book_return(object):
    def setupUi(self, Dialog_book_return):
        Dialog_book_return.setObjectName("Dialog_book_return")
        Dialog_book_return.resize(448, 402)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        Dialog_book_return.setFont(font)
        self.label_2 = QtWidgets.QLabel(Dialog_book_return)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 120, 22))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog_book_return)
        self.label.setGeometry(QtCore.QRect(180, 20, 131, 30))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_book_return)
        self.lineEdit.setGeometry(QtCore.QRect(60, 110, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.layoutWidget = QtWidgets.QWidget(Dialog_book_return)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 350, 195, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(Dialog_book_return)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 100, 22))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Dialog_book_return)
        self.textEdit.setGeometry(QtCore.QRect(60, 200, 331, 131))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog_book_return)
        QtCore.QMetaObject.connectSlotsByName(Dialog_book_return)

    def retranslateUi(self, Dialog_book_return):
        _translate = QtCore.QCoreApplication.translate
        Dialog_book_return.setWindowTitle(_translate("Dialog_book_return", "Dialog"))
        self.label_2.setText(_translate("Dialog_book_return", "请输入书号："))
        self.label.setText(_translate("Dialog_book_return", "图书归还"))
        self.pushButton_2.setText(_translate("Dialog_book_return", "确认"))
        self.pushButton.setText(_translate("Dialog_book_return", "取消"))
        self.label_3.setText(_translate("Dialog_book_return", "发表书评："))
