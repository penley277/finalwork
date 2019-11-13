from DButil.DBO import DBO


class StudentList(object):
    """
    在学生的链表中，包含了学生信息的查询，以及对学生的信息的一些处理，
    获取学生借阅图书的情况，借阅图书的批量处理等
    """
    def __init__(self, stulist=None):
        self.db = DBO(stulist)

    def addStu(self, stu):
        """
        添加学生
        :param stu: 添加学生的信息
        :return: 无
        """
        self.db.insert_values('student', [stu.getStuNo(), stu.getStuName(),
                                       stu.getMajor(), stu.getClassNum(),
                                       stu.getPhoneNum(), stu.getPasswd()])

    def getStuByNo(self, no):
        """
        使用学生的学号获取学生的信息
        :param no: 想要得到学生的学号
        :return: 某个学生
        """
        return self.db.select_items('student', '*', '%s%s%s' % ('where studNo=\'', no, '\''))

    def getStuByName(self, name):
        """
        通过学生的名字，获取学生
        :param name: 想要找到的学生的名字
        :return: 某个学生
        """
        return self.db.select_items('student', '*', '%s%s%s' % ('where studName=\'', name, '\''))

    def getStuByPhNum(self, phone):
        """
        通过学生的手机号，获取该学生
        :param phone: 想要找到的学生的手机号
        :return: 某个学生
        """
        return self.db.select_items('student', '*', '%s%s%s' % ('where phoneNum=\'', phone, '\''))

    def outputStuList(self):
        """
        输出所有的学生信息
        :return: 无
        """
        return self.db.select_items('student', '*', '*')

