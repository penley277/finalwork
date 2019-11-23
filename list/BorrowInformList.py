import string

from DButil.DBO import DBO
from list.InformList import InformList
from list.StudentList import StudentList
from list.BookList import BookList
import datetime

from models.BorrowInfo import BorrowInfo
import random

from util import Error, Success


class BorrowInformList(InformList):

    def __init__(self, database_name):
        """
        初始化，链接数据库
        :param database_name: 数据库名字
        """
        self.db = DBO(database_name)
        self.bookList = BookList(database_name)
        self.studList = StudentList(database_name)
        self.history = [] # 借阅历史的buffer

    def addInform(self, other):
        """
        添加借阅信息
        :param other: 添加借阅信息的内容
        :return: 添加成功，返回True; 否则返回False
        """
        book = self.bookList.getBookByNo(other.getBookNo())
        if book is False:
            return Error.NoneBook

        student = self.studList.getStuByNo(other.getStuNo())

        if book.getBookCnt() == 0:  # 如果书籍已经借空
            return Error.BookCnt0

        other.setNo(''.join(random.sample(string.digits * 5 + string.ascii_letters * 4, 20)))
        self.db.insert_values('borrowInfo', [other.getNo(), other.getStuNo(), other.getBookNo(), other.getBorrowTime(),
                                             other.getFinishTime()])
        self.db.update_values('book', {'bookCnt': book.getBookCnt() - 1, 'borrowCnt': book.getBorrowCnt() + 1},
                              '%s%s%s' % ('where bookNum=\'', other.getBookNo(), '\''))
        return Success.FinishBorrow

    def deleteInform(self, stuno, bookno):
        """
        删除借阅信息，使用学生和书号，删除借阅信息
        :param stuno: 学生学号
        :param bookno: 书籍书号
        :return: 删除成功返回True， 否则返回False
        """
        book = self.bookList.getBookByNo(bookno)

        # 通过操纵数据库删除信息
        self.db.delete_values('borrowInfo', '%s%s%s%s%s' % ('where studNo=\'', stuno, '\' and bookNo=\'',bookno, '\''))
        # 更新借阅数量和剩余数量
        self.db.update_values('book', {'bookCnt': book.getBookCnt() + 1, 'borrowCnt': book.getBorrowCnt() - 1},
                              '%s%s%s' % ('where bookNum=\'', book.getBookNo(), '\''))

        return Success.FinishReturn

    def getInformByStudNo(self, no):
        """
        根据学号，列出所有的借阅书籍
        :param no: 学生学号
        :return: 获取到信息，返回借阅信息数组; 如果没有得到信息，返回None
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where studNo=\'', no, '\''))
        i = 0
        bi = []

        # 如果没有选择到信息，返回空
        if len(select) == 0:
            return Error.NoBorrowInform

        while i < len(select):
            bi.append(BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1
        return bi

    def getInformByBookNo(self, no):
        """
        根据书号列出所有的借阅书籍
        :param no: 书号
        :return: 获取到信息，返回借阅信息数组; 如果没有得到信息，返回None
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where bookNo=\'', no, '\''))

        if len(select) == 0:
            return Error.NoBorrowInform
        i = 0
        bi = []
        while i < len(select):
            bi.append(BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1

        return bi

    def getInformBybTime(self, time):
        """
        根据借阅时间列出借阅信息
        :param time:时间格式为yyyy/mm/dd
        :return: 返回借阅信息
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where borrowTime=\'', time, '\''))
        if len(select) == 0:  # 没有查询到记录
            return Error.NoBorrowInform

        i = 0
        bi = []
        while i < len(select):  # 将查询到的记录转化为借阅信息类
            bi.append(BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1

        return bi

    def addInformLast(self, stu):
        """
        按照学号续借所有的书籍
        :param stu: 学号
        :param newBTime: 新的借阅时间
        :param newFTime: 新的换书时间
        :return: 需要设置续借信息，如果续借成功，返回True
        """
        list = self.getInformByStudNo(stu)
        if list is False:  # 如果没有查询到借阅信息
            return Error.NoBorrowInform

        i = 0
        while i < len(list):
            # 删除原有的信息
            self.deleteInform(list[i].getStuNo(), list[i].getBookNo())
            # 更新信息
            list[i].setBorrowTime(list[i].getBorrowTime())
            year, month, day = [i for i in list[i].getFinishTime().split('-')]  # 根据空格，将值读出
            time = datetime.date(int(year), int(month), int(day))+ datetime.timedelta(days=30)
            list[i].setFinishTime(time.isoformat())
            self.addInform(list[i])
            i = i + 1
        return Success.FinishBorrow

    def getInformByfTime(self, time):
        """
        根据借阅的结束时间进行查询
        :param time: 结束时间
        :return: 如果没有查询到元素，返回False，否则返回True
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where finishTime=\'', time, '\''))

        if len(select) == 0:  # 没有查询到
            return Error.NoBorrowInform
        i = 0
        bi = []
        while i < len(select):
            bi.append(BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1

        return bi

    def topTenByCnt(self):
        """
        获取借阅量最多的10本书籍
        :return: 返回借阅量由高到低的字典， 包含学生的学号以及借阅的次序
        TODO: 还有问题啊！！！！
        """
        select = self.db.select_items('borrowInfo', '*')

        i = 0
        while i < len(select):
            self.history.append(select[i][2])
            i = i + 1

        dict = {}
        for key in self.history:
            dict[key] = dict.get(key, 0) + 1
        d_order = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        while len(d_order) < 10:  # 如果借阅数量总数不足十个， 加入空格补位置
            d_order.append((' ', ' '))

        return d_order

    def outputInform(self):
        """
        输出所有的借阅信息
        :return: 返回借阅信息的列表
        """
        select = self.db.select_items('borrowInfo', '*')
        i = 0
        bi = []
        while i < len(select):
            binfo = BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4])
            bi.append(binfo)
            i = i + 1
        if len(select) == 0:
            return Error.NoBorrowInform
        return bi

    def closeDB(self):
        """
        关闭数据库的接口
        :return: 无
        """
        self.db.close_database()


if __name__ == '__main__':
    borrow = BorrowInformList('system.db')
    book = BookList('system.db')
    other1 = BorrowInfo('1113000001', 'XW3005', '2019-10-12', '2019-11-12')

    list1 = borrow.topTenByCnt()
    print(list1[0][0], list1[0][1])
    borrow.closeDB()
