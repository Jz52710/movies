# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import ClimbmoviesItem
import json
import re

class DoubanurlsSpider(scrapy.Spider):
    name = 'doubanurls'#爬虫的名字
    allowed_domains = ['movie.douban.com']#爬取域名
    start_urls = ['https://movie.douban.com/']#爬取页面地址

    #取链接
    def start_requests(self):
        start_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=0'
        yield scrapy.Request(url=start_url,callback=self.parse)
    #读链接
    def parse(self, response):
        main_data = json.loads(response.body.decode("utf-8"))
        for i in main_data['subjects']:
            urls = i['url']
            print(urls)
            yield scrapy.Request(url=urls,callback=self.url)
    #xpath选择
    def url(self,response):
        for data in response.xpath('//div[@id="content"]'):
            item = ClimbmoviesItem()
            item['mname'] = "".join(data.xpath('h1/span[1]/text()').extract()).strip()#电影名
            item['years'] = "".join(data.xpath('h1/span[2]/text()').extract()).strip()#时间
            item['score'] = "".join(data.xpath('//div[@id="interest_sectl"]/div[@class="rating_wrap clearbox"]/div[@class="rating_self clearfix"]/strong[@class="ll rating_num"]/text()').extract())#评分
            item['director'] = "".join(data.xpath('//div[@id="info"]/span[1]/span[2]/a/text()').extract())#导演
            item['mold'] = "/".join(data.xpath('//div[@id="info"]/span[@property="v:genre"]/text()').extract())  #类型
            item['act'] = "/".join(data.xpath('//div[@id="info"]/span[3]/span[2]/a/text()').extract())#主演
            item['languages'] = "".join(re.findall('<span class="pl">语言:</span>(.*?)<br/>', response.body.decode())).strip()#语言
            item['img'] = "".join(data.xpath('//div[@id="mainpic"]/a/img/@src').extract())#图片
            item['details'] = "".join(data.xpath('//meta[@name="mobile-agent"]/@content').extract()).replace("format=html5; url=","")#详情
            item['official'] = "".join(data.xpath('//div[@id="info"]/a[1]/@href').extract())#官网
            yield item

