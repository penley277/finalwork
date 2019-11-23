import sys
from PyQt5.QtWidgets import *

from gui.mainwindow_manager_stu import Ui_MainWindow_manager_stu
from gui.stu_add import Ui_Dialog_stu_add
from gui.stu_alter import Ui_Dialog_stu_alter
from gui.stu_delete import Ui_Dialog_stu_delete

from list.ManagerList import ManagerList


class Ui_manager_stu(QMainWindow, Ui_MainWindow_manager_stu):
    """学生管理"""
    def __init__(self, manager_stu_id):
        super(Ui_manager_stu, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.manager_stu_id = manager_stu_id
        self.manager_stu, self.manager_stu_list = self.get_manager_stu()

        # button连接界面
        self.ui_stu_add = Ui_stu_add()
        self.ui_stu_alter = Ui_stu_alter()
        self.ui_stu_delete = Ui_stu_delete()

        # button槽函数
        self.pushButton.clicked.connect(self.stu_add)
        self.pushButton_2.clicked.connect(self.stu_alter)
        self.pushButton_3.clicked.connect(self.stu_delete)
        self.pushButton_4.clicked.connect(self.stu_import)
        self.pushButton_5.clicked.connect(self.query)

        self.menu.triggered[QAction].connect(self.menuTriggered)    # 菜单栏

    def stu_add(self):
        self.ui_stu_add.show()

    def stu_alter(self):
        self.ui_stu_alter.show()

    def stu_delete(self):
        self.ui_stu_delete.show()

    def stu_import(self):
        from ui_others import Ui_import
        self.ui_import = Ui_import()
        self.ui_import.show()

    def query(self):
        QMessageBox.information(self, "提醒", "您正在查询xx学生！")

    def menuTriggered(self, q):
        if q.text() == "密码更改":
            from ui_others import Ui_pw_change
            self.ui_pw_change = Ui_pw_change('manager', self.manager_stu, self.manager_stu_list)
            self.ui_pw_change.show()
        if q.text() == "注销":
            from ui_others import Ui_Login
            self.ui_Login = Ui_Login()
            self.ui_Login.show()
            self.close()

    def get_manager_stu(self):
        manager_stu_list = ManagerList('system.db')
        manager_stu = manager_stu_list.getManagerById(self.manager_stu_id)
        return manager_stu, manager_stu_list


class Ui_stu_add(QDialog, Ui_Dialog_stu_add):
    """学生账户添加:"""
    def __init__(self):
        super(Ui_stu_add, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton_2.clicked.connect(self.stu_add)
        self.pushButton.clicked.connect(self.close)

# 待完善1
    def stu_add(self):
        QMessageBox.information(self, "提醒", "您已添加xx学生！")


class Ui_stu_alter(QDialog, Ui_Dialog_stu_alter):
    """学生信息修改"""
    def __init__(self):
        super(Ui_stu_alter, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton_2.clicked.connect(self.stu_alter)
        self.pushButton.clicked.connect(self.close)

# 待完善2
    def stu_alter(self):
        QMessageBox.information(self, "提醒", "您已修改xx学生信息！")


class Ui_stu_delete(QDialog, Ui_Dialog_stu_delete):
    """批量删除:"""
    def __init__(self):
        super(Ui_stu_delete, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton_2.clicked.connect(self.stu_delete)
        self.pushButton.clicked.connect(self.close)

# 待完善2
    def stu_delete(self):
        QMessageBox.information(self, "提醒", "您已批量删除xx学生！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_manager_stu = Ui_manager_stu()
    ui_manager_stu.show()
    sys.exit(app.exec_())
