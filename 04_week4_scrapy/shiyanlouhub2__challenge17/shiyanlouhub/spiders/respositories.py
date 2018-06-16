# -*- coding:utf-8 -*-
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
            item = ShiyanlouhubItem()
            item['name'] =i.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('\n\s*(.*)')
            item['datetime'] = i.xpath('.//relative-time/@datetime').extract_first()
            href_next = response.urljoin(i.xpath('.//h3/a/@href').extract_first())
            request=scrapy.Request(href_next,callback=self.parse_next)
            request.meta['item']=item
            yield request
    def parse_next(self,response):
        item = response.meta['item']
        item['commits']=int(response.xpath('(//span[@class="num text-emphasized"])[1]/text()').re_first('[^\d]*(\d*)[^\d]').replace(',',''))
        item['branches']=int(response.xpath('(//span[@class="num text-emphasized"])[2]/text()').re_first('[^\d]*(\d*)[^\d]').replace(',',''))
        
        item['releases']=int(response.xpath('(//span[@class="num text-emphasized"])[3]/text()').re_first('[^\d]*(\d*)[^\d]').replace(',',''))
        yield item
