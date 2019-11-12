from models.Manager import Manager


class AdminManager(Manager):

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
        self.type = type
