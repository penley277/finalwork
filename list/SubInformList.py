from DButil.DBO import DBO
from list.InformList import InformList
from models.SubInform import SubInform


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
            return False
        self.db.insert_values('subInfo', [other.getNo(), other.getStuNo(),
                                          other.getBookNo(), other.getTime()])

    def deleteInform(self, stuno, bookno):
        """
        根据学号删除所有的预订信息
        :param no: 学号
        :return:
        """
        self.db.delete_values('subInfo', '%s%s%s%s%s' % ('where studNo=\'', stuno, '\' and bookNo=\'',bookno, '\''))

    def getInformByStudNo(self, no):
        select = self.db.select_items('subInfo', '*', '%s%s%s' % ('where studNo=\'', no, '\''))
        i = 0
        bi = []
        while i < len(select):
            bi.append(SubInform(select[i][0], select[i][1], select[i][2], select[i][3]))
            i = i + 1
        if len(select) == 0:
            return None
        return bi

    def getInformByBookNo(self, no):
        select = self.db.select_items('subInfo', '*', '%s%s%s' % ('where bookNo=\'', no, '\''))
        i = 0
        bi = []
        while i < len(select):
            bi.append(SubInform(select[i][0], select[i][1], select[i][2], select[i][3]))
            i = i + 1
        if len(select) == 0:
            return None
        return bi

    def getInformByTime(self, time):
        select = self.db.select_items('subInfo', '*', '%s%s%s' % ('where borrowTime=\'', time, '\''))
        i = 0
        bi = []
        while i < len(select):
            bi.append(SubInform(select[i][0], select[i][1], select[i][2], select[i][3]))
            i = i + 1
        if len(select) == 0:
            return None
        return bi

    def getPreTime(self):
        pass

    def closeDB(self):
        self.db.close_database()