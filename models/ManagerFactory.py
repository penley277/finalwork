from models.AbstractFactory import AbstractFactory
from models.BookManager import BookManager
from models.StuManager import  StuManager
import random

class ManagerFactory(AbstractFactory):

    def getManager(self, type):

        if type == None:
            return None
        elif type == '学生管理员': # 建立一个学生管理员类
            stu = StuManager()
            stu.setManagerId(generate_id())
            return stu
        elif type == '图书管理员': # 建立一个书籍管理员类型
            book = BookManager()
            book.setManagerId(generate_id())
            return book


def generate_id():
    a = range(1000, 9999)
    return '2MN' + str(random.sample(a, 1).pop(0))

if __name__ == '__main__':
    print(generate_id())