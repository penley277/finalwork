from util.util import Time


class Book(object):
    """
    书籍类包含了书籍的信息
    """
    def __init__(self, bookNo, bookName, author, publisher,
                 bookCnt, borrowCnt, pubTime, comment=None):
        """
        书籍类的初始化函数
        :rtype: object
        :param bookNo: 书号
        :param bookName: 书名
        :param author: 书籍作者
        :param bookCnt: 馆藏数量
        :param borrowCnt: 借阅次数
        :param pubTime: 出版时间
        :param comment: 书籍评论
        """
        self.bookNo = bookNo
        self.bookName = bookName
        self.author = author
        self.publisher = publisher
        self.bookCnt = bookCnt
        self.borrowCnt = borrowCnt
        self.pubTime = pubTime
        self.comment = comment

    def getBookNo(self):
        """
        获取书号
        :return: 书号
        """
        return self.bookNo

    def setBookNo(self, bookNo):
        """
        设置书号
        :param bookNo: 书号
        :return: 无
        """
        self.bookNo = bookNo

    def getBookName(self):
        """
        设置书籍名字
        :return: 返回书籍的名字
        """
        return self.bookName

    def setBookName(self, bookName):
        """
        设置书籍名字
        :param bookName: 想要设置的书籍名
        :return: 无
        """
        self.bookName = bookName

    def getAuthor(self):
        """
        返回作者名
        :return: 作者名字
        """
        return  self.author

    def setAuthor(self, author):
        """
        设置书籍作者名字
        :param author: 想要设置的作者名字
        :return: 无
        """
        self.author = author


    def getPublisher(self):
        return self.publisher


    def setPublisher(self, pub):
        self.publisher = pub

    def getBookCnt(self):
        """
        获取书籍的数量
        :return: 书籍数量
        """
        return  self.bookCnt

    def setBookCnt(self, bookCnt):
        """
        设置书籍的数量
        :param bookCnt: 想要设置的书籍数量
        :return: 无
        """
        self.bookCnt = bookCnt

    def getBorrowCnt(self):
        """
        获取借阅的书籍的次数
        :return: 借阅书籍的次数
        """
        return  self.borrowCnt

    def setBorrowCnt(self, borrowCnt):
        """
        :param borrowCnt: 设置书籍的借阅数量
        :return: 无
        """
        self.borrowCnt = borrowCnt

    def getPubTime(self):
        """
        获取书籍的出版时间
        :return: 书籍的出版时间
        """
        return self.pubTime

    def setPubTime(self, pubTime):
        """
        设置书籍的出版时间
        :param pubTime: 书籍的出版时间
        :return: 无
        """
        self.pubTime = pubTime

    def getComment(self):
        """
        获取书籍的评论
        :return:
        """
        return self.comment

    def setComment(self, comment):
        """
        对书籍进行评论
        :param comment:书籍评论
        :return:无
        """
        self.comment = comment

    def print(self):
        spaces = "      "
        print(self.bookNo, spaces, self.bookName, spaces,
              self.bookCnt, spaces, self.borrowCnt, spaces,
              self.pubTime)

