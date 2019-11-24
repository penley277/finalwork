from list.StudentList import StudentList
from models.Student import Student
from util import Error, Success


class StuMangerService(object):

    def __init__(self, database_name):
        """
        学生信息的维护
        :param database_name: 数据库列表
        """
        self.studlist = StudentList(database_name)

    def addStu(self, no, name, major, classNum, phoneNum, passwd=None):
        """
        添加学生信息
        :param no: 学号
        :param name: 姓名
        :param major: 专业
        :param classNum: 班级
        :param phoneNum:  手机号
        :param passwd: 密码， 如果没有进行密码的设置，初始密码和学号相同
        :return: @see$Error.ExitStu: 学生的学号已经冲突，不能进行添加
                 @see$Success.FinishAddStu: 成功添加学生信息
        """
        if passwd == None:
            passwd = no

        stu = Student(no, name, major, classNum, phoneNum, passwd)

        if self.studlist.getStuByNo(no) == Error.NoneStu:
            self.studlist.addStu(stu)
            return Success.FinishAddStu

        return Error.ExitStu

    ###################################信息修改部分######################################
    def modifyName(self, no, name):
        """
        根据学号，修改学生信息
        :param no: 学号
        :param name:姓名
        :return:@see$Error.NoneStu : 没有这个学生
                @see$Error.FinishModify: 修改成功
        """
        if self.studlist.getStuByNo(no) != Error.NoneStu:
            self.studlist.modify('studName',no, name)
            return Success.FinishModify
        return Error.NoneStu

    def modifyMajor(self, no, major):
        """
        根据学号，修改学生专业
        :param no: 学号
        :param name:姓名
        :return:@see$Error.NoneStu : 没有这个学生
                @see$Error.FinishModify: 修改成功
        """

        if self.studlist.getStuByNo(no) != Error.NoneStu:
            self.studlist.modify('major', no, major)
            return Success.FinishModify
        return Error.NoneStu

    def modifyClassNum(self, no, classnum):
        """
        根据学号，修改学生信息
        :param no: 学号
        :param name:姓名
        :return:@see$Error.NoneStu : 没有这个学生
                @see$Error.FinishModify: 修改成功
        """
        if self.studlist.getStuByNo(no) != Error.NoneStu:
            self.studlist.modify('classNum', no, classnum)
            return Success.FinishModify
        return Error.NoneStu

    def modifyPhoneNum(self, no, phonenum):
        """
        根据学号，修改学生信息
        :param no: 学号
        :param name:姓名
        :return:@see$Error.NoneStu : 没有这个学生
                @see$Error.FinishModify: 修改成功
        """
        if self.studlist.getStuByNo(no) != Error.NoneStu:
            self.studlist.modify('phoneNum', no, phonenum)
            return Success.FinishModify
        return Error.NoneStu

    def modifyPasswd(self, no, passwd):
        """
        根据学生学号，修改学生的密码
        :param no: 学号
        :param name: 密码
        :return:@see$Error.NoneStu : 没有这个学生
                @see$Error.FinishModify: 修改成功
        """
        if self.studlist.getStuByNo(no) != Error.NoneStu:
            self.studlist.modify('passwd', no, passwd)
            return Success.FinishModify
        return Error.NoneStu

    ###################################信息修改部分###################################

    def deleteStuByPatch(self, list):
        """
        批量删除学生
        :param list: 学号的列表
        :return: @see$Success.FinishDeleteStu: 删除学生信息
        """
        i = 0
        while i < len(list):
            if self.studlist.getStuByNo(list[i]) != Error.NoneStu:
                self.studlist.removeStu(list[i])
            return Success.FinishDeleteStu
        return Error.NoneStu

    def addStuByPatch(self, filename):
        """
        批量增加学生信息
        :param filename: 文件名
        :return:@see$Error.FileNameFalse: 文件类型错误
                @see$SuccessAddStu: 成功添加学生
        """
        if filename[-3:] != '.txt':
            return Error.FileNameFalse
        self.studlist.addStuByFile(filename)
        return Success.FinishAddStu

    #############################学生信息获取部分##############################
    def displayAllStu(self):
        """
        显示所有的学生信息
        :return: 所有学生信息的类的列表
        """
        return self.studlist.outputStuList()

    def getStudentByNo(self, no):
        """
        通过学号获取某个学生的信息
        :param no: 使用学生学号，进行精确查询
        :return: 返回学生的信息列表
        """
        return self.studlist.getStuByNo(no)

    def getStudentByName(self, name):
        """
        通过姓名，获取学生信息
        :param name: 学生名字，模糊查询
        :return:@see$Student 学生信息的列表
                @see$Error: NoneStu
        """
        return self.studlist.getStuByParam('studName', name)

    def getStudentByMajor(self, major):
        """
        通过专业，获取学生信息
        :param major: 学生名字，模糊查询
        :return:@see$Student 学生信息的列表
                @see$Error: NoneStu
        """
        return self.studlist.getStuByParam('major', major)

    def getStudentByClassNum(self, classNum):
        """
        通过班级，获取学生信息
        :param classNum: 学生名字，模糊查询
        :return:@see$Student 学生信息的列表
                @see$Error: NoneStu
        """
        return self.studlist.getStuByParam('classNum', classNum)

    def getStudentByPhoneNum(self, phone):
        """
        通过手机号，获取学生信息
        :param phone: 手机号，模糊查询
        :return:@see$Student 学生信息的列表
                @see$Error: NoneStu
        """
        return self.studlist.getStuByParam('phoneNum', phone)
    #############################学生信息获取部分##############################

if __name__ == '__main__':
    stu = StuMangerService('../system.db')
    print(stu.displayAllStu())