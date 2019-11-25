# -*- coding: utf-8 -*-
import pymysql.cursors
from . import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ClimbmoviesPipeline(object):
    def __init__(self):
        #链接数据库
        self.connect = pymysql.connect(host=settings.MYSQL_HOST,user=settings.MYSQL_USER,password=settings.MYSQL_PASSWD,db=settings.MYSQL_DBNAME,port=settings.MYSQL_PORT,charset='utf8',use_unicode=True,autocommit=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """select * from moviebackgrounds_movieinformation where mname = %s""",
                item['mname'])
            # 去重
            repetition = self.cursor.fetchone()
            if repetition is not None:
                pass
            else:
                self.cursor.execute(
                    "INSERT INTO moviebackgrounds_movieinformation(mname,years,score,director,mold,act,languages,img,details,official) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (item['mname'],
                    item['years'],
                    item['score'],
                    item['director'],
                    item['mold'],
                    item['act'],
                    item['languages'],
                    item['img'],
                    item['details'],
                    item['official']
                     ))
                self.connect.commit()
        except Exception as error:
            print(error)
        return item
    def close_spider(self,spider):
        self.cursor.close()#关游标
        self.connect.close()#关链接
