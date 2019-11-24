from list.BookList import BookList
from models.Book import Book
from util import Error, Success


class BookManagerService(object):

    def __init__(self, database_name):
        """
        学生服务类，提供程序的各项功能
        :param database_name:
        """
        self.booklist = BookList(database_name)

    def addBook(self, no, name, author, publisher, bookCnt, pubTime, comment=None):
        if comment == None:
            comment= ''
        other = Book(no, name, author, publisher, bookCnt, 0, pubTime, comment)
        self.booklist.addBook(other)

    def getBookByNo(self, no):
        """
        使用书号，获取书籍信息
        :param no: 书号
        :return: 书籍信息的列表
                @see$Error.NoneBook: 书籍不存在
        """
        return self.booklist.getBookByNo(no)

    def getBookByName(self, name):
        """
        使用书名，查找书籍信息
        :param name: 书名
        :return: 返回书籍信息列表
                @see$Error.Nonebook: 书籍信息不存在
        """
        return self.booklist.getBookByParam('bookName', name)

    def getBookByAuthor(self, author):
        """
        使用书名，查找书籍信息
        :param name: 书名
        :return: 返回书籍信息列表
                @see$Error.Nonebook: 书籍信息不存在
        """
        return self.booklist.getBookByParam('author', author)

    def getBookByPublisher(self, publisher):
        """
        使用书名，查找书籍信息
        :param name: 书名
        :return: 返回书籍信息列表
                @see$Error.Nonebook: 书籍信息不存在
        """
        return self.booklist.getBookByParam('publisher', publisher)

    def getBookByPubTime(self, time):
        """
        使用发布时间，查找书籍信息
        :param time: 发布时间
        :return: 返回书籍信息列表
                @see$Error.Nonebook: 书籍信息不存在
        """
        return self.booklist.getBookByParam('pubTime', time)

    def modifyBookName(self, no, name):
        if self.booklist.getBookByNo(no) == Error.NoneBook:
            return Error.NoneBook
        self.booklist.modifyBookByParam('bookName', no, name)
        return Success.FinishModify

    def modifyBookAuthor(self, no, author):
        if self.booklist.getBookByNo(no) == Error.NoneBook:
            return Error.NoneBook
        self.booklist.modifyBookByParam('author', no, author)
        return Success.FinishModify

    def modifyBookPublisher(self, no, publisher):
        if self.booklist.getBookByNo(no) == Error.NoneBook:
            return Error.NoneBook
        self.booklist.modifyBookByParam('author', no, publisher)
        return Success.FinishModify

    def modifyBookPubTime(self, no, pubTime):
        if self.booklist.getBookByNo(no) == Error.NoneBook:
            return Error.NoneBook
        self.booklist.modifyBookByParam('pubTime', no, pubTime)
        return Success.FinishModify

    def displayAllBook(self):
        return self.booklist.outputBookList()

    def addBookByPatch(self, filename):
        if filename[-3:] != '.txt':
            return Error.FileNameFalse
        self.booklist.addBookByFile(filename)
        return Success.FinishAddBook

if __name__ == '__main__':
    book = BookManagerService('../system.db')
    book.getBookByNo('XW3001').pop(0).print()
    book.getBookByName('史').pop(0).print()
    book.modifyBookPubTime('XW3001', '2001-10-1')
    book.getBookByNo('XW3001').pop(0).print()
