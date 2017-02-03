# -*- coding: utf-8 -*-
import scrapy
from madlan_spider.items import MadlanItem

class MadlanSpider(scrapy.Spider):
    name = "madlan"
    allowed_domains = ["www.madlan.co.il"]
    start_urls = ['http://www.madlan.co.il/local/%D7%9B%D7%A4%D7%A8%20%D7%A1%D7%91%D7%90']

    def parse(self, response):
#    h1_tag = response.xpath('//*[@id="affixTarget"]/div[3]/div[1]/div/div/table/thead/tr/th[1]/text()').extract_first()
#        print h1_tag
        #rows = response.xpath('//table/tbody/tr')
        table_3 = response.xpath('//table')[3]
        rows = table_3.xpath('./tbody/tr')
        print len(rows)
        for row in rows:
            item = MadlanItem()
            item['Address'] = row.xpath('./td[1]/a/text()').extract_first()
            item['Price'] = row.xpath('./td[2]/text()').extract_first()
            #return  item
            #request.meta['item'] = item
            #print ("%s " % item['Address'])
            yield {
                'Address' : item['Address'],
                'Price': item['Price'],
            }

