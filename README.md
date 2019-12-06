# 图书管理系统

图书管理系统的介绍！！

## 功能描述

将系统的整体功能按照人员分为4个部分，分别是学生功能、系统管理员、学生管理员和图书管理员等模块。将会按照这四个部分进行介绍。

### 学生功能描述

| 功能编号 | 功能         |
| -------- | ------------ |
| 1        | 用户登录     |
| 2        | 借阅图书     |
| 3        | 归还图书     |
| 4        | 续借图书     |
| 5        | 预约图书     |
| 6        | 查看借阅信息 |
| 7        | 图书评论     |
| 8        | 查看借阅排行 |
| 9        | 修改用户密码 |
| 10       | 浏览图书     |
| 11       | 查找图书     |

### 系统管理员

|功能编号| 功能|
|-----------|------|
|1|用户登录|
|2|添加管理员|
|3|修改管理员属性|
|4|删除管理员|
|5|修改用户密码|

### 学生管理员

| 功能编号 | 功能             |
| -------- | ---------------- |
| 1        | 用户登录         |
| 2        | 添加学生信息     |
| 3        | 维护指定学生信息 |
| 4        | 批量删除学生     |
| 5        | 批量导入学生信息 |
| 6        | 修改用户密码     |

### 图书管理员

| 功能编号 | 功能             |
| -------- | ---------------- |
| 1        | 用户登录         |
| 2        | 维护指定书籍信息 |
| 3        | 批量导入书籍信息 |
| 4        | 修改用户密码     |



## 类的设计

### 实体类

<img src="D:\2019\OOP\My\pic\ER.jpg" alt="ER" style="zoom:80%;" />

####  学生类

| 字段名          | Type | PK   |
| --------------- | ---- | ---- |
| 学号 studNo     | str  | *    |
| 姓名 studName   | str  |      |
| 专业 major      | str  |      |
| 班级 classNum   | str  |      |
| 手机号 phoneNum | str  |      |
| 密码 passwd     | str  |      |

#### 书籍类

| 字段名             | Type | PK   |
| ------------------ | ---- | ---- |
| 书号 bookNum       | str  | *    |
| 书名 bookName      | str  |      |
| 作者 author        | str  |      |
| 出版社 publisher   | str  |      |
| 总数 bookCnt       | int  |      |
| 借阅数量 borrowCnt | int  |      |
| 发布时间 pubTime   | date |      |
| 书籍评论 comment   | str  |      |

#### 借阅信息类

| 字段名                  | 类型 | PK   |
| ----------------------- | ---- | ---- |
| 借阅信息号 infoId       | str  | *    |
| 学生学号 studNo         | str  |      |
| 书籍书号 bookNo         | str  |      |
| 借阅时间 borrowTime     | date |      |
| 预计归还时间 finishTime | date |      |

#### 预订信息类
| 字段名              | 类型 | PK   |
| ------------------- | ---- | ---- |
| 预订信息号 infoId   | str  | *    |
| 学生学号 studNo     | str  |      |
| 书籍书号 bookNo     | str  |      |
| 预订时间 borrowTime | date |      |

#### 管理员类

| 字段                   | 类型 | PK   |
| ---------------------- | ---- | ---- |
| 管理员号 managerId     | str  | *    |
| 姓名 name              | str  |      |
| 手机号 phone           | str  |      |
| 密码 passwd            | str  |      |
| 管理员类型 managerType | str  |      |

### 数据库操作的接口类

BookList: 对数据库中的书籍表的操作类
StudentList：对数据库中的学生表的各种操作的实现类
InformList：信息类的接口
SubInformList：继承自信息类，对数据库中预约信息表的操纵的接口
BorrowInformList：继承自信息类，对数据库中借阅信息表的操纵的接口
ManagerList：对数据库中管理员信息表进行操作的接口

### 功能实现类

StudentService：包含了学生可以使用所有的功能接口

StuManagerService：包含了学生管理员可以使用的功能接口

BookManagerService：包含了图书管理员可以使用的功能接口

AdminManagerService：包含了系统管理员可以使用的功能接口

## 用例图及用例描述

![图书管理](D:\2019\OOP\My\pic\图书管理.jpg)

| 用例编号 | 用例名   | 对应用户                                 | 备注                 |
| -------- | -------- | ---------------------------------------- | -------------------- |
| US 01    | 登录系统 | 学生、系统管理员、学生管理员、图书管理员 | 进入图书管理系统     |
| US 02    | 借阅图书 | 学生                                     |                      |
| US 03    | 归还图书 | 学生                                     | 学生登录图书管理系统 |
| US 04    | 续借图书 | 学生                                     | 学生登录图书管理系统 |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |
|          |          |                                          |                      |

用例描述据举例：

