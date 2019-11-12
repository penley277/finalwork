from DButil.DBO import DBO
from list.InformList import InformList


class BorrowInformList(InformList):

    def __init__(self, borrowList):
        self.db = DBO(borrowList)

    def addInform(self, other):
        self.db.insert_values('borrowInfo',[])

    def deleteInform(self, other):
        pass