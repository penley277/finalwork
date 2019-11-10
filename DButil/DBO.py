import sqlite3


class DBO(object):
    def __init__(self, database_name):
        self.conn = None
        self.c = None
        self.connect_database(database_name)

    def connect_database(self, database_name):
        try:
            #   排除错误的数据库名
            if database_name[-3:] != '.db':
                database_name += '.db'
            self.conn = sqlite3.connect(database_name)
            self.c = self.conn.cursor()
        except sqlite3.Error as e:
            print("unable to open database file:", e)

    def close_database(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print("unable to close database file:", e)

    def create_table(self, table_name, args):
        try:
            table_items = ''
            if type(args) == list or type(args) == tuple:
                for item in args:
                    table_items += item + ','
                table_items = table_items[:-1]  # 去掉最后一个逗号
            elif type(args) == dict:
                for item in args.items():
                    table_items += item[0] + ' ' + item[1] + ','
                table_items = table_items[:-1]  # 去掉最后一个逗号

            self.c.execute('CREATE TABLE ' + table_name + ' (' + table_items + ')')
        except sqlite3.Error as e:
            print("unable to create table:", table_name, e)

    def drop_table(self, table_name):
        try:
            self.c.execute('DROP TABLE ' + table_name)
        except sqlite3.Error as e:
            print("unable to drop table:", table_name, e)

    def insert_values(self, table_name, args):
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
        try:
            self.c.execute('DELETE FROM ' + table_name + ' ' + constrains)
        except sqlite3.Error as e:
            print("unable to delete values from:", table_name, e)

    def get_table_info(self, table_name):
        try:
            self.c.execute('PRAGMA table_info(' + table_name + ')')
            return self.c.fetchall()
        except sqlite3.Error as e:
            print("unable to get table info:", table_name, e)
