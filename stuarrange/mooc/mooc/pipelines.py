# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


def dbHandle():
    conn = pymysql.connect(
        host="120.46.3.93",
        user="root",
        passwd="0411mtxM+",
        charset="utf8",
        use_unicode=False
    )
    return conn


class MoocPipeline:
        def process_item(self, item, spider):
            dbObject = dbHandle()
            cursor = dbObject.cursor()
            cursor.execute("USE SPIDER")
            # 插入数据库
            sql = "INSERT INTO COURSES(NAME,IMG,STATUS,PRICE,LINK) VALUES(%s,%s,%s,%s,%s)"
            try:
                cursor.execute(sql,
                               (item['name'], item['img'], item['status'],item['price'],item['linque']))
                cursor.connection.commit()
            except BaseException as e:
                print(e)
                dbObject.rollback()
            return item
