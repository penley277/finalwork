
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

    def addInform(self, other):
        book = self.bookList.getBookByNo(other.getBookNo()) # 根据书号，获取书籍
        student = self.studList.getStuByNo(other.getStuNo) # 根据学生号，获取学生名

        if book.getBookCnt() == 0:
            return False
        self.db.update_values('book',['bookCnt',book.getBookCnt()-1, 'borrowCnt', book.getBorrowCnt()+1], '%s%s%s' % ('where bookNum=\'', other.getBookNo(), '\''))
        self.db.insert_values('borrowInfo',[other.getNo(), other.getStuNo(), other.getBookNo(), other.getBorrowTime(),
                                            other.getFinishTime()])
        return True

    def deleteInform(self, no):
        """
        从列表中删除某个学生所有的借阅信息
        :param no: 学生的学号
        :return:用于进行学生书籍的批量归还
        """
        self.db.delete_values('borrowInfo', '%s%s%s' % ('where studNo=\'', no, '\''))

    def getInformByStudNo(self, no):
        """
        获取某个学生所有的借阅信息，通过书名进行查看
        :param no: 学生学号
        :return: 如果学生
        """
        select = self.db.select_items('borrowInfo',  '*', '%s%s%s' % ('where studNo=\'', no, '\''))
        i = 0
        bi = []
        print(len(select))
        while i < len(select):
            bi.append(BorrowInfo(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i+1
        if len(select) == 0:
            return None
        return bi

    def getInformByBookNo(self, no):
        """
        通过书号，获取所有这本书所有的借阅信息
        :param no: 书号
        :return: 如果这本书不存在借阅历史或者这本书不存在，将会返回None；否则，将获取所有的借阅信息
        """
        select = self.db.select_items('borrowInfo',  '*', '%s%s%s' % ('where bookNo=\'', no, '\''))
        i = 0
        bi = []

        while i < len(select):
            bi.append(BorrowInfo(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1
        if len(select) == 0:
            return None
        return bi

    def getInformByTime(self, time):
        """
        通过时间获取借阅信息列表中的内容
        :param time: 想要获取的日期时间
        :return: 返回借阅信息列表
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


if __name__ == '__main__':
    borrow = BorrowInformList()
    other1 = BorrowInfo(2, 'wx101', 'sdsd', '1995/10/12', '1995/11/12')
    other2 = BorrowInfo(3, 'wx101', 'sdsd', '1995/10/12', '1995/11/12')
    other3 = BorrowInfo(4, 'wx101', 'sdsd', '1995/10/12', '1995/11/12')

    print(borrow.getInformByBookNo('sdsd')[0].getNo())