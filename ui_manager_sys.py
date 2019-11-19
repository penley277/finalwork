import sys
from PyQt5.QtWidgets import *

from gui.mainwindow_manager_sys import Ui_MainWindow_manager_sys
from gui.sys_add import Ui_Dialog_sys_add
from gui.sys_delete import Ui_Dialog_stu_delete
from gui.sys_alter import Ui_Dialog_stu_alter


class Ui_manager_sys(QMainWindow, Ui_MainWindow_manager_sys):
    """系统管理"""

    def __init__(self):
        super(Ui_manager_sys, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        # button连接界面
        self.ui_sys_add = Ui_sys_add()
        self.ui_sys_delete = Ui_sys_delete()
        self.ui_sys_alter = Ui_sys_alter()

        # button槽函数
        self.pushButton.clicked.connect(self.sys_add)
        self.pushButton_2.clicked.connect(self.sys_delete)
        self.pushButton_3.clicked.connect(self.sys_alter)
        self.pushButton_4.clicked.connect(self.query)

        self.menu.triggered[QAction].connect(self.menuTriggered)  # 菜单栏

    def sys_add(self):
        self.ui_sys_add.show()

    def sys_delete(self):
        self.ui_sys_delete.show()

    def sys_alter(self):
        self.ui_sys_alter.show()

    def query(self):
        QMessageBox.information(self, "提醒", "您正在查询xx管理员信息！")

    def menuTriggered(self, q):
        if q.text() == "密码更改":
            from ui_others import Ui_pw_change
            self.ui_pw_change = Ui_pw_change()
            self.ui_pw_change.show()
        if q.text() == "注销":
            from ui_others import Ui_Login
            self.ui_Login = Ui_Login()
            self.ui_Login.show()
            self.close()


class Ui_sys_add(QDialog, Ui_Dialog_sys_add):
    """管理员添加"""

    def __init__(self):
        super(Ui_sys_add, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton_2.clicked.connect(self.sys_add)
        self.pushButton.clicked.connect(self.close)

    # 待完善2
    def sys_add(self):
        QMessageBox.information(self, "提醒", "您已添加xx管理员！")


class Ui_sys_delete(QDialog, Ui_Dialog_stu_delete):
    """管理员删除"""

    def __init__(self):
        super(Ui_sys_delete, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton_2.clicked.connect(self.sys_delete)
        self.pushButton.clicked.connect(self.close)

    # 待完善2
    def sys_delete(self):
        QMessageBox.information(self, "提醒", "您已删除xx管理员！")


class Ui_sys_alter(QDialog, Ui_Dialog_stu_alter):
    """管理员信息修改"""

    def __init__(self):
        super(Ui_sys_alter, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton_2.clicked.connect(self.sys_alter)
        self.pushButton.clicked.connect(self.close)

    # 待完善2
    def sys_alter(self):
        QMessageBox.information(self, "提醒", "您已修改xx管理员信息！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_manager_sys = Ui_manager_sys()
    ui_manager_sys.show()
    sys.exit(app.exec_())
