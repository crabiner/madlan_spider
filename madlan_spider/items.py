# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
from scrapy.item import Item, Field

class MadlanItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Address = Field()
    Price = Field()
    Type = Field()
    Rooms = Field()
    Space = Field()
    Floor = Field()
    Seller = Field()
#    pass