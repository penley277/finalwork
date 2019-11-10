import abc


class InformList(object):

    def __init(self):
        pass

    @abc.abstractmethod
    def addInform(self, object):
        pass

    @abc.abstractmethod
    def deleteInform(self, object):
        pass

    @abc.abstractmethod
    def getInformByStudNo(self):
        pass

    @abc.abstractmethod
    def getInformByBookNo(self):
        pass


    @abc.abstractmethod
    def getInformByTime(self):
        pass

    @abc.abstractmethod
    def outputInform(self):
        pass