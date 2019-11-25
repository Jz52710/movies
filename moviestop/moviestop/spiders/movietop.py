# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import MoviestopItem

class MovietopSpider(scrapy.Spider):
    name = 'movietop'
    allowed_domains = ['douban-api.uieee.com/v2/movie/top250']
    start_urls = ['https://douban-api.uieee.com/v2/movie/top250?count=100']

    def parse(self, response):
        main_data = json.loads(response.body.decode("utf-8"))
        for items in main_data['subjects']:
            item = MoviestopItem()
            item['score'] = items['rating']['average']#评分
            item['mold'] = "/".join(items['genres'])#类型
            item['mname'] = items['title']#名字
            arr = []
            for val in items['casts']:
                a = val['name']
                arr.append(a)
            item['act'] = "/".join(arr)#演员
            arr1 = []
            for val in items['directors']:
                name = val['name']
                arr1.append(name)
            item['director'] = "/".join(arr1)#导演
            item['years'] = items['year']#年份
            item['img'] = items['images']['small']#图片
            item['details'] = items['alt']#详情
            yield item

