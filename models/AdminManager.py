from models.Manager import Manager
from list.ManagerList import ManagerList


class AdminManager(Manager):
    managerlist = ManagerList()

    def __init__(self, managerID=None, name=None, phone=None, passwd=None, type="stu"):
        """
        StuManager class is the Manager of Student
        :param managerID: the id number of student manager
        :param name:  the name of student manager
        :param phone:  the phone number of the student number
        :param passwd: password
        :param type: type of the manager
        """
        super().__init__(managerID, name, phone, passwd)
        self.type = type

    def addInfo(self, object):
        """
        添加一个管理员
        :param object: 学生类型
        :return: 无
        """
        self.managerlist.addManager(object)

    def importObject(self, object):
        pass

    def changeTypeOfManager(self, managerId, type):
        """
        更改管理员类型
        :param managerId: 管理员的ID
        :param type: 管理员类型
        :return: 无
        """
        self.managerlist.getManagerById(managerId).setType(type)
