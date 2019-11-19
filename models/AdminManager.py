from list.ManagerList import ManagerList


class AdminManager(object):

    def __init__(self, managerID=None, name=None, phone=None, passwd=None, type="admin"):
        """
        StuManager class is the Manager of Student
        :param managerID: the id number of student manager
        :param name:  the name of student manager
        :param phone:  the phone number of the student number
        :param passwd: password
        :param type: type of the manager
        """
        super().__init__(managerID, name, phone, passwd)
        self.managerList = ManagerList('system.db')
        self.type = type

    def addManager(self, other):
        self.managerList.addManager(other)

    def changeTypeofManager(self, id, type):
        self.managerList.changeType(id, type)

    def removeManager(self, id):
        self.managerList.removeManager(id)
