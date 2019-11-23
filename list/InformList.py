import abc


class InformList(object):

    @abc.abstractmethod
    def addInform(self, object):
        """
        添加信息
        :param object: 借阅信息或者预约信息
        :return:
        """
        pass

    @abc.abstractmethod
    def deleteInform(self, object1, object2):
        pass

    @abc.abstractmethod
    def getInformByStudNo(self, no):
        pass

    @abc.abstractmethod
    def getInformByBookNo(self, no):
        pass


    @abc.abstractmethod
    def getInformByTime(self, time):
        pass

    @abc.abstractmethod
    def outputInform(self):
        pass