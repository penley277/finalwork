import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gui.mainwindow_stu import Ui_MainWindow_stu
from gui.borrow_info import Ui_Dialog_borrow_info
from gui.book_renew import Ui_Dialog_renew
from gui.book_borrow import Ui_Dialog_book_borrow
from gui.book_return import Ui_Dialog_book_return
from gui.book_search import Ui_Widget_book_search
from gui.book_subscribe import Ui_Dialog_subscribe
from gui.book_read import Ui_Dialog_read


class Ui_stu(QMainWindow, Ui_MainWindow_stu):
    """学生主界面"""

    def __init__(self):
        super(Ui_stu, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        # 推荐榜
        self.model = QStandardItemModel(10, 2)
        self.model.setHorizontalHeaderLabels(['书名', '推荐理由'])
        self.tableView.setModel(self.model)

        # 排行榜
        self.model_2 = QStandardItemModel(10, 3)
        self.model_2.setHorizontalHeaderLabels(['书名', '作者', '借阅人数'])
        self.tableView_2.setModel(self.model_2)

        # tableview布局
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # button连接界面
        self.ui_borrow_info = Ui_borrow_info()
        self.ui_book_borrow = Ui_book_borrow()
        self.ui_book_return = Ui_book_return()
        self.ui_book_search = Ui_book_search()

        # button槽函数
        self.pushButton.clicked.connect(self.borrow_info)
        self.pushButton_2.clicked.connect(self.book_borrow)
        self.pushButton_3.clicked.connect(self.book_return)
        self.pushButton_4.clicked.connect(self.book_search)

        # 菜单栏

        self.menu.triggered[QAction].connect(self.menuTriggered)

    def borrow_info(self):
        self.ui_borrow_info.show()

    def book_borrow(self):
        self.ui_book_borrow.show()

    def book_return(self):
        self.ui_book_return.show()

    def book_search(self):
        self.ui_book_search.show()

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


class Ui_borrow_info(QDialog, Ui_Dialog_borrow_info):
    """借阅信息"""

    def __init__(self):
        super(Ui_borrow_info, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        # button
        self.ui_book_renew = Ui_book_renew()  # 部分续借界面

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.book_renew)
        self.pushButton_3.clicked.connect(self.all_renew)

    def book_renew(self):
        self.ui_book_renew.show()

# 待完善1
    def all_renew(self):
        QMessageBox.information(self, "提醒", "您已全部续借所借图书！")


class Ui_book_renew(QDialog, Ui_Dialog_renew):
    """图书续借"""

    def __init__(self):
        super(Ui_book_renew, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        # button槽函数
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.renew_ok)

# 待完善2
    def renew_ok(self):
        QMessageBox.information(self, "提醒", "您已续借xx图书！")


class Ui_book_borrow(QDialog, Ui_Dialog_book_borrow):
    """图书借阅"""

    def __init__(self):
        super(Ui_book_borrow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        # button槽函数
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.borrow_ok)

# 待完善3
    def borrow_ok(self):
        QMessageBox.information(self, "提醒", "您已借阅xx图书！")


class Ui_book_return(QDialog, Ui_Dialog_book_return):
    """图书归还"""

    def __init__(self):
        super(Ui_book_return, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        # button槽函数
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.return_ok)

# 待完善4
    def return_ok(self):
        QMessageBox.information(self, "提醒", "您已归还xx图书！")


class Ui_book_search(QWidget, Ui_Widget_book_search):
    """图书查询"""

    def __init__(self):
        super(Ui_book_search, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.ui_book_subscribe = Ui_book_subscribe()
        self.ui_book_read = Ui_book_read()

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.book_subscribe)
        self.pushButton_3.clicked.connect(self.book_read)
        self.pushButton_4.clicked.connect(self.query)

    def book_subscribe(self):
        self.ui_book_subscribe.show()

    def book_read(self):
        self.ui_book_read.show()

# 待完善5
    def query(self):
        QMessageBox.information(self, "提醒", "查询xx图书！")


class Ui_book_subscribe(QDialog, Ui_Dialog_subscribe):
    """图书预约"""

    def __init__(self):
        super(Ui_book_subscribe, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        # button槽函数
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.subscribe_ok)

# 待完善6
    def subscribe_ok(self):
        QMessageBox.information(self, "提醒", "您已预约xx图书！")


class Ui_book_read(QDialog, Ui_Dialog_read):
    """在线浏览"""

    def __init__(self):
        super(Ui_book_read, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.ui_book_borrow = Ui_book_borrow()
        # button槽函数
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.book_borrow)
        self.pushButton_3.clicked.connect(self.book_read)

    def book_borrow(self):
        self.ui_book_borrow.show()

# 待完善7
    def book_read(self):
        QMessageBox.information(self, "提醒", "您正在浏览xx图书！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_student_main = Ui_stu()
    ui_student_main.show()
    sys.exit(app.exec_())
