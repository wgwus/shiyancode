# -*- coding: utf-8 -*-
import scrapy
from shiyanlouhub.items import ShiyanlouhubItem


class RespositoriesSpider(scrapy.Spider):
    name = 'respositories'
#    allowed_domains = ['https://github.com/shiyanlou?tab=repositories']
    @property
    def start_urls(self):
                        
        url_tmpl ='https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for i in response.css('li.public'):
            item = ShiyanlouhubItem({
                'name': i.xpath('.//h3/a/text()').re('\w.*'),
               'datetime': i.xpath('.//relative-time/@datetime').extract()
                                                                                              })   
            yield item
