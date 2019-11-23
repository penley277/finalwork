from models.AbstractFactory import AbstractFactory
from models.AdminManager import AdminManager
from models.BookManager import BookManager
from models.StuManager import  StuManager


class ManagerFactory(AbstractFactory):

    def getManager(self, type):
        if type == None:
            return None
        elif type == '学生管理员': # 建立一个学生管理员类
            return StuManager()
        elif type == '图书管理员': # 建立一个书籍管理员类型
            return BookManager()
        elif type == '系统管理员': # ？？？？？
            return AdminManager()
