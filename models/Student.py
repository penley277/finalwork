

class Student(object):
    """
    学生类中包含了学生的基本信息以及联系方式
    主要包含的接口是学生基本信息的获取以及修改主要方式
    学生类是一个实体类
    """

    def __init__(self, studNo, studName, major, classNum, phoneNum, passwd=None):
        """
        学生类的初始化函数
        :param studNo: 学号
        :param studName: 名字
        :param major: 学生所在的专业
        :param classNum: 学生所在班级的学号
        :param phoneNum: 手机号
        :param passwd: 学生密码
        :param bookList: 学生借阅的图书列表
        """
        self.studNo = studNo
        self.studName = studName
        self.major = major
        self.classNum = classNum
        self.phoneNum = phoneNum
        self.passwd = passwd

    def getStudNo(self):
        """
        获取学生的学号
        :return: 返回学生的学号
        """
        return self.studNo

    def setStudNo(self, studNo):
        """
        设置学生的学号
        :param studNo: 要改为的学生学号
        :return: 无返回值
        """
        self.studNo = studNo

    def getStudName(self):
        """
        获取学生姓名
        :return: 当前学生的姓名
        """
        return self.studName

    def setStudName(self, studName):
        """
        设置学生的姓名
        :param studName: 需要更改的名字
        :return: 无
        """
        self.studName = studName

    def getMajor(self):
        """
        获取学生专业
        :return: 学生的专业
        """
        return self.major

    def setMajor(self, major):
        """
        设置学生专业
        :param major: 需要更改的学生专业
        :return: 无
        """
        self.major = major


    def getPhoneNum(self):
        return self.phoneNum

    def setPhoneNum(self, phoneNum):
        self.phoneNum = phoneNum


    def setPassWd(self, passwd):
        """
        进行更改密码的更改
        :param passwd: 想要改为的密码
        :return: 无
        """
        self.passwd = passwd

    def print(self):
        """
        输出学生的信息
        :return: 无
        """
        spaces = "      "
        print(self.studNo, spaces, self.studName, spaces,
              self.major, spaces, self.classNum, spaces,
              self.phoneNum)
