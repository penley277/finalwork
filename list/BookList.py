from DButil.DBO import DBO
from models.Book import Book
from util import Time


class BookList(object):

    def __init__(self, bookList):
        self.db = DBO(bookList)

    def getDBInfo(self):
        self.db.get_table_info('book')

    def addBook(self, other):
        self.db.insert_values('book', [other.getBookNo(), other.getBookName(),
                                       other.getAuthor(), other.getPublisher(),
                                       other.getBookCnt(), other.getBorrowCnt(),
                                       other.getPubTime().getYear(), other.getPubTime().getMonth(),
                                       other.getPubTime().getDay()," "])

    def getBookByName(self, name):
        """
        通过书籍的名字，获取书籍
        :param name: 书籍的名字
        :return: 返回书籍
        """
        return self.db.select_items('book', '*', '%s%s%s' % ('where bookName=\'', name, '\''))

    def getBookByNo(self, num):
        """
        通过书籍的书号，获取书籍
        :param num: 书籍的书号
        :return: 返回书籍
        """
        return self.db.select_items('book', '*', '%s%s%s' % ('where bookNum=\'', num, '\''))

    def removeBook(self, num):
        """
        从数据库中删除图书
        :param num: 删除图书的书号
        :return:
        """
        self.db.delete_values('book', '%s%s%s' % ('where bookNum=\'', num, '\''))

    def addBookByFile(self, filename):
        pass

    def outputBookList(self):
        """
        输出书籍列表中的所有信息
        :return: 无
        """
        pass



if __name__ == '__main__':
    booklist = BookList('system.db')
    booklist.removeBook('XW3002')
