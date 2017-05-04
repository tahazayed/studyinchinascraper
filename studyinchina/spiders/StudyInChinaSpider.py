# -*- coding: utf-8 -*-
import scrapy
from studyinchina.items import ScholarshipItem
from bs4 import BeautifulSoup
from datetime import datetime
from studyinchina.mongodal import MongoDAL
from time import sleep
from scrapy.selector import Selector
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


class StudyInChinaSpider(scrapy.Spider):
    name = "studyinchinaspider"
    allowed_domains = ["www.csc.edu.cn"]
    base_url = 'http://www.csc.edu.cn/studyinchina/programsearchen.aspx?PageNo=%s'
    start_urls = [base_url % 1]
    pageid = 1

    

    def parse(self, response):
        scholarships = Selector(response).xpath('//div[@class="zy_list blue"]')
        print(len(scholarships))
        for scholarship in scholarships:
            item = ScholarshipItem()

            item['University'] = scholarship.xpath(
                'div[@class="mingcheng"]/a/text()').extract()
            item['Program'] = scholarship.xpath(
                'div[@class="zhuanye"]/text()').extract()
            item['Degree'] = scholarship.xpath(
                'div[@class="degree"]/text()').extract()
            item['Duration'] = scholarship.xpath(
                'div[@class="xuezhi"]/text()').extract()
            item['Instruction_Language'] = scholarship.xpath(
                'div[@class="yuyan"]/text()').extract()
            item['uition_Fee_RMB'] = scholarship.xpath(
                'div[@class="xuefei"]/text()').extract()
            item['Starting_Date'] = scholarship.xpath(
                'div[@class="rx_date"]/text()').extract()
            item['Application_Deadline'] = scholarship.xpath(
                'div[@class="sq_date"]/text()').extract()
               
            yield item
			
        if len(scholarships)>0:
            self.pageid = self.pageid + 1    
            next_page = self.base_url % self.pageid
            yield scrapy.Request(url=next_page, callback=self.parse,meta={'dont_merge_cookies': False},dont_filter=True,encoding='utf-8',errback=self.errback)    

    def errback(self, response):
        pass

"""
#configure_logging()
runner = CrawlerRunner(get_project_settings())

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(StudyInChinaSpider)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished
"""