# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClimbmoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    mname = scrapy.Field()
    years = scrapy.Field()
    score = scrapy.Field()
    director = scrapy.Field()
    mold = scrapy.Field()
    act = scrapy.Field()
    languages = scrapy.Field()
    img = scrapy.Field()
    details = scrapy.Field()
    official = scrapy.Field()
