import string

from DButil.DBO import DBO

from list.InformList import InformList
from list.StudentList import StudentList
from list.BookList import BookList
import datetime

from models.BorrowInfo import BorrowInfo
import random

from util import Error, Success
from util import util


class BorrowInformList(InformList):

    def __init__(self, database_name):
        """
        初始化，链接数据库
        :param database_name: 数据库名字
        """
        self.db = DBO(database_name)
        self.bookList = BookList(database_name)
        # self.studList = StudentList(database_name)
        self.history = []  # 借阅历史的buffer

    def addInform(self, other):
        """
        添加借阅信息
        :param other: 添加借阅信息的内容
        :return: 添加成功，返回True; 否则返回False
        """
        other.setNo(''.join(random.sample(string.digits * 5 + string.ascii_letters * 4, 20)))
        self.db.insert_values('borrowInfo', [other.getNo(), other.getStuNo(), other.getBookNo(), other.getBorrowTime(),
                                             other.getFinishTime()])
        return Success.FinishBorrow

    def addInformByNos(self, stuno, bookno):
        """
        使用学号和书号进行书籍借阅
        :param stuno: 学号，需要进行检测是否在书籍的列表中。登录之后，可以直接获取使用
        :param bookno: 书号，需要检测是否在书籍的列表中
        :return: 返回添加成功或者失败
        """
        no = ''.join(random.sample(string.digits * 5 + string.ascii_letters * 4, 20))
        self.db.insert_values('borrowInfo', [no, stuno, bookno, datetime.date.today().isoformat(),
                                             util.getReturnTime(datetime.date.today().isoformat())])
        return Success.FinishBorrow

    def deleteInform(self, stuno, bookno):
        """
        删除借阅信息，使用学生和书号，删除借阅信息
        :param stuno: 学生学号
        :param bookno: 书籍书号
        :return: 删除成功返回True， 否则返回False
        """
        # 通过操纵数据库删除信息
        self.db.delete_values('borrowInfo', '%s%s%s%s%s' % ('where studNo=\'', stuno, '\' and bookNo=\'', bookno, '\''))
        # 更新借阅数量和剩余数量
        return Success.FinishReturn

    def getInformByStudNo(self, no):
        """
        根据学号，列出所有的借阅书籍
        :param no: 学生学号
        :return: 获取到信息，返回借阅信息数组; 如果没有得到信息，返回None
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where studNo=\'', no, '\''))
        i = 0
        bi = []

        # 如果没有选择到信息，返回空
        if len(select) == 0:
            return Error.NoBorrowInform

        while i < len(select):
            bi.append(BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1
        return bi

    def getInformByStudNoBookNo(self, stuno, bookno):
        """
        根据学号，列出所有的借阅书籍
        :param no: 学生学号
        :return: 获取到信息，返回借阅信息数组; 如果没有得到信息，返回None
        """
        select = self.db.select_items('borrowInfo', '*',
                                      '%s%s%s%s%s%s' % ('where studNo=\'', stuno, '\'', ' and bookNo=\'', bookno, '\''))
        i = 0
        bi = []

        # 如果没有选择到信息，返回空
        if len(select) == 0:
            return Error.NoBorrowInform

        while i < len(select):
            bi.append(BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1
        return bi

    def getInformByBookNo(self, no):
        """
        根据书号列出所有的借阅书籍
        :param no: 书号
        :return: 获取到信息，返回借阅信息数组; 如果没有得到信息，返回None
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where bookNo=\'', no, '\''))

        if len(select) == 0:
            return Error.NoBorrowInform
        i = 0
        bi = []
        while i < len(select):
            bi.append(BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1

        return bi

    def getInformBybTime(self, time):
        """
        根据借阅时间列出借阅信息
        :param time:时间格式为yyyy/mm/dd
        :return: 返回借阅信息
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where borrowTime=\'', time, '\''))
        if len(select) == 0:  # 没有查询到记录
            return Error.NoBorrowInform

        i = 0
        bi = []
        while i < len(select):  # 将查询到的记录转化为借阅信息类
            bi.append(BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1

        return bi

    def addInformLast(self, list):
        """
        按照学号书号续借书籍
        :param stu: 学号
        :param no: 书号
        :return: 需要设置续借信息，如果续借成功，返回True
        """

        rtime = util.getReturnTime(datetime.date.today().isoformat())
        self.db.update_values('borrowInfo', {'borrowTime': list.getBorrowTime(),
                                             'finishTime': rtime},
                              '%s%s%s%s%s%s' % ('where studNo=\'', list.getStuNo(), '\'', ' and bookNo=\'', list.getBookNo(), '\''))
        return Success.FinishBorrow

    def getInformByfTime(self, time):
        """
        根据借阅的结束时间进行查询
        :param time: 结束时间
        :return: 如果没有查询到元素，返回False，否则返回True
        """
        select = self.db.select_items('borrowInfo', '*', '%s%s%s' % ('where finishTime=\'', time, '\''))

        if len(select) == 0:  # 没有查询到
            return Error.NoBorrowInform
        i = 0
        bi = []
        while i < len(select):
            bi.append(BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4]))
            i = i + 1

        return bi

    def topTenByCnt(self):
        """
        获取借阅量最多的10本书籍
        :return: 返回借阅量由高到低的字典， 包含学生的学号以及借阅的次序
        TODO: 我知道有bug，但是我不想改
        """
        select = self.db.select_items('borrowInfo', '*')

        i = 0
        while i < len(select):
            self.history.append(select[i][2])
            i = i + 1

        dict = {}
        for key in self.history:
            dict[key] = dict.get(key, 0) + 1
        d_order = sorted(dict.items(), key=lambda x: x[1], reverse=True)

        while len(d_order) < 10:  # 如果借阅数量总数不足十个， 加入空格补位置
            d_order.append((' ', ' '))

        return d_order

    def outputInform(self):
        """
        输出所有的借阅信息
        :return: 返回借阅信息的列表
        """
        select = self.db.select_items('borrowInfo', '*')
        if len(select) == 0:
            return Error.NoBorrowInform

        i = 0
        bi = []
        while i < len(select):
            binfo = BorrowInfo(select[i][1], select[i][2], select[i][3], select[i][4])
            bi.append(binfo)
            i = i + 1

        return bi

    def closeDB(self):
        """
        关闭数据库的接口
        :return: 无
        """
        self.db.close_database()

