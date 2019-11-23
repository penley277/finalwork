# coding=utf-8
from PyQt5.QtWidgets import *

from ui_stu import Ui_stu
from ui_manager_stu import Ui_manager_stu
from ui_manager_book import Ui_manager_book
from ui_manager_sys import Ui_manager_sys

from gui.login import Ui_Widget_login
from gui.pw_change import Ui_Dialog_pw_change
from gui.error import Ui_Dialog_error
from gui.batch_import import Ui_Dialog_import

from list.StudentList import StudentList
from list.ManagerList import ManagerList


class Ui_Login(QWidget, Ui_Widget_login):
    """登录窗口"""

    def __init__(self):
        super(Ui_Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)  # 遮盖密码

        self.userID = ''  # 用户id

        self.buttonBox_2.clicked.connect(self.slot_Login)  # 登录函数
        self.buttonBox.clicked.connect(self.close)

    def slot_Login(self):
        """
        登录
        :return:
        """

        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
            QMessageBox.warning(self, "警告", "账号或密码不能为空，请重新输入！")
        else:
            self.userID = self.lineEdit.text()  # 用户id
            if self.comboBox.currentText() == '学生':
                self.login_stu()
            else:
                self.login_manager()

    def login_stu(self):
        """
        学生登录
        :return:
        """

        stu_list = StudentList('system.db')
        stu = stu_list.getStuByNo(self.userID)  # 寻找该id学生对象

        try:
            password_stu = stu.getPassWd()  # 学生密码
            self.ui_stu = Ui_stu(self.userID)  # 学生主页
            self.LoginCheck('学生', password_stu, self.ui_stu)
        except AttributeError:
            QMessageBox.warning(self, "警告", "该账号不存在，请重新输入！")

    def login_manager(self):
        """
        管理员登录
        :return:
        """

        manager_list = ManagerList('system.db')
        manager = manager_list.getManagerById(self.userID)  # 寻找该id管理员对象

        try:
            manager_type = manager.getType()  # 获得类型
            manager_password = manager.getPassWd()  # 获得密码

            if manager_type == '学生管理员':
                self.ui_manager_stu = Ui_manager_stu(self.userID)  # 学生管理主页
                self.LoginCheck(manager_type, manager_password, self.ui_manager_stu)
            if manager_type == '图书管理员':
                self.ui_manager_book = Ui_manager_book(self.userID)  # 图书管理主页
                self.LoginCheck(manager_type, manager_password, self.ui_manager_book)
            if manager_type == '系统管理员':
                self.ui_manager_sys = Ui_manager_sys(self.userID)  # 系统管理主页
                self.LoginCheck(manager_type, manager_password, self.ui_manager_sys)
        except AttributeError:
            QMessageBox.warning(self, "警告", "该账号不存在，请重新输入！")

    def LoginCheck(self, Type, password, ui):
        """
        根据用户类型、密码检查登陆
        :param Type: 用户类型
        :param password: 用户密码
        :param ui: 主页
        :return: 无
        """

        if self.comboBox.currentText() == Type:
            if password == self.lineEdit_2.text():
                ui.show()
                self.close()
            else:
                QMessageBox.warning(self, "警告", "账号或密码错误，请重新输入！")


class Ui_pw_change(QDialog, Ui_Dialog_pw_change):
    """密码修改"""

    def __init__(self, Type, user, List):
        super(Ui_pw_change, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)  # 遮盖密码
        self.lineEdit_3.setEchoMode(QLineEdit.Password)  # 遮盖密码

        self.user = user
        self.list = List
        self.Type = Type

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.pw_change)

    def pw_change(self):
        if self.lineEdit.text() == self.user.getPassWd():
            if self.lineEdit_2.text() == self.lineEdit_3.text():
                if self.Type == 'student':
                    self.list.setPW(self.user.studNo, self.lineEdit_2.text())
                if self.Type == 'manager':
                    self.list.setPW(self.user.managerID, self.lineEdit_2.text())
                QMessageBox.information(self, "提醒", "您已修改密码！")
                self.close()
            else:
                QMessageBox.warning(self, "警告", "两次输入不一致！")
        else:
            QMessageBox.warning(self, "警告", "密码输入错误！")


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
