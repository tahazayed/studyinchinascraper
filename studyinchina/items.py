# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ScholarshipItem(Item):
    # define the fields for your item here like:
    University = Field()
    Program = Field()
    Degree = Field()
    Duration = Field()
    Instruction_Language = Field()
    uition_Fee_RMB = Field()
    Starting_Date = Field()
    Application_Deadline = Field()
    pass

class RecipeURLItem(Item):
    # define the fields for your item here like:
    url = Field()
    title = Field()    
    pass