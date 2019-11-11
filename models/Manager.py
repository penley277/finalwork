import abc


class Manager(object):
    """
    抽象的管理员类，可以从管理员类中分别实现
    学生管理员和图书管理员
    """

    def __init__(self, managerID=None, name=None, phone=None, passwd=None, type = None):
        """
        :param managerID: 管理员ID
        :param name:  管理员名字
        :param phone:  管理员手机号
        :param passwd: 密码
        :param type: 管理员类型
        """
        self.managerID = managerID
        self.name = name
        self.phone = phone
        self.passwd = passwd
        self.type = type

    def getManagerId(self):
        """
        获取管理员id
        :return: 管理员id
        """
        return self.managerID

    def setManagerId(self, id):
        """
        获取管理员id
        :return: 管理员id
        """
        self.managerID = id

    def getName(self):
        """
        获取管理员名字
        :return: 名字
        """
        return self.name

    def setName(self, name):
        """
        设置管理员名字
        :param name: 想要设置的姓名
        :return: 无
        """
        self.name = name

    def getPhone(self):
        """
        获取手机号
        :return: 手机号
        """
        return self.phone

    def setPhone(self, phone):
        """
        设置手机号
        :param phone: 想要设置的手机号
        :return: 无
        """
        self.phone = phone

    def setPasswd(self, passwd):
        """
        更改密码
        :param passwd: 想要改为的密码
        :return: 无
        """
        self.passwd = passwd

    def getPasswd(self):
        """
        更改密码
        :param passwd: 想要改为的密码
        :return: 无
        """
        return self.passwd

    def getType(self):
        """
        获取管理员类型
        :return: 管理员类型
        """
        return self.type

    def setType(self, type):
        """
        设置管理员类型
        :param type:
        :return: 无
        """
        self.type = type