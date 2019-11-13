import abc


class InformList(object):

    @abc.abstractmethod
    def addInform(self, object):
        pass

    @abc.abstractmethod
    def deleteInform(self, object):
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