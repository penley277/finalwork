import sqlite3


class DBO(object):
    """
    使用通用的数据库接口，完成在数据库中的增删改查等操作
    """

    def __init__(self, name):
        """
        初始化函数，创建数据库连接
        """
        self.conn = sqlite3.connect(name)
        self.c = self.conn.cursor()

    def executeUpdate(self, sql, ob):
        """
        数据库的插入、修改函数，通过sql语句进行插入操作以及修改，
        只需要完成操作后，更新数据即可
        :param sql: 传入的SQL语句
        :param ob: 传入的数据，可以是多个
        :return: 返回操作数据库状态
        """
        try:
            self.c.executemany(sql, ob)
            add = self.conn.total_changes
        except Exception as e:
            print('Error： ', e)
            return False
        finally:
            self.conn.commit()
        if add > 0:
            return True
        else:
            return False


    def executeDelete(self, sql, ob):
        """
        操作数据库数据删除的函数
        :param sql: 传入的SQL语句
        :param ob: 传入数据
        :return: 返回操作数据库状态
        """
        try:
            self.c.execute(sql, ob)
            delete = self.conn.total_changes
        except Exception as e:
            print('Error： ', e)
            return False
        finally:
            self.conn.commit() # 进行提交，完成数据库变化
        if delete > 0:
            return True
        else:
            return False

    def executeQuery(self, sql, ob):
        """
        数据库数据查询
        :param sql: 传入的SQL语句
        :param ob: 传入数据
        :return: 返回操作数据库状态
        """
        query = self.c.execute(sql, ob)
        return query

    def close(self):
        """
        关闭数据库相关连接的函数
        :return:
        """
        self.c.close()
        self.conn.close()
