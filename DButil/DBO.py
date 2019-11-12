import sqlite3


class DBO(object):
    """
    进行数据库操作的接口，进行增删改查等操作
    从网上找的，写的比我好
    """
    def __init__(self, database_name):
        """
        与数据库建立链接
        :param database_name: 需要进行了链接的数据库名称
        """
        self.conn = None
        self.c = None
        self.connect_database(database_name)

    def connect_database(self, database_name):
        """
        连接数据库，并且进行数据名称的审核
        :param database_name:
        :return:
        """
        try:
            if database_name[-3:] != '.db': # 判断后三个字符是不是数据库的后缀
                database_name += '.db'
            self.conn = sqlite3.connect(database_name)
            self.c = self.conn.cursor()
        except sqlite3.Error as e: # 捕获错误数据名
            print("unable to open database file: ", e)

    def close_database(self):
        """
        关闭数据库，断开连接
        :return:
        """
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print("unable to close database file:", e)

    def create_table(self, table_name, args):
        """
        创建建一个数据库表
        :param table_name: 数据库表的名称
        :param args: 参数名
        :return:
        """
        try:
            table_items = ''
            if type(args) == list or type(args) == tuple:
                for item in args:
                    table_items += item + ','
                table_items = table_items[:-1]
            elif type(args) == dict:
                for item in args.items():
                    table_items += item[0] + ' ' + item[1] + ','
                table_items = table_items[:-1]  # 去掉最后一个逗号

            self.c.execute('CREATE TABLE ' + table_name + ' (' + table_items + ')')
            self.conn.commit()
        except sqlite3.Error as e:
            print("unable to create table:", table_name, e)

    def drop_table(self, table_name):
        try:
            self.c.execute('DROP TABLE ' + table_name)
            self.conn.commit()
        except sqlite3.Error as e:
            print("unable to drop table:", table_name, e)

    def insert_values(self, table_name, args):
        """
        数据库中的插入记录操作
        :param table_name: 插入目标的表名
        :param args: 插入记录的属性
        :return:
        """
        try:
            table_items = ''
            table_values = ''
            if type(args) == list or type(args) == tuple:
                for item in args:
                    if type(item) == str:
                        value = '"' + item + '"'
                    else:
                        value = item
                    table_values += str(value) + ','
                table_values = table_values[:-1]  # 去掉最后一个逗号
                self.c.execute('INSERT INTO ' + table_name + ' VALUES (' + table_values + ')')
            elif type(args) == dict:
                for item in args.items():
                    table_items += item[0] + ','
                    if type(item[1]) == str:
                        value = '"' + item[1] + '"'
                    else:
                        value = item[1]
                    table_values += str(value) + ','
                table_items = table_items[:-1]
                table_values = table_values[:-1]  # 去掉最后一个逗号
                self.c.execute('INSERT INTO ' + table_name + ' (' + table_items + ') VALUES (' + table_values + ')')
            self.conn.commit()
        except sqlite3.Error as e:
            print("unable to insert table:", table_name, e)

    def select_items(self, table_name, args, constrains=''):
        try:
            table_items = ''
            for item in args:
                table_items += item + ','
            table_items = table_items[:-1]  # 去掉最后一个逗号
            self.c.execute('SELECT ' + table_items + ' FROM ' + table_name + ' ' + constrains)
            return self.c.fetchall()
        except sqlite3.Error as e:
            print("unable to select items from:", table_name, e)

    def update_values(self, table_name, args, constrains=''):
        try:
            table_items = ''
            for item in args.items():
                if type(item[1]) == str:
                    value = '"' + item[1] + '"'
                else:
                    value = item[1]
                table_items += item[0] + '=' + str(value) + ','
            table_items = table_items[:-1]  # 去掉最后一个逗号
            self.c.execute('UPDATE ' + table_name + ' SET ' + table_items + ' ' + constrains)
            self.conn.commit()

        except sqlite3.Error as e:
            print("unable to update values in", table_name, e)

    def delete_values(self, table_name, constrains=''):
        """
        删除一条记录
        :param table_name: 删除记录的表名
        :param constrains: 进行记录选择条件
        :return:
        """
        try:
            self.c.execute('DELETE FROM ' + table_name + ' ' + constrains)
            self.conn.commit()
        except sqlite3.Error as e:
            print("unable to delete values from:", table_name, e)

    def get_table_info(self, table_name):
        try:
            self.c.execute('PRAGMA table_info(' + table_name + ')')
            return self.c.fetchall()
        except sqlite3.Error as e:
            print("unable to get table info:", table_name, e)
