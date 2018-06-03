#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Create time : 2018/6/3下午12:56
# Create by Saseny.Zhou
# File name: csv_read.py

import csv


def writeCsv(path, list):
    """列表方式写入CSV文件"""
    try:
        csvFile = open(path, "a")
        f_write = csv.writer(csvFile)
        f_write.writerow(list)
        csvFile.close()
    except:
        print('Write CSV file Fail')


def readCsvRow(path):
    """以读行的方式读取csv文件"""
    return_list = []
    try:
        csvRead = open(path, "r")
        reader = csv.reader(csvRead)
        for i in reader:
            return_list.append(i)
        csvRead.close()
    except:
        print("read File Error.")
    return return_list


def readCsvDict(path):
    """以读字典的方式读取csv文件"""
    return_list = []
    try:
        csvRead = open(path, "r")
        reader = csv.DictReader(csvRead)
        for i in reader:
            return_list.append(i)
        csvRead.close()
    except:
        print("read File Error.")
    return return_list


def writeFile(path, string):
    """输入string类型写入文档"""
    try:
        f = open(path, "a")
        f.write(string)
        f.close()
    except:
        print('Write File Fail')
