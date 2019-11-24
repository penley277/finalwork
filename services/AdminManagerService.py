from list.ManagerList import ManagerList
from models import ManagerFactory
from util import Error, Success


class AdminMangerService(object):
    def __init__(self, database_name):
        """
        管理员信息的维护
        :param database_name: 数据库列表
        """
        self.managerlist = ManagerList(database_name)

    def addManger(self, name, phone, passwd, type):
        manager = ManagerFactory.ManagerFactory().getManager(type)
        manager.setName(name)
        manager.setPhone(phone)
        manager.setPasswd(passwd)
        self.managerlist.addManager(manager)
        return Success.FinishAddManager

    def deleteManager(self, id):
        if self.managerlist.getManagerById(id) == Error.NoManager:
            return Error.NoManager

        self.managerlist.removeManager(id)
        return Success.FinishDeleteManager

    def getMangerByName(self, name):
        return self.managerlist.getManagerByParam('name', name)

    def getManagerByPhone(self, phone):

        return self.managerlist.getManagerByParam('phone', phone)

    def getManagerByType(self, type):
        return self.managerlist.getManagerByParam('managerType', type)

    def modifyNameById(self, id, name):
        if self.managerlist.getManagerById(id) == Error.NoManager:
            return Error.NoManager
        self.managerlist.modifyParamById('name', id, name)
        return Success.FinishModify

    def modifyPhoneById(self, id, phone):
        if self.managerlist.getManagerById(id) == Error.NoManager:
            return Error.NoManager
        self.managerlist.modifyParamById('phone', id, phone)
        return Success.FinishModify

    def modifyPasswdById(self, id, passwd):
        if self.managerlist.getManagerById(id) == Error.NoManager:
            return Error.NoManager
        self.managerlist.modifyParamById('passwd', id, passwd)
        return Success.FinishModify

    def modifyTypeById(self, id, manaType):
        """
        修改管理员类型
        :param id: 管理员号
        :param manaType: 管理员类型
        :return:
        """
        if self.managerlist.getManagerById(id) == Error.NoManager:
            return Error.NoManager
        self.managerlist.changeType(id, manaType)
        return Success.FinishModify

    def displayAllManager(self):
        """
        显示所有的管理员信息
        :return: 所有管理员信息的类的列表
        """
        return self.managerlist.getAllManager()


if __name__ == '__main__':
    ma = AdminMangerService('../system.db')
    print(ma.displayAllManager().pop(0))
