import datetime

from DButil.DBO import DBO
from models.Book import Book


class BookList(object):

    def __init__(self, db):
        self.db = DBO(db)

    def getDBInfo(self):
        self.db.get_table_info('book')

    def addBook(self, other):
        self.db.insert_values('book', [other.getBookNo(), other.getBookName(),
                                       other.getAuthor(), other.getPublisher(),
                                       other.getBookCnt(), other.getBorrowCnt(),
                                       other.getPubTime(), " "])

    def getBookByName(self, name):
        """
        通过书籍的名字，获取书籍
        :param name: 书籍的名字
        :return: 返回书籍
        """
        select = self.db.select_items('book', '*', '%s%s%s' % ('where bookName=\'', name, '\''))
        if len(select) == 0:
            return None
        return Book(select[0][0], select[0][1], select[0][2], select[0][3], select[0][4], select[0][5],
                    select[0][6], select[0][7])

    def getBookByNo(self, num):
        """
        通过书籍的书号，获取书籍
        :param num: 书籍的书号
        :return: 返回书籍
        """
        select = self.db.select_items('book', '*', '%s%s%s' % ('where bookNum=\'', num, '\''))
        if len(select) == 0:
            return None
        return Book(select[0][0], select[0][1], select[0][2], select[0][3], select[0][4], select[0][5],
                    select[0][6], select[0][7])

    def getBookByAuthor(self, author):
        """
        通过书籍的书号，获取书籍
        :param author: 作者
        :param num: 书籍的书号
        :return: 返回书籍
        """
        select = self.db.select_items('book', '*', '%s%s%s' % ('where author=\'', author, '\''))
        if len(select) == 0:
            return None
        return Book(select[0][0], select[0][1], select[0][2], select[0][3], select[0][4], select[0][5],
                    select[0][6], select[0][7])

    def removeBook(self, num):
        """
        从数据库中删除图书
        :param num: 删除图书的书号
        :return:
        """
        self.db.delete_values('book', '%s%s%s' % ('where bookNum=\'', num, '\''))

    def getBookByPublisher(self, publisher):
        """
        通过书籍的书号，获取书籍
        :param author: 作者
        :param num: 书籍的书号
        :return: 返回书籍
        """
        select = self.db.select_items('book', '*', '%s%s%s' % ('where publisher=\'', publisher, '\''))

        if len(select) == 0:
            return None

        i = 0
        bi = []
        while i < len(select):
            bi.append(Book(select[0][0], select[0][1], select[0][2], select[0][3], select[0][4], select[0][5],
                           select[0][6], select[0][7]))
            i = i + 1
        return bi

    def setComment(self, no, comment):
        book = self.getBookByNo(no)
        if book.getComment() is None:
            self.db.update_values('book', {'comment': comment+'`'},
                                  '%s%s%s' % ('where bookNum=\'', no, '\''))
        else:
            self.db.update_values('book', {'comment': str(book.getComment())+comment+'`'},
                              '%s%s%s' % ('where bookNum=\'', no, '\''))

    def outputBookList(self):
        """
        输出所有的图书信息
        :return: 所有图书的信息，保存在元组
        """
        select = self.db.select_items('book', '*')
        if len(select) == 0:
            return None
        return select

    def topTenByTime(self):
        pass

    def addBookByFile(self, filename):
        """
        从文件批量添加书籍到数据库中
        :param filename:文件名字
        :return:无
        """
        with open(filename, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()
                if not lines:  # 读取到最后一行，停止读取操作
                    break
                    pass

                no, name, author, publisher, borrow, left, year, month, day = [i for i in lines.split()]  # 根据空格，将值读出
                book = Book(no, name, author, publisher, int(borrow), int(left),  # 将读取的值设置为一个对象
                            datetime.date(int(year), int(month), int(day)).isoformat())
                self.addBook(book)
        file_to_read.close()


if __name__ == '__main__':
    b = BookList('system.db')
    b.getBookByNo('XW3032').print()
    b.setComment('XW3031', '很好')
    b.setComment('XW3031', '很棒')
