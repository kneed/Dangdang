# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DangdangPipeline(object):
    def process_item(self, item, spider):
        db=pymysql.connect(host="localhost",port=3306,user="root",password="739535841",db="dangdang",charset="utf8")#连接数据库
        cursor=db.cursor()#获取一个可供操作数据库的游标
        sql='INSERT INTO python(name,summary,address,price)VALUES(%s,%s,%s,%s)'
        try:
            print('传输进数据库')
            for n,s,a,pr in zip(item['name_'],item['summary_'],item['address_'],item['price_']):
                cursor.execute(sql,(n,s,a,pr))
                db.commit()
                print('commit suceessful')
        except:
            db.rollback()
            print('failed to commit')
        finally:
            db.close()
        return item
