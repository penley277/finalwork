from models.Manager import Manager
from list.StudentList import StudentList


class StuManager(Manager):
    studentlist = StudentList()

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
        添加一个学生
        :param object: 学生类型
        :return: 无
        """
        self.studentlist.addStu(object)

    def importObject(self, object):
        pass
