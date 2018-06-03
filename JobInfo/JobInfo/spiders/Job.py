# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from page_read.json_read import *


class JobSpider(scrapy.Spider):
    name = 'Job'
    allowed_domains = ['51job.com']
    urlInfo = read_json_file("config/startUrl.json")
    start_urls = []
    start_urls.append(urlInfo["start"])
    for i in range(2, urlInfo["pageNumber"]):
        start_urls.append(urlInfo["default"].format(i))

    print(start_urls)

    def parse(self, response):
        jpy = PyQuery(response.text)
        items = jpy('.el').items()
        for item in items:
            position = item('.t1 > span > a').text()
            positionUrl = item('.t1 > span > a').attr('href')
            company = item('span.t2 > a').text()
            companyUrl = item('span.t2 > a').attr('href')
            address = item('.t3').text()
            salary = item('.t4').text()
            updateTime = item('.t5').text()

            if position:
                info = {
                    "position": position,
                    "company": company,
                    "positionUrl": response.urljoin(positionUrl),
                    "companyUrl": response.urljoin(companyUrl),
                    "address": address,
                    "salary": salary,
                    "updateTime": updateTime
                }
                yield scrapy.Request(info["positionUrl"], meta={"info": info}, callback=self.parse_second)

    def parse_second(self, response):
        info = response.meta["info"]
        jpy = PyQuery(response.text)
        info["information"] = "|".join(jpy('.msg.ltype').text().split("   |  "))
        info["requirement"] = jpy('.sp4').text()
        info["others"] = jpy('.t2').text()
        info["workAddress"] = jpy(
            'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(3) > div > p').text().replace(
            "上班地址：", "")
        info["companyInfo"] = jpy(
            'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(4) > div').text()
        info["positionInfo"] = jpy(
            'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(2) > div').text()
        return info
