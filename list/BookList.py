from DButil.DBO import DBO
from models.Book import Book


class BookList(object):

    def __init__(self, bookList):
        self.db = DBO(bookList)

    def addBook(self, other):
        sql = 'insert into book (no, name) values (?,?)'
        self.db.executeUpdate(sql, other)

    def getBookByName(self, name):
        """
        通过书籍的名字，获取书籍
        :param name: 书籍的名字
        :return: 返回书籍
        """
        sql = 'select * from book where name=?'
        self.db.executeQuery(sql, name)

    def getBookByNo(self, num):
        """
        通过书籍的书号，获取书籍
        :param num: 书籍的书号
        :return: 返回书籍
        """
        sql = 'select * from book where num=?'
        self.db.executeQuery(sql, num)

    def removeBook(self, bookNum):
        sql = "DELETE from book where bookNum=?"
        self.db.executeDelete(sql, bookNum)


    def addBookByFile(self, filename):
        pass

    def outputBookList(self):
        """
        输出书籍列表中的所有信息
        :return: 无
        """
        pass

