# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget_book_search(object):
    def setupUi(self, Widget_book_search):
        Widget_book_search.setObjectName("Widget_book_search")
        Widget_book_search.resize(635, 576)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        Widget_book_search.setFont(font)
        self.pushButton_4 = QtWidgets.QPushButton(Widget_book_search)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 80, 71, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(Widget_book_search)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Widget_book_search)
        self.comboBox.setGeometry(QtCore.QRect(40, 80, 81, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(Widget_book_search)
        self.textBrowser.setGeometry(QtCore.QRect(50, 120, 541, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Widget_book_search)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 520, 93, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Widget_book_search)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 520, 93, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Widget_book_search)
        self.label.setGeometry(QtCore.QRect(270, 20, 131, 30))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Widget_book_search)
        self.pushButton.setGeometry(QtCore.QRect(400, 520, 93, 31))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Widget_book_search)
        QtCore.QMetaObject.connectSlotsByName(Widget_book_search)

    def retranslateUi(self, Widget_book_search):
        _translate = QtCore.QCoreApplication.translate
        Widget_book_search.setWindowTitle(_translate("Widget_book_search", "Form"))
        self.pushButton_4.setText(_translate("Widget_book_search", "查询"))
        self.comboBox.setItemText(0, _translate("Widget_book_search", "书名"))
        self.comboBox.setItemText(1, _translate("Widget_book_search", "书号"))
        self.comboBox.setItemText(2, _translate("Widget_book_search", "作者"))
        self.comboBox.setItemText(3, _translate("Widget_book_search", "出版社"))
        self.pushButton_2.setText(_translate("Widget_book_search", "图书预约"))
        self.pushButton_3.setText(_translate("Widget_book_search", "在线浏览"))
        self.label.setText(_translate("Widget_book_search", "图书查询"))
        self.pushButton.setText(_translate("Widget_book_search", "取消"))