1. 用例编号：US 02

   用例名称：借阅图书

   参与者：学生

   入口条件：以学生身份登录图书管理系统

   事件流：
      - 通常情况：
        - 1. 输入借阅图书的书号等信息
        - 2. 在图书系统中查找相应的图书
        - 3. 查看图书的借阅情况
        - 4. 借阅成功
      - 例外情况：
        - 2.1 图书不存在，重新输入图书信息
        - 2.2 图书已经借完，推荐进入预约图书

   出口条件：图书借阅成功或者失败

2. 用例编号： 添加学生信息

   用例名称：添加学生信息

   参与者：学生管理员

   入口条件：以学生管理员身份登录管理系统

   事件流：

   - 通常情况：
     - 1. 输入学生信息
     - 2. 添加学生
   - 异常情况：
     - 1.1 学生信息缺失，提示补全信息
     - 2.1 学生存在，添加失败
   
   出口条件：学生信息添加成功或者失败



## 系统类图

![](D:\2019\OOP\My\pic\类图.jpg)

## 时序图



## 系统功能描述

![功能结构](D:\2019\OOP\My\pic\功能结构.png)

1. 图书借阅功能：

   结语成功的条件：1. 学生存在 2. 书籍存在，而且书籍存在可借 3. 在借阅过程中会查看是否曾经借阅过这本书。其功能实现如图所示：

   

## 系统实现描述

1. 图书借阅功能：

   具体代码实现如下所示：

   ```Python
   def borrowBook(self, stuno, bookno):
       """
       图书借阅功能
       :param stuno: 借阅学生的学号
       :param bookno: 借阅的书号
       :return:@see$Error.NoneBook : 没有这本书的借阅信息
               @see$Error.BookCnt0: 书籍已经借空，不能借阅
               @see$Error.FinishBorrow : 借阅成功
       """
       book = self.booklist.getBookByNo(bookno)
       if book is Error.NoneBook: 
           return Error.NoneBook
   
       if self.borrowlist.getInformByStudNoBookNo(stuno, bookno) is Error.NoBorrowInform:
           if book.getBookCnt() == book.getBorrowCnt():
               return Error.BookCnt0
   
           self.borrowlist.addInformByNos(stuno, bookno)
           self.booklist.updateBorrowAndCnt(bookno, book.getBorrowCnt()+1)
           return Success.FinishBorrow
   
       return Error.ExitBorrowInform
   ```

2. 归还书籍

   ```python
   def returnBookWithComment(self, stuno, bookno, comment=None):
           """
           归还书籍
           :param stuno: 归还学生的学号
           :param bookno: 归还学生的书号
           :param comment: 归还时给予的评价
           :return: @see$Error.NoneBook : 没有这本书的借阅信息
                    @see$Error.BookCnt0: 书籍已经借空，不能借阅
                    @see$Error.FinishReturn: 归还书籍成功
           """
           book = self.booklist.getBookByNo(bookno)
   
           # 查看书籍是否存在
           if book is Error.NoneBook:
               return Error.NoneBook
           book = self.booklist.getBookByNo(bookno)
   
           # 删除借阅记录
           self.borrowlist.deleteInform(stuno, bookno)
   
           # 评价内容
           if comment is not None: # 如果没有给评价
               self.booklist.setComment(book.getBookNo(), comment)
           return Success.FinishReturn
   ```

3. 续借书籍

   ```python
   def renewBook(self, stuno, bookno):
           """
           续借单本书籍
           :param stuno: 学号
           :param bookno: 书号
           :return: @see$Error.NoneBook : 没有这本书
                    @see$Error.FinishRenew： 续借成功
                    @see$Error.NoBorrowInform: 没有这条借阅信息
           """
           book = self.booklist.getBookByNo(bookno)
           if book == Error.NoneBook:
               return Error.NoneBook
   
           list = self.borrowlist.getInformByStudNoBookNo(stuno, bookno)
   
           # 如果借阅信息存在
           if list != Error.NoBorrowInform:
               borrow = list.pop(0)
               self.borrowlist.addInformLast(borrow)
               return Success.FinishRenew
   
           return Error.NoBorrowInform
   ```



## 总结与反思

### 设计特点

1. 关于数据库调用接口的设计

   数据库查询操作使用的是字段形式，将语句进行了拆分，增加了代码的复用。

2. 加入了抽象工厂

   使用抽象工厂，负责产生特定的管理员，进行管理员id的生成

3. 将实体类、数据库操作类和功能实现类，分成了三个不同的层次



### 反思

- 宋鹏磊的反思

  在完成作业的过程中，最开始是结构设计的问题。设计的过程经历了一段时间，比写代码花费了更多的时间。

  到了，完成作业之中，最主要的问题变成了合作问题。合作的问题从项目合并开始，就一直困扰着我。最开始是给出的接口。
