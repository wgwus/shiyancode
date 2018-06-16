#-*- coding:utf-8 _*-
 
import scrapy

class CoursesFollowSpider(scrapy.Spider):
    name = 'courses_foolow'
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self,response):
        yield{
                'name': response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
                'author':response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()

                }
        
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href').extract():
            yield scrapyRequest(url = response.urljoin(url),callback=self.parse)
