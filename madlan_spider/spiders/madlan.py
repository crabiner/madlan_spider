# -*- coding: utf-8 -*-
import scrapy
from madlan_spider.items import MadlanItem

class MadlanSpider(scrapy.Spider):
    name = "madlan"
    allowed_domains = ["www.madlan.co.il"]
    start_urls = ['http://www.madlan.co.il/local/%D7%9B%D7%A4%D7%A8%20%D7%A1%D7%91%D7%90']

    def parse(self, response):
        table_3 = response.xpath('//table')[3]
        rows = table_3.xpath('./tbody/tr')
        print len(rows)
        for row in rows:
            item = MadlanItem()
            item['Address'] = row.xpath('./td[1]/a/text()').extract_first()
            item['Price'] = row.xpath('./td[2]/text()').extract_first()
            item['Type'] = row.xpath('./td[3]/text()').extract_first()
            item['Rooms'] = row.xpath('./td[4]/text()').extract_first()
            item['Area'] = row.xpath('./td[5]/text()').extract_first()
            item['Floor'] = row.xpath('./td[6]/text()').extract_first()
            item['Seller'] = row.xpath('./td[7]/text()').extract_first()
            yield {
                'Address' : item['Address'].strip(),
                'Price': item['Price'].strip(),
                'Type': item['Type'].strip(),
                'Rooms': item['Rooms'].strip(),
                'Area': item['Area'].strip(),
                'Floor': item['Floor'].strip(),
                'Seller': item['Seller'].strip(),
            }

