# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stu_delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_stu_delete(object):
    def setupUi(self, Dialog_stu_delete):
        Dialog_stu_delete.setObjectName("Dialog_stu_delete")
        Dialog_stu_delete.resize(336, 237)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        Dialog_stu_delete.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(Dialog_stu_delete)
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
        self.label = QtWidgets.QLabel(Dialog_stu_delete)
        self.label.setGeometry(QtCore.QRect(120, 20, 131, 30))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_stu_delete)
        self.lineEdit.setGeometry(QtCore.QRect(60, 110, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Dialog_stu_delete)
        self.comboBox.setGeometry(QtCore.QRect(30, 70, 81, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog_stu_delete)
        QtCore.QMetaObject.connectSlotsByName(Dialog_stu_delete)

    def retranslateUi(self, Dialog_stu_delete):
        _translate = QtCore.QCoreApplication.translate
        Dialog_stu_delete.setWindowTitle(_translate("Dialog_stu_delete", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog_stu_delete", "删除"))
        self.pushButton.setText(_translate("Dialog_stu_delete", "取消"))
        self.label.setText(_translate("Dialog_stu_delete", "批量删除"))
        self.comboBox.setItemText(0, _translate("Dialog_stu_delete", "班级"))
        self.comboBox.setItemText(1, _translate("Dialog_stu_delete", "专业"))
