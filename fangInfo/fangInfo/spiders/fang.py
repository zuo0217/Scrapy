# -*- coding: utf-8 -*-
import scrapy


class FangSpider(scrapy.Spider):
    name = 'fang'
    allowed_domains = ['fang.com']
    start_urls = ['http://fang.com/']

    def parse(self, response):
        pass
