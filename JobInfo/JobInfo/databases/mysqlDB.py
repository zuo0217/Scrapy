#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create time : 2018/6/3下午5:40
# Create by Saseny.Zhou
# File name: mysqlDB.py

import mysql.connector


class MySQL_Connector():
    """
        数据库接口应用类
    """

    PORT = 3306
    en_decode = "utf8"

    def __init__(self, address, user, database, password=""):
        self.ip = address
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        config = {
            "host": self.ip,
            "user": self.user,
            "password": self.password,
            "port": self.PORT,
            "database": self.database,
            "charset": self.en_decode
        }
        try:
            self.cnn = mysql.connector.connect(**config)
            return True
        except mysql.connector.Error as a:
            print('connect fails!{}'.format(a))
            return False

    def create_table(self, NewTable):
        status = self.connect()
        if status is True:
            cursor = self.cnn.cursor()
            sql_create_table = 'CREATE TABLE IF NOT EXISTS `%s` (`id` int(50) NOT NULL AUTO_INCREMENT,' \
                               '`updateTime` text(0) DEFAULT NULL,' \
                               '`position` text(0) DEFAULT NULL,' \
                               '`address` text(0) DEFAULT NULL,' \
                               '`company` text(0) DEFAULT NULL,' \
                               '`salary` text(0) DEFAULT NULL,' \
                               '`information` text(0) DEFAULT NULL,' \
                               '`workAddress` text(0) DEFAULT NULL,' \
                               '`others` text(0) DEFAULT NULL,' \
                               '`requirement` text(0) DEFAULT NULL,' \
                               '`positionInfo` text(0) DEFAULT NULL,' \
                               '`companyInfo` text(0) DEFAULT NULL,' \
                               '`positionUrl` text(0) DEFAULT NULL,' \
                               '`companyUrl` text(0) DEFAULT NULL,' \
                               'PRIMARY KEY (`id`))ENGINE=MyISAM DEFAULT CHARSET=utf8' % NewTable
            try:
                cursor.execute(sql_create_table)
                self.cnn.commit()

            except mysql.connector.Error as e:
                print('create table orange fails!{}'.format(e))

    def search_table(self, dictInfo, tableName):
        status = self.connect()

        base = "select * from {} where {}"
        tmp = []
        for i in dictInfo.keys():
            tmp.append("{} = \"{}\"".format(i, dictInfo[i]))
            sql_search = base.format(tableName, " and ".join(tmp))

        print(sql_search)

        if status is True and sql_search:
            cursor = self.cnn.cursor()
            try:
                cursor.execute(sql_search)
                for i in cursor:
                    yield i
            except mysql.connector.DataError as e:
                print('query error!{}'.format(e))
            finally:
                cursor.close()
                self.cnn.close()
        else:
            print("Connect Fail.")

    def insert(self, table, dictInfo):
        status = self.connect()
        if status is True:
            cursor = self.cnn.cursor()
            try:
                sql_insert = "insert into {} ({}) values{}".format(
                    table, ",".join(dictInfo.keys()), tuple(dictInfo.values()))
                cursor.execute(sql_insert, ())
                self.cnn.commit()
            except mysql.connector.DataError as e:
                print('insert data error!{}'.format(e))
            finally:
                cursor.close()
                self.cnn.close()
        else:
            print("Connect Fail.")

    def insert_date(self, Table, dictInfo):
        status = self.connect()
        if status is True:
            cursor = self.cnn.cursor()
            try:
                sql_insert = "insert into {} ({}) values{}".format(
                    Table, ",".join(dictInfo.keys()), tuple(dictInfo.values()))
                cursor.execute(sql_insert, ())
                self.cnn.commit()
            except mysql.connector.Error as e:
                print('insert data error!{}'.format(e))
            finally:
                cursor.close()
                self.cnn.close()
        else:
            print("Connect Fail.")


if __name__ == "__main__":
    t = MySQL_Connector(address="127.0.0.1", user="root", database="Position", password="88670211")
    print(t.connect())
    a = t.search_table({"position": "AI工程师"}, "python")
    for i in a:
        print(i)
