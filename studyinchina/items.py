# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from collections import OrderedDict
import six

class ScholarshipItem(Item):
    University = Field()
    Program = Field()
    Degree = Field()
    Duration = Field()
    Instruction_Language = Field()
    Tuition_Fee_RMB = Field()
    Starting_Date = Field()
    Application_Deadline = Field()
    pass
    
 