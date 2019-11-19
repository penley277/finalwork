from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui_stu import Ui_stu
from ui_manager_stu import Ui_manager_stu
from ui_manager_book import Ui_manager_book
from ui_manager_sys import Ui_manager_sys

from gui.login import Ui_Widget_login
from gui.pw_change import Ui_Dialog_pw_change
from gui.error import Ui_Dialog_error
from gui.batch_import import Ui_Dialog_import


class Ui_Login(QWidget, Ui_Widget_login):
    """登录窗口"""
    def __init__(self):
        super(Ui_Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.ui_stu = Ui_stu()    # 学生主页
        self.ui_manager_stu = Ui_manager_stu()  # 学生管理主页
        self.ui_manager_book = Ui_manager_book()  # 学生管理主页
        self.ui_manager_sys = Ui_manager_sys()  # 学生管理主页

        self.buttonBox_2.clicked.connect(self.slot_Login)
        self.buttonBox.clicked.connect(self.close)

# 待完善8
    def slot_Login(self):
        self.get_comboBox('学生', '1', '1', self.ui_stu)
        self.get_comboBox('学生管理员', '2', '2', self.ui_manager_stu)
        self.get_comboBox('图书管理员', '3', '3', self.ui_manager_book)
        self.get_comboBox('系统管理员', '4', '4', self.ui_manager_sys)

    def get_comboBox(self, Type, username, password, ui):
        if self.comboBox.currentText() == Type:
            if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
                QMessageBox.warning(self, "警告", "账号或密码不能为空，请重新输入！")
            if username == self.lineEdit.text() and password == self.lineEdit_2.text():
                ui.show()
                self.close()
            else:
                QMessageBox.warning(self, "警告", "账号或密码错误，请重新输入！")


class Ui_pw_change(QDialog, Ui_Dialog_pw_change):
    """密码修改"""
    def __init__(self):
        super(Ui_pw_change, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.pw_change)

# 待完善9
    def pw_change(self):
        QMessageBox.information(self, "提醒", "您已修改密码！")


class Ui_error(QDialog, Ui_Dialog_error):
    """错误提示"""
    def __init__(self):
        super(Ui_error, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton.clicked.connect(self.close)  # 连接槽函数：确认按钮


class Ui_import(QDialog, Ui_Dialog_import):
    """批量导入:"""
    def __init__(self):
        super(Ui_import, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton_2.clicked.connect(self.stu_import)
        self.pushButton.clicked.connect(self.close)

# 待完善3
    def stu_import(self):
        QMessageBox.information(self, "提醒", "批量导入完成！")
