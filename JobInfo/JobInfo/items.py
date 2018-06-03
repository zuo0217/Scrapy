# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobinfoItem(scrapy.Item):
    # define the fields for your item here like:
    position = scrapy.Field()  # 职位
    company = scrapy.Field()  # 公司
    address = scrapy.Field()  # 地址
    salary = scrapy.Field()  # 薪资
    updateTime = scrapy.Field()  # 更新时间
    positionUrl = scrapy.Field()  # 职位链接
    companyUrl = scrapy.Field()  # 公司链接
    information = scrapy.Field()  # 信息
    requirement = scrapy.Field()  # 信息
    positionInfo = scrapy.Field()  # 职位信息
    workAddress = scrapy.Field()  # 工作地点
    companyInfo = scrapy.Field()  # 公司信息
    others = scrapy.Field()   # 其他
