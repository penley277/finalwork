from DButil.DBO import DBO
from list.InformList import InformList


class SubInformList(InformList):

    def __init__(self, subInfo):
        self.db = DBO(subInfo)

    def addInform(self, other):
        self.db.insert_values('subInfo', [other.getNo(), other.getStuNo(), other.getBookNo(), other.getTime()])

    def getInformByStudNo(self, no):
        self.db.select_items('subInfo', '*', '%s%s%s' % ('where studNo=\'', no, '\''))

    def getInformByBookNo(self, no):
        self.db.select_items('subInfo', '*', '%s%s%s' % ('where bookNo=\'', no, '\''))

    def getInformByTime(self, time):
        self.db.select_items('subInfo', '*', '%s%s%s' % ('where borrowTime=\'', time, '\''))

    def getPreTime(self):
        pass