class StudentList(object):
    """
    在学生的链表中，包含了学生信息的查询，以及对学生的信息的一些处理，
    获取学生借阅图书的情况，借阅图书的批量处理等
    """
    def __init__(self, stulist=None):
        if stulist is None:
            stulist = []
        self.stulist = stulist


    def addStu(self, stu):
        """
        添加学生
        :param stu: 添加学生的信息
        :return: 无
        """
        self.stulist.append(stu)

    def removeStu(self, stu):
        """
        移除数组中的某个学生
        :param stu: 想要移除的学生
        :return: 无
        """
        self.stulist.remove(stu)

    def getStuByNo(self, no):
        """
        使用学生的学号获取学生的信息
        :param no: 想要得到学生的学号
        :return: 某个学生
        """
        i = 0
        while i < len(self.stulist):
            if self.stulist[i].getStudNo() == no:
                return self.stulist[i]
            i = i + 1

    def getStuByName(self, name):
        """
        通过学生的名字，获取学生
        :param name: 想要找到的学生的名字
        :return: 某个学生
        """
        i = 0
        while i < len(self.stulist):
            if self.stulist[i].getStudName() == name:
                return self.stulist[i]
            i = i + 1

    def getStuByPhNum(self, phone):
        """
        通过学生的手机号，获取该学生
        :param phone: 想要找到的学生的手机号
        :return: 某个学生
        """
        i = 0
        while i < len(self.stulist):
            if self.stulist[i].getPhoneNum() == phone:
                return self.stulist[i]
            i = i + 1

    def outputStuList(self):
        """
        输出所有的学生信息
        :return: 无
        """
        i = 0
        while i < len(self.stulist):
            self.stulist[i].print()
            i = i + 1