from DButil.DBO import DBO
from list.InformList import InformList
import datetime

from models.BorrowInfo import BorrowInfo


class BorrowInformList(InformList):

    def __init__(self, borrowList):
        self.db = DBO(borrowList)

    def addInform(self, other):
        self.db.insert_values('borrowInfo',[other.getNo(), other.getStuNo(), other.getBookNo(), other.getBorrowTime(),
                                            other.getFinishTime()])

    def deleteInform(self, other):
        self.db.delete_values('borrowInfo', '%s%s%s' % ('where studNo=\'', other, '\''))

    def getInformByStudNo(self, no):
        self.db.select_items('borrowInfo',  '*', '%s%s%s' % ('where studNo=\'', no, '\''))

    def getInformByBookNo(self, no):
        self.db.select_items('borrowInfo',  '*', '%s%s%s' % ('where bookNo=\'', no, '\''))

    def getInformByTime(self, time):
        self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where borrowTime=\'', time, '\''))







