import sys
from PyQt5.QtWidgets import *

from gui.mainwindow_manager_book import Ui_MainWindow_manager_book
from gui.book_alter import Ui_Dialog_book_alter

from list.ManagerList import ManagerList


class Ui_manager_book(QMainWindow, Ui_MainWindow_manager_book):
    """图书管理"""
    def __init__(self, manager_book_id):
        super(Ui_manager_book, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.manager_book_id = manager_book_id
        self.manager_book, self.manager_book_list = self.get_manager_book()

        # button连接界面
        self.ui_book_alter = Ui_book_alter()

        # button槽函数
        self.pushButton.clicked.connect(self.book_alter)
        self.pushButton_2.clicked.connect(self.book_import)
        self.pushButton_3.clicked.connect(self.query)

        self.menu.triggered[QAction].connect(self.menuTriggered)  # 菜单栏

    def book_alter(self):
        self.ui_book_alter.show()

    def book_import(self):
        from ui_others import Ui_import
        self.ui_import = Ui_import()
        self.ui_import.show()

    def query(self):
        QMessageBox.information(self, "提醒", "您正在查询xx图书！")

    def menuTriggered(self, q):
        if q.text() == "密码更改":
            from ui_others import Ui_pw_change
            self.ui_pw_change = Ui_pw_change('manager', self.manager_book, self.manager_book_list)
            self.ui_pw_change.show()
        if q.text() == "注销":
            from ui_others import Ui_Login
            self.ui_Login = Ui_Login()
            self.ui_Login.show()
            self.close()

    def get_manager_book(self):
        manager_book_list = ManagerList('system.db')
        manager_book = manager_book_list.getManagerById(self.manager_book_id)
        return manager_book, manager_book_list


class Ui_book_alter(QDialog, Ui_Dialog_book_alter):
    """图书信息修改"""
    def __init__(self):
        super(Ui_book_alter, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.pushButton_2.clicked.connect(self.stu_alter)
        self.pushButton.clicked.connect(self.close)

# 待完善2
    def stu_alter(self):
        QMessageBox.information(self, "提醒", "您已修改xx图书信息！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_manager_book = Ui_manager_book()
    ui_manager_book.show()
    sys.exit(app.exec_())
