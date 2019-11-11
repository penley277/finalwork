from DButil.DBO import DBO
from models.ManagerFactory import ManagerFactory


class ManagerList(object):

    def __init__(self, managerList):
        self.db = DBO(managerList)

    def addManager(self, other):
        self.db.insert_values('manager', [other.getManagerId(), other.getName(),
                                          other.getPhone(), other.getPasswd(), other.getType()])

    def getManagerById(self, id):
        return self.db.select_items('manager', '*', '%s%s%s' % ('where managerID=\'', id, '\''))

    def getManagerByName(self, name):
        return self.db.select_items('manager', '*', '%s%s%s' % ('where name=\'', name, '\''))

    def removeManager(self, num):
        """
        从数据库中删除管理员
        :param num: 删除管理员的ID号
        :return:
        """
        self.db.delete_values('manager', '%s%s%s' % ('where managerID=\'', num, '\''))

    def changeType(self, num, manaType):
        if manaType == 'stu' or manaType == 'book':
                self.db.update_values('manager', dict([('managerType', manaType)]),
                                      '%s%s%s' % ('where managerID=\'', num, '\''))
        else:
            print("修改的类型有误或者超出权限")

    def changePasswd(self, num, passwd):
        self.db.update_values('manager', dict([('passwd', passwd)]),
                              '%s%s%s' % ('where managerID=\'', num, '\''))


if __name__ == "__main__":
    managerlist = ManagerList('system.db')
    # manager = Manager('101', , , 'dfkjdjafkd', 'stu')
    managerlist.changeType('101', 'passwddfd')
