from list.SubInformList import SubInformList
from list.BookList import BookList
from list.BorrowInformList import BorrowInformList
from util import Error, Success


class StudentService(object):

    def __init__(self, database_name):
        """
        学生服务类，提供程序的各项功能
        :param database_name:
        """
        self.borrowlist = BorrowInformList(database_name)
        self.booklist = BookList(database_name)
        self.sublist = SubInformList(database_name)

    def borrowBook(self, stuno, bookno):
        """
        图书借阅功能
        :param stuno: 借阅学生的学号
        :param bookno: 借阅的书号
        :return: @see$Error.NoneBook : 没有这本书的借阅信息
                 @see$Error.FinishBorrow : 借阅成功
        """
        book = self.booklist.getBookByNo(bookno)
        if book is Error.NoneBook:
            return Error.NoneBook

        if self.borrowlist.getInformByStudNoBookNo(stuno, bookno) is Error.NoBorrowInform:
            book = book.pop(0)
            self.borrowlist.addInformByNos(stuno, bookno)
            self.booklist.updateBorrowAndCnt(bookno, book.getBookCnt()-1, book.getBorrowCnt()+1)
            return Success.FinishBorrow

        return Error.ExitBorrowInform

    def returnBookWithComment(self, stuno, bookno, comment=None):
        """
        归还书籍
        :param stuno: 归还学生的学号
        :param bookno: 归还学生的书号
        :param comment: 归还时给予的评价
        :return: @see$Error.NoneBook : 没有这本书的借阅信息
                 @see$Error.BookCnt0: 书籍已经借空，不能借阅
                 @see$Error.FinishReturn: 归还书籍成功
        """
        book = self.booklist.getBookByNo(bookno)

        # 查看书籍是否存在
        if book is Error.NoneBook:
            return Error.NoneBook
        book = self.booklist.getBookByNo(bookno).pop(0)

        # 图书是否已经借空
        if book.getBookCnt() == 0:
            return Error.BookCnt0

        # 删除借阅记录
        self.borrowlist.deleteInform(stuno, bookno)

        # 评价内容
        if comment is not None: # 如果没有给评价
            self.booklist.setComment(book.getBookNo(), comment)
        return Success.FinishReturn

    def renewBook(self, stuno, bookno):
        """
        续借单本书籍
        :param stuno: 学号
        :param bookno: 书号
        :return: @see$Error.NoneBook : 没有这本书
                 @see$Error.FinishRenew： 续借成功
                 @see$Error.NoBorrowInform: 没有这条借阅信息
        """
        book = self.booklist.getBookByNo(bookno)
        if book == Error.NoneBook:
            return Error.NoneBook

        list = self.borrowlist.getInformByStudNoBookNo(stuno, bookno)

        # 如果借阅信息存在
        if list != Error.NoBorrowInform:
            borrow = list.pop(0)
            self.borrowlist.addInformLast(borrow)
            return Success.FinishRenew

        return Error.NoBorrowInform

    def renewAllBook(self, stuno):
        """
        续借单本书籍
        :param stuno: 学号
        :return: @see$Error.NoBorrowInform : 没有这本书的借阅信息
                 @see$Error.FinishRenew： 续借成功
        """

        list= self.borrowlist.getInformByStudNo(stuno)
        if list == Error.NoBorrowInform:
            return Error.NoBorrowInform
        i = 0
        while i < len(list):
            self.borrowlist.addInformLast(list.pop(i))
            i = i+1
        return Success.FinishRenew

    def getTopBooks(self):
        """
        获取借阅量排名前十的书籍
        :return: bi: Book的列表
                cnt：对应书籍的借阅数量
        """
        top =  self.borrowlist.topTenByCnt()
        i = 0
        bi = []
        cnt = []
        while i < 10:
            book = self.booklist.getBookByNo(top[i][0])
            if book != Error.NoneBook:
                book = self.booklist.getBookByNo(top[i][0]).pop(0)
                bi.append(book)
                cnt.append(top[i][1])
            else:
                bi.append('')
                cnt.append(' ')
            i = i + 1
        return bi, cnt

    def getNewBooks(self):
        """
        获取最新书籍
        :return: 返回Book的列表
        """
        return self.booklist.topTenByTime()

    def subBook(self, stuno, bookno):
        """
        预约书籍
        :param stuno:
        :param bookno:
        :return: @see$Error.NoneBook : 没有这本书
                 @see$Error.NoBorrowInform: 没有这条借阅信息
        """
        book = self.booklist.getBookByNo(bookno)
        if book is False:
            return Error.NoneBook

        return self.sublist.addInformByNos(stuno, bookno)



if __name__ == '__main__':
    stu = StudentService('../system.db')
    print(stu.subBook('1113000004', 'XW3004'))

    b, t = stu.getTopBooks()
    b.pop(0).print()
    t.pop(0)

