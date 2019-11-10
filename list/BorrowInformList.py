from list.InformList import InformList


class BorrowInformList(InformList):

    def __init__(self, borrowList = None):
        if borrowList is None:
            borrowList = []
        self.borrowList = borrowList

    def addInform(self, other):
        self.borrowList.append(other)

    def deleteInform(self, other):
        self.borrowList.remove(other)





