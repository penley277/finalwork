from DButil.DBO import DBO
from list.InformList import InformList
from list.StudentList import StudentList
from list.BookList import BookList
import datetime

from models.BorrowInfo import BorrowInfo


class BorrowInformList(InformList):

    def __init__(self, database_name):
        self.db = DBO(database_name)
        self.bookList = BookList(database_name)
        self.studList = StudentList(database_name)
        self.history = []

    def addInform(self, other):
        """
        添加借阅信息
        :param other: 添加借阅信息的内容
        :return: 添加成功，返回True; 否则返回False
        """
        book = self.bookList.getBookByNo(other.getBookNo())
        student = self.studList.getStuByNo(other.getStuNo())

        if book.getBookCnt() == 0:  # 如果书籍已经借空
            return False

        self.db.insert_values('borrowInfo', [other.getNo(), other.getStuNo(), other.getBookNo(), other.getBorrowTime(),
                                             other.getFinishTime()])
        self.db.update_values('book', {'bookCnt': book.getBookCnt() - 1, 'borrowCnt': book.getBorrowCnt() + 1},
                              '%s%s%s' % ('where bookNum=\'', other.getBookNo(), '\''))
        return True

    def deleteInform(self, no, comment=None):
        """
        删除借阅信息
        :param comment:
        :param no: 借阅信息序号
        :return: 删除成功返回True， 否则返回False
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where infoId=\'', no, '\''))
        book = self.bookList.getBookByNo(select[0][2])

        if len(select) == 0:
            return None

        self.db.delete_values('borrowInfo', '%s%s' % ('where infoId=', no))
        self.db.update_values('book', {'bookCnt': book.getBookCnt() + 1, 'borrowCnt': book.getBorrowCnt() - 1, 'comment': (float(book.getComment()) + float(comment))/2.0},
                              '%s%s%s' % ('where bookNum=\'', book.getBookNo(), '\''))


    def getInformByStudNo(self, no):
        """
        根据学号，列出所有的借阅书籍
        :param no: 学号
        :return:
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where studNo=\'', no, '\''))
        i = 0
        bi = []

        if len(select) == 0:
            return None
        while i < len(select):
            bi.append(BorrowInfo(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1

        return bi

    def getInformByBookNo(self, no):
        """
        根据书号列出所有的借阅书籍
        :param no: 书号
        :return:
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where bookNo=\'', no, '\''))
        i = 0
        bi = []

        while i < len(select):
            bi.append(BorrowInfo(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1
        if len(select) == 0:
            return None
        return bi

    def getInformBybTime(self, time):
        """
        根据借阅时间列出借阅信息
        :param time:时间格式为yyyy/mm/dd
        :return: 返回借阅信息
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where borrowTime=\'', time, '\''))
        i = 0
        bi = []
        while i < len(select):
            bi.append(BorrowInfo(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1
        if len(select) == 0:
            return None
        return bi

    def addInformLast(self, stu, newBTime, newFTime):
        """
        按照学号续借所有的书籍
        :param stu: 学号
        :param newBTime: 新的借阅时间
        :param newFTime: 新的换书时间
        :return:
        """
        list = self.getInformByStudNo(stu)
        if len(list) == 0:
            return None

        i = 0
        while i < len(list):
            self.deleteInform(list[i].getNo())
            list[i].setBorrowTime(newBTime)
            list[i].setFinishTime(newFTime)
            self.addInform(list[i])
            i = i + 1
        return True

    def getInformByfTime(self, time):
        """
        :param time:
        :return:
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where finishTime=\'', time, '\''))
        if len(select) == 0:
            return None
        i = 0
        bi = []
        while i < len(select):
            bi.append(BorrowInfo(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1

        return bi

    def topTenByCnt(self):

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
            binfo = BorrowInfo(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4])
            i = i + 1
        if len(select) == 0:
            return None
        return bi

    def closeDB(self):
        self.db.close_database()


if __name__ == '__main__':
    borrow = BorrowInformList('system.db')
    book = BookList('system.db')
    other1 = BorrowInfo(2, '1113000001', 'XW3003', '2019/10/12', '2019/11/12')
    borrow.addInform()
    borrow.setComment(2, '5')
    for i in range(10):
        if borrow.topTenByCnt().pop(i)[0] != ' ':
            book.getBookByNo(borrow.topTenByCnt().pop(i)[0]).print()
    borrow.closeDB()