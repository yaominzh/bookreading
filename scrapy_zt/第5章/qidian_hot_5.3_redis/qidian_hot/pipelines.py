# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class QidianHotPipeline(object):
    def process_item(self, item, spider):
        #判断小说形式是连载还是完结
        if item["form"] == "连载":#连载的情况
            item["form"] = "LZ"#替换为简称
        else:#其他情况
            item["form"] = "WJ"
        return item

#去除重复作者的Item Pipeline
class DuplicatesPipeline(object):
    def __init__(self):
        #定义一个保存作者姓名的集合，
        self.author_set = set()
    def process_item(self, item, spider):
        if item['author'] in self.author_set:
            #抛弃重复的Item项
            raise DropItem("查找到重复姓名的项目: %s"%item)
        else:
            self.author_set.add(item['author'])
        return item

import redis#导入redis库
#将数据保存于redis的Item Pipeline
class RedisPipeline(object):
    #Spider开启时，获取数据库配置信息，连接redis数据库服务器
    def open_spider(self,spider):
        #获取配置文件中redis配置信息
        host = spider.settings.get("REDIS_HOST")#主机地址
        port = spider.settings.get("REDIS_PORT",)#端口
        db_index = spider.settings.get("REDIS_DB_INDEX")#索引
        db_psd = spider.settings.get("REDIS_PASSWORD")#密码
        #连接redis，得到一个连接对象
        self.db_conn = redis.StrictRedis(host=host,port=port,db=db_index,
                                         password=db_psd)

    #将数据存储于redis数据库
    def process_item(self, item, spider):
        #将item转换为字典类型
        item_dict = dict(item)
        #将item_dict保存于key为novel的列表中
        self.db_conn.sadd("novel",item_dict)
        return item
    #Spider关闭时，执行数据库关闭工作
    def close_spider(self,spider):
        #关闭数据库连接
        self.db_conn.connection_pool.disconnect()