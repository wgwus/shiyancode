import scrapy


#ponse.xpath('//h3/a/@href').extract()
#ponse.xpath('//h3/a/text()').re('\w.*')
#get url href ,wait get frush time

class start_spider_git_page1(scrapy.Spider):
    name = "github-spider"
    @property
    def start_urls(self):
        
        url_tmpl ='https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for i in response.css('li.public'):
            yield {'name': i.xpath('.//h3/a/text()').re('\w.*'),
               'time': i.xpath('.//relative-time/@datetime').extract()
               }
       # response.xpath('//h3/a/@href').extract()
'''
href_list = start_spider_git_page1().parse()
class start_spider_gitpage2(spyder.Spider):
    name = 'github-spider2'
    def start_urls(self):
        for i in href_list:
            return i
            

    def parse(self,response):
        response.xpath('//span').re_first('datetime="(.+)"')
        '''
