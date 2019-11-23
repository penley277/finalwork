import datetime
import time


class BorrowInfo(object):

    def __init__(self, studNo, bookNo, borrowTime, finishTime):
        """
        借阅信息的初始化类型，建立借阅信息
        :param studNo: 学生号
        :param bookNo: 书号
        :param borrowTime: 借阅的开始时间
        :param finishTime: 借阅的结束时间
        """
        self.no = ''
        self.studNo = studNo
        self.bookNo = bookNo
        self.borrowTime = borrowTime
        self.finishTime = finishTime

    def getNo(self):
        return self.no

    def setNo(self, no):
        self.no = no

    def getStuNo(self):
        """
        获取学生号
        :return: 返回学生号
        """
        return  self.studNo

    def setStuNo(self, studNo):
        """
        设置学生号
        :param studNo: 要改为的学生号
        :return: 无
        """
        self.studNo = studNo

    def getBookNo(self):
        """
        获取书号
        :return: 书号
        """
        return  self.bookNo

    def setBookNo(self, bookNo):
        """
        设置书号
        :param bookNo: 要改为的书号
        :return: 无
        """
        self.bookNo = bookNo


    def getBorrowTime(self):
        """
        获取借阅时间
        :return: 借阅时间
        """
        return self.borrowTime

    def setBorrowTime(self, borrowTime):
        """
        设置借阅时间
        :param borrowTime: 要改为的借阅时间
        :return: 借阅时间
        """
        self.borrowTime = borrowTime

    def getFinishTime(self):
        return self.finishTime

    def setFinishTime(self, finishTime):
        """

        :param self:
        :return: 无
        """
        self.finishTime = finishTime

    def getReturnTime(self, startTime):
        year, month, day = [i for i in startTime.split('-')]  # 根据空格，将值读出
        time = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(days=30)
        return time.isoformat()

    def print(self):
        print(self.studNo, self.bookNo, self.borrowTime, self.finishTime)