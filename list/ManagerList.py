from DButil.DBO import DBO
from models.Manager import Manager


class ManagerList(object):

    def __init__(self, database_name):
        """
        初始化管理员列表，链接数据库
        :param managerList:
        """
        self.db = DBO(database_name)

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
        select = self.db.select_items('manager', '*', '%s%s%s' % ('where managerID=\'', id, '\''))
        if len(select) == 0:
            return None
        return Manager(select[0][0], select[0][1], select[0][2], select[0][3], select[0][4])

    def getManagerByName(self, name):
        """
        通过管理员姓名获取管理员
        :param name: 管理员姓名
        :return: 管理员列表
        """
        select = self.db.select_items('manager', '*', '%s%s%s' % ('where name like \'%', name, '%\''))
        if len(select) == 0:
            return False
        i = 0
        bi = []
        while i < len(select):
            bi.append(Manager(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1
        return bi

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
            return True
        else:
            return False

    def setPW(self, Id, newPW):
        self.db.update_values('manager', {'passwd': newPW}, '%s%s%s' % ('where managerID=\'', Id, '\''))

    def closeDB(self):
        self.db.close_database()


if __name__ == '__main__':
    l = ManagerList('system.db')
    print(l.getManagerById('101'))