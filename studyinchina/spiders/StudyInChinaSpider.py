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
    pageid = 1
    max_pageid = 1
    start_urls = [base_url % pageid]


    

    def parse(self, response):
    
        if self.max_pageid == 1:
            self.max_pageid = int(Selector(response).xpath('//*[@id="zy_box"]/div[1]/text()').extract()[2].replace('/',''))
        
        scholarships = Selector(response).xpath('//div[@class="zy_list blue"]')

        for scholarship in scholarships:
        
            item = ScholarshipItem()
            try:
                item['University'] = scholarship.xpath('div[@class="mingcheng"]/a/text()').extract()[0].strip()
            except:
                item['University'] = ''
                pass
                
            starred = ''
            try:
                starred=scholarship.xpath('div[@class="zhuanye"]/font[@class="font-red"]/text()').extract()[0].strip()
            except:
                pass 
                
            try:
                item['Program'] = starred + scholarship.xpath('div[@class="zhuanye"]/text()').extract()[0].strip()
            except:
                item['Program'] = ''
                pass  
                
            try:
                item['Degree'] = scholarship.xpath('div[@class="degree"]/text()').extract()[0].strip()
            except:
                item['Degree'] = ''
                pass
                
            try:                
                item['Duration'] = scholarship.xpath('div[@class="xuezhi"]/text()').extract()[0].strip()
            except:
                item['Duration'] = ''
                pass
            
            try:            
                item['Instruction_Language'] = scholarship.xpath('div[@class="yuyan"]/text()').extract()[0].strip()
            except:
                item['Instruction_Language'] = ''
                pass

            try:                
               item['Tuition_Fee_RMB'] = scholarship.xpath('div[@class="xuefei"]/text()').extract()[0].strip()
            except:
                item['Tuition_Fee_RMB'] = ''
                pass

            try:                
                item['Starting_Date'] = scholarship.xpath('div[@class="rx_date"]/text()').extract()[0].strip()
            except:
                item['Starting_Date'] = ''
                pass

            try:
                item['Application_Deadline'] = scholarship.xpath('div[@class="sq_date"]/text()').extract()[0].strip()
            except:
                item['Application_Deadline'] = ''
                pass
                
            yield item
            
        if self.pageid < self.max_pageid:
            self.pageid = self.pageid + 1    
            next_page = self.base_url % self.pageid
            yield scrapy.Request(url=next_page, callback=self.parse,meta={'dont_merge_cookies': False},dont_filter=True,encoding='utf-8',errback=self.errback)    

    def errback(self, response):
        pass

"""            

"""

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