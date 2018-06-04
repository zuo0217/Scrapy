# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pandas
import os
from databases.mysqlDB import *
from page_read.json_read import *


class JobinfoPipeline(object):
    data_list = []
    tableInfo = read_json_file("config/startUrl.json")
    dbInfo = read_json_file("config/config.json")["mysql"]
    t = MySQL_Connector(address=dbInfo["ip"], user=dbInfo["username"], database=dbInfo["database"],
                        password=dbInfo["password"])
    t.create_table(tableInfo["table"])

    def open_spider(self, spider):
        pathFolder = os.path.join(os.path.expanduser("~"), "Downloads/招聘信息")
        if not os.path.isdir(pathFolder):
            os.makedirs(pathFolder)
        self.file = os.path.join(pathFolder, "{}({}).xlsx".format(self.tableInfo["table"], self.tableInfo["city_name"]))

    def close_spider(self, spider):
        self.pd = pandas.DataFrame(self.data_list)
        self.pd.to_excel(self.file, encoding='utf-8', index=False)

    def process_item(self, item, spider):
        tmpDict = {}
        for i in self.getKeys():
            tmpDict[i] = item[i]
        self.data_list.append(item)
        try:
            info = self.t.search_table(tmpDict, self.tableInfo["table"])
            getInfo = info.__next__()
            if getInfo[1] != item["updateTime"]:
                self.t.update(self.tableInfo["table"], getInfo[0], item["updateTime"])
        except:
            self.t.insert(self.tableInfo["table"], item)
            return item

    def getKeys(self):
        info = read_json_file("config/config.json")["duplicate key"]
        keys = []
        for i in info.keys():
            if info[i] is True:
                keys.append(i)
        return keys
