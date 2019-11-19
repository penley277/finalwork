# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batch_import.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_import(object):
    def setupUi(self, Dialog_import):
        Dialog_import.setObjectName("Dialog_import")
        Dialog_import.resize(336, 237)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        Dialog_import.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(Dialog_import)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 170, 195, 31))
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
        self.label = QtWidgets.QLabel(Dialog_import)
        self.label.setGeometry(QtCore.QRect(120, 20, 131, 30))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_import)
        self.lineEdit.setGeometry(QtCore.QRect(60, 110, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog_import)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 151, 22))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog_import)
        QtCore.QMetaObject.connectSlotsByName(Dialog_import)

    def retranslateUi(self, Dialog_import):
        _translate = QtCore.QCoreApplication.translate
        Dialog_import.setWindowTitle(_translate("Dialog_import", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog_import", "导入"))
        self.pushButton.setText(_translate("Dialog_import", "取消"))
        self.label.setText(_translate("Dialog_import", "批量导入"))
        self.label_2.setText(_translate("Dialog_import", "请输入文件名："))
