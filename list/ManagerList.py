from DButil.DBO import DBO
from models.Manager import Manager
from util import Error, Success


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
        return Success.FinishAddManager

    def getManagerById(self, id):
        """
        根据ID获取管理员
        :param id: 想要获取的管理员ID
        :return: 返回获取的列表
        """
        select = self.db.select_items('manager', '*', '%s%s%s' % ('where managerID=\'', id, '\''))
        if len(select) == 0:
            return Error.NoManager

        i = 0
        bi = []
        while i < len(select):
            bi.append(Manager(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1
        return bi

    def getManagerByParam(self, param, name):
        """
        通过管理员姓名获取管理员
        :param name: 管理员姓名
        :return: 管理员列表
        """
        select = self.db.select_items('manager', '*', '%s%s%s%s%s' % ('where ', param, ' like \'%', name, '%\''))
        if len(select) == 0:
            return Error.NoManager

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
        if self.getManagerById(num) == Error.NoManager:
            return Error.NoManager

        self.db.delete_values('manager', '%s%s%s' % ('where managerID=\'', num, '\''))
        return

    def changeType(self, num, manaType):
        """
        更改管理员的类型，根据id找到管理员，修改管理员类型
        :param num: 管理员id
        :param manaType: 想要改为的管理员类型
        :return:
        """
        if manaType == '学生管理员' or manaType == '书籍管理员':
            self.db.update_values('manager', dict([('managerType', manaType)]),
                                  '%s%s%s' % ('where managerID=\'', num, '\''))
            return Success.FinishChangeType
        else:
            return Error.ChangeTypeInvild

    def modifyParamById(self, param, Id, newItem):
        self.db.update_values('manager', {param: newItem}, '%s%s%s' % ('where managerID=\'', Id, '\''))

    def getAllManager(self):
        """
        输出所有的学生信息
        :return: 所有学生的信息
        """
        select = self.db.select_items('manager', '*')
        if select is None:
            return False
        i = 0
        bi = []
        while i < len(select):
            bi.append(Manager(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1
        return bi

    def closeDB(self):
        self.db.close_database()


if __name__ == '__main__':
    l = ManagerList('system.db')
    print(l.getManagerById('101'))