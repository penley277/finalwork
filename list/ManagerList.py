class ManagerList(object):

    def __init__(self, managerList=None):
        if managerList is None:
            managerList = []
        self.managerList = managerList

    def addManager(self, object):
        self.managerList.append(object)

    def getManagerById(self, id):
        i = 0
        while i < len(self.managerList):
            if self.managerList[i].getManagerId() == id:
                return self.managerList[i]
            i = i + 1
        return None

    def getManagerIndexById(self, id):
        i = 0
        while i < len(self.managerList):
            if self.managerList[i].getManagerId() == id:
                return i
            i = i+1
        return -1