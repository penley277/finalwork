
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
        book = self.bookList.getBookByNo(other.getBookNo())
        student = self.studList.getStuByNo(other.getStuNo)

        if book.getBookCnt() == 0:
            return False
        self.db.update_values('book',{'bookCnt':book.getBookCnt()-1, 'borrowCnt': book.getBorrowCnt()+1}, '%s%s%s' % ('where bookNum=\'', other.getBookNo(), '\''))
        self.db.insert_values('borrowInfo',[other.getNo(), other.getStuNo(), other.getBookNo(), other.getBorrowTime(),
                                            other.getFinishTime()])
        return True

    def deleteInform(self, no):
        self.db.delete_values('borrowInfo', '%s%s%s' % ('where studNo=\'', no, '\''))

    def getInformByStudNo(self, no):
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

        :param time:
        :return:
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