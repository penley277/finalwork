from DButil.DBO import DBO
from models.ManagerFactory import ManagerFactory


class ManagerList(object):

    def __init__(self, managerList):
        """
        初始化管理员列表，链接数据库
        :param managerList:
        """
        self.db = DBO(managerList)

    def addManager(self, other):
        """
        添加一个管理员
        :param other: 需要添加的管理员
        :return:
        """
        self.db.insert_values('manager', [other.getManagerId(), other.getName(),
                                          other.getPhone(), other.getPasswd(), other.getType()])

    def getManagerById(self, id):
        """
        根据ID获取管理员
        :param id: 想要获取的管理员ID
        :return: 返回获取的列表
        """
        return self.db.select_items('manager', '*', '%s%s%s' % ('where managerID=\'', id, '\''))

    def getManagerByName(self, name):
        """
        通过管理员姓名获取管理员
        :param name: 管理员姓名
        :return: 管理员列表
        """
        return self.db.select_items('manager', '*', '%s%s%s' % ('where name=\'', name, '\''))

    def removeManager(self, num):
        """
        从数据库中删除管理员
        :param num: 删除管理员的ID号
        :return:
        """
        self.db.delete_values('manager', '%s%s%s' % ('where managerID=\'', num, '\''))

    def changeType(self, num, manaType):
        """
        更改管理员的类型，根据id找到管理员，修改管理员类型
        :param num: 管理员id
        :param manaType: 想要改为的管理员类型
        :return:
        """
        if manaType == 'stu' or manaType == 'book':
                self.db.update_values('manager', dict([('managerType', manaType)]),
                                      '%s%s%s' % ('where managerID=\'', num, '\''))
        else:
            print("修改的类型有误或者超出权限")

    def changePasswd(self, num, passwd):
        """
        修改管理员密码
        :param num: 想要修改的管理员id
        :param passwd: 想要改为的密码
        :return:
        """
        self.db.update_values('manager', dict([('passwd', passwd)]),
                              '%s%s%s' % ('where managerID=\'', num, '\''))
