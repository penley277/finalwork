from DButil.DBO import DBO
from models.Student import Student
from util import Error


class StudentList(object):
    """
    在学生的链表中，包含了学生信息的查询，以及对学生的信息的一些处理，
    获取学生借阅图书的情况，借阅图书的批量处理等
    """

    def __init__(self, database_name):
        self.db = DBO(database_name)

    def addStu(self, stu):
        """
        添加学生
        :param stu: 添加学生的信息
        :return: 无
        """
        self.db.insert_values('student', [stu.getStudNo(), stu.getStudName(),
                                          stu.getMajor(), stu.getClassNum(),
                                          stu.getPhoneNum(), stu.getPassWd()])

    def removeStu(self, num):
        """
        从数据库中删除学生
        :param num: 删除学生的学号
        :return:
        """
        self.db.delete_values('student', '%s%s%s' % ('where studNum=\'', num, '\''))

    def getStuByNo(self, no):
        """
        使用学生的学号获取学生的信息
        :param no: 想要得到学生的学号
        :return: 某个学生
        """
        select = self.db.select_items('student', '*', '%s%s%s' % ('where studNo=\'', no, '\''))
        if len(select) == 0:
            return Error.NoneStu
        return Student(select[0][0], select[0][1], select[0][2], select[0][3], select[0][4], select[0][5])

    def modify(self, param, no, name):
        """
        修改学生的某个属性的值，不包括学生号
        :param param: 修改的属性名
        :param no: 学号
        :param name: 姓名
        :return:
        """
        self.db.update_values('student', {'%s%s%s' % ('\'', param, '\''): name},
                              '%s%s%s' % ('where studNo=\'', no, '\''))

    def getStuByParam(self, param, other):
        """
        通过学生的名字，获取学生
        :param name: 想要找到的学生的名字
        :return: 某个学生列表
        """
        select = self.db.select_items('student', '*', '%s%s%s%s%s' % ('where ', param, ' like \'%', other, '%\''))
        if len(select) == 0:
            return Error.NoneStu
        i = 0
        bi = []
        while i < len(select):
            bi.append(Student(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4], select[i][5]))
            i = i + 1
        return bi

    def outputStuList(self):
        """
        输出所有的学生信息
        :return: 所有学生的信息
        """
        select = self.db.select_items('student', '*')
        if select is None:
            return False
        i = 0
        bi = []
        while i < len(select):
            bi.append(Student(select[i][0], select[i][1], select[i][2], select[i][3], select[i][4], select[i][5]))
            i = i + 1
        return bi

    def addStuByFile(self, filename):
        """
        从文件批量添加书籍到数据库中
        :param filename:文件名字
        :return:无
        """
        with open(filename, 'r', encoding='gbk') as file_to_read:
            while True:
                lines = file_to_read.readline()
                if not lines:  # 读取到最后一行，停止读取操作
                    break

                no, name, major, classNum, phoneNum = [i for i in lines.split()]  # 根据空格，将值读出
                student = Student(no, name, major,  # 将读取的值设置为一个对象
                                  classNum, phoneNum, no)
                self.addStu(student)
        file_to_read.close()

    def closeDB(self):
        self.db.close_database()
