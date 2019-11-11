import abc


class AbstractFactory(object):
    """
    抽象工厂类可以建立不同的管理员类型
    """
    @abc.abstractmethod
    def getManager(self, object):
        pass