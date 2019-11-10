class SubInform(object):
    """
    预约信息的类，包含了学生进行预约的信息，是数据库中的一个表
    """

    def __init__(self, stuNo, bookNo, time):
        """
        预约信息的类
        :param stuNo: 学好
        :param bookNo: 书号
        :param time: 预约时间
        """
        self.stuNo = stuNo
        self.bookNo = bookNo
        self.time = time

    def getStuNo(self):
        """
        获取预约的学生
        :return: 返回学生的学号
        """
        return self.stuNo

    def setStuNo(self, stuNo):
        """
        更改预约信息中的学生学号
        :param stuNo: 想要改为的学生学号
        :return: 无
        """
        self.stuNo = stuNo

    def getBookNo(self):
        """
        获取预约的书号
        :return: 书号
        """
        return self.bookNo

    def setBookNo(self, bookNo):
        """
        更改书号
        :param bookNo: 想要改为的书号
        :return: 无
        """
        self.bookNo = bookNo

    def getTime(self):
        """
        获得预约时间
        :return: 预约时间
        """
        return self.time

    def setTime(self, time):
        """
        设置预约时间
        :param time:
        :return: 无
        """
        self.time = time
