# coding=utf-8
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

from list.StudentList import StudentList
from list.BorrowInformList import BorrowInformList
from list.BookList import BookList


class Ui_stu(QMainWindow, Ui_MainWindow_stu):
    """学生主界面"""

    def __init__(self, stu_id):
        super(Ui_stu, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.stu_id = stu_id
        self.stu, self.stu_list = self.get_stu()
        self.borrow_list = BorrowInformList('system.db')

        self.model = QStandardItemModel(10, 2)  # 推荐榜
        self.show_recommend()

        self.model_2 = QStandardItemModel(10, 3)  # 排行榜
        self.show_leaderboard()

        # button连接界面
        self.ui_borrow_info = Ui_borrow_info(self.stu_id)
        self.ui_book_borrow = Ui_book_borrow(self.stu_id)
        self.ui_book_return = Ui_book_return(self.stu_id)
        self.ui_book_search = Ui_book_search(self.stu_id)

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
            self.ui_pw_change = Ui_pw_change('student', self.stu, self.stu_list)
            self.ui_pw_change.show()
        if q.text() == "注销":
            from ui_others import Ui_Login
            self.ui_Login = Ui_Login()
            self.ui_Login.show()
            self.close()

    def get_stu(self):
        stu_list = StudentList('system.db')
        stu = stu_list.getStuByNo(self.stu_id)
        return stu, stu_list

    def show_recommend(self):
        self.model.setHorizontalHeaderLabels(['书名', '推荐理由'])

        Recommend = [['1', '2'], []]
        for row, linedata in enumerate(Recommend):
            for column, itemdata in enumerate(linedata):
                item = QStandardItem(str(itemdata)) if itemdata is not None else QStandardItem('')
                item.setEditable(False)

                self.model.setItem(row, column, item)

        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 布局

    def show_leaderboard(self):
        self.model_2.setHorizontalHeaderLabels(['书名', '作者', '借阅人数'])

        leaderboard = self.borrow_list.topTenByCnt()
        if leaderboard is None:
            leaderboard = []
        for row, linedata in enumerate(leaderboard):
            for column, itemdata in enumerate(linedata):
                item = QStandardItem(str(itemdata)) if itemdata is not None else QStandardItem('')
                item.setEditable(False)

                self.model_2.setItem(row, column, item)

        self.tableView_2.setModel(self.model_2)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)   # 布局


class Ui_borrow_info(QDialog, Ui_Dialog_borrow_info):
    """借阅信息"""

    def __init__(self, stu_id):
        super(Ui_borrow_info, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.stu_id = stu_id
        self.borrow_list = BorrowInformList('system.db')

        self.model = QStandardItemModel(10, 3)  # 借阅信息
        self.show_borrow_info()

        # button
        self.ui_book_renew = Ui_book_renew(self.stu_id)  # 部分续借界面

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.book_renew)
        self.pushButton_3.clicked.connect(self.all_renew)

    def book_renew(self):
        self.ui_book_renew.show()

# 待完善
    def all_renew(self):
        """
        根据学号续借所有已借图书
        :return:
        """
        all_renew = self.borrow_list.addInformLast(self.stu_id)
        if all_renew:
            QMessageBox.information(self, "提醒", "您已续借所有已借图书！")
        else:
            QMessageBox.information(self, "提醒", "您暂未借阅图书！")

    def show_borrow_info(self):
        self.model.setHorizontalHeaderLabels(['书名', '借阅日期', '应还日期'])

        borrow_info = self.borrow_list.getInformByStudNo(self.stu_id)
        if borrow_info is False:
            borrow_info = []
        for row, linedata in enumerate(borrow_info):
            for column, itemdata in enumerate(linedata):
                item = QStandardItem(str(itemdata)) if itemdata is not None else QStandardItem('')
                item.setEditable(False)

                self.model.setItem(row, column, item)

        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 布局


class Ui_book_renew(QDialog, Ui_Dialog_renew):
    """图书续借"""

    def __init__(self, stu_id):
        super(Ui_book_renew, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.stu_id = stu_id
        self.borrow_list = BorrowInformList('system.db')

        # button槽函数
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.renew)

# 待完善
    def renew(self):
        """
        根据学号、书号续借指定已借图书
        :return:
        """
        book_id = self.lineEdit.text()

        renew = 1
        if book_id:
            if renew:
                QMessageBox.information(self, "提醒", "您暂未借阅该图书！")
            else:
                QMessageBox.information(self, "提醒", "您已续借xx图书！")
        else:
            QMessageBox.information(self, "提醒", "请输入书号！")


class Ui_book_borrow(QDialog, Ui_Dialog_book_borrow):
    """图书借阅"""

    def __init__(self, stu_id):
        super(Ui_book_borrow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.stu_id = stu_id
        self.borrow_list = BorrowInformList('system.db')

        # button槽函数
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.borrow)

# 待完善
    def borrow(self):
        """
        根据学号、书号借阅图书
        :return:
        """
        book_id = self.lineEdit.text()
        # 待调用函数
        QMessageBox.information(self, "提醒", "您已借阅xx图书！")


class Ui_book_return(QDialog, Ui_Dialog_book_return):
    """图书归还"""

    def __init__(self, stu_id):
        super(Ui_book_return, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.stu_id = stu_id
        self.borrow_list = BorrowInformList('system.db')

        # button槽函数
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.book_return)

# 待完善
    def book_return(self):
        """
        根据书号归还图书
        :return:
        """
        book_id = self.lineEdit.text()
        comment = self.textEdit.toPlainText()
        if book_id:
            self.borrow_list.deleteInform(self.stu_id, book_id)
            QMessageBox.information(self, "提醒", "您已归还xx图书！")
        else:
            QMessageBox.information(self, "提醒", "请输入书号！")


class Ui_book_search(QWidget, Ui_Widget_book_search):
    """图书查询"""

    def __init__(self, stu_id):
        super(Ui_book_search, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.stu_id = stu_id
        self.book_list = BookList('system.db')

        self.model = QStandardItemModel(10, 8)  # 图书信息
        self.show_book_info()

        self.ui_book_subscribe = Ui_book_subscribe(self.stu_id)    # 预约界面
        self.ui_book_read = Ui_book_read()   # 图书浏览界面

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.book_subscribe)
        self.pushButton_3.clicked.connect(self.book_read)
        self.pushButton_4.clicked.connect(self.query)

    def book_subscribe(self):
        self.ui_book_subscribe.show()

    def book_read(self):
        self.ui_book_read.show()

# 待完善
    def query(self):
        self.model.setHorizontalHeaderLabels(['书号', '书名', '作者', '出版社',
                                              '出版日期', '馆藏复本', '已借副本', '图书评论'])

        book_info = []
        Type = self.comboBox.currentText()
        if Type == '书名':
            book_info = self.book_list.getBookByName(self.lineEdit.text())
        if Type == '书号':
            book_info = self.book_list.getBookByNo(self.lineEdit.text())
        if Type == '作者':
            book_info = self.book_list.getBookByAuthor(self.lineEdit.text())
        if Type == '出版社':
            book_info = self.book_list.getBookByPublisher(self.lineEdit.text())

        if book_info is False:
            book_info = []
        for row, linedata in enumerate(book_info):
            for column, itemdata in enumerate(linedata):
                item = QStandardItem(str(itemdata)) if itemdata is not None else QStandardItem('')
                item.setEditable(False)

                self.model.setItem(row, column, item)

        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 布局
        QMessageBox.information(self, "提醒", "查询xx图书！")

# 待完善
    def show_book_info(self):
        self.model.setHorizontalHeaderLabels(['书号', '书名', '作者', '出版社',
                                              '出版日期', '馆藏复本', '已借副本', '图书评论'])

        book_info = self.book_list.getDBInfo()
        if book_info is None:
            book_info = []
        for row, linedata in enumerate(book_info):
            for column, itemdata in enumerate(linedata):
                item = QStandardItem(str(itemdata)) if itemdata is not None else QStandardItem('')
                item.setEditable(False)

                self.model.setItem(row, column, item)

        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 布局


class Ui_book_subscribe(QDialog, Ui_Dialog_subscribe):
    """图书预约"""

    def __init__(self, stu_id):
        super(Ui_book_subscribe, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        self.stu_id = stu_id

        # button槽函数
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.subscribe)

# 待完善
    def subscribe(self):
        """
        根据学号、书号续借指定已借图书
        :return:
        """
        book_id = self.lineEdit.text()

        subscribe = 3
        if subscribe == 1:
            QMessageBox.information(self, "提醒", "暂未订购该图书！")
        if subscribe == 2:
            QMessageBox.information(self, "提醒", "该图书无可借复本！")
        else:
            QMessageBox.information(self, "提醒", "您已预约xx图书！")


class Ui_book_read(QDialog, Ui_Dialog_read):
    """在线浏览"""

    def __init__(self):
        super(Ui_book_read, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")

        # self.book_read = BookList('system.db')

        # button槽函数
        self.pushButton.clicked.connect(self.book_read)

# 待完善
    def book_read(self):
        QMessageBox.information(self, "提醒", "您正在浏览xx图书！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_student_main = Ui_stu('001')
    ui_student_main.show()
    sys.exit(app.exec_())
