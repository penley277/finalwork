import random
import string

from DButil.DBO import DBO
from list.InformList import InformList
from models.SubInform import SubInform
from util import Error, Success


class SubInformList(InformList):

    def __init__(self, database_name):
        self.db = DBO(database_name)

    def addInform(self, other):
        """
        添加订阅信息
        :param other:
        :return:
        """
        select = self.db.select_items('book', '*', '%s%s%s' % ('where bookNum=\'', other.getBookNo(), '\''))
        if len(select) == 0:
            return Error.NoneBook

        if select[0][4] == 0:
            return Error.BookCnt0

        # 预约id随机生成
        other.setNo(''.join(random.sample(string.digits * 5 + string.ascii_letters * 4, 20)))
        self.db.insert_values('subInfo', [other.getNo(), other.getStuNo(),
                                          other.getBookNo(), other.getTime()])
        return Success.FinishSub


    def deleteInform(self, stuno, bookno):
        """
        根据学号和书号删除某条借阅信息
        :param no: 学号
        :return:
        """
        self.db.delete_values('subInfo', '%s%s%s%s%s' % ('where studNo=\'', stuno, '\' and bookNo=\'', bookno, '\''))

    def getInformByStudNo(self, no):
        select = self.db.select_items('subInfo', '*', '%s%s%s' % ('where studNo=\'', no, '\''))

        if len(select) == 0:
            return None

        i = 0
        bi = []
        while i < len(select):
            bi.append(SubInform(select[i][0], select[i][1], select[i][2], select[i][3]))
            i = i + 1

        return bi

    def getInformByBookNo(self, no):
        select = self.db.select_items('subInfo', '*', '%s%s%s' % ('where bookNo=\'', no, '\''))
        if len(select) == 0:
            return None

        i = 0
        bi = []
        while i < len(select):
            bi.append(SubInform(select[i][0], select[i][1], select[i][2], select[i][3]))
            i = i + 1

        return bi

    def getInformByTime(self, time):
        """
        通过日期选择预约信息
        :param time:
        :return:
        """
        select = self.db.select_items('subInfo', '*', '%s%s%s' % ('where borrowTime=\'', time, '\''))

        if len(select) == 0:
            return None

        i = 0
        bi = []
        while i < len(select):
            bi.append(SubInform(select[i][0], select[i][1], select[i][2], select[i][3]))
            i = i + 1

        return bi

    def getPreTime(self):
        pass

    def closeDB(self):
        self.db.close_database()
