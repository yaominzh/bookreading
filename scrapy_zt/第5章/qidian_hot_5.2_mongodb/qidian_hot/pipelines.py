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

import pymongo#导入pymongo库
#将数据保存于MongoDB的Item Pipeline
class MongoDBPipeline(object):
    #Spider开启时，获取数据库配置信息，连接MongoDB数据库服务器
    def open_spider(self,spider):
        #获取配置文件中MongoDB配置信息
        host = spider.settings.get("MONGODB_HOST","localhost")#主机地址
        port = spider.settings.get("MONGODB_PORT",27017)#端口
        db_name = spider.settings.get("MONGODB_NAME","qidian")#数据库名称
        collection_name = spider.settings.get("MONGODB_COLLECTION","hot")#集合名称
        #连接MongoDB，得到一个客户端对象
        self.db_client = pymongo.MongoClient(host=host, port=port)
        self.db_client = pymongo.MongoClient('mongodb://localhost:27017/')
        #指定数据库,得到一个数据库对象
        self.db = self.db_client[db_name]
        #指定集合，得到一个集合对象
        self.db_collection = self.db[collection_name]
    #将数据存储于MongoDB数据库
    def process_item(self, item, spider):
        #将item转换为字典类型
        item_dict = dict(item)
        #将数据插入到集合中
        self.db_collection.insert_one(item_dict)
        return item
    #Spider关闭时，执行数据库关闭工作
    def close_spider(self,spider):
        #关闭数据库连接
        self.db_client.close()