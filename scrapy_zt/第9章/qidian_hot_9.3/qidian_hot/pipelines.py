# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis#导入redis库
class QidianHotPipeline(object):
    #Spider开启时，获取数据库配置信息，连接redis数据库服务器
    def open_spider(self,spider):
        if spider.name == "xici":
            #获取配置文件中redis配置信息
            host = spider.settings.get("REDIS_HOST")#主机地址
            port = spider.settings.get("REDIS_PORT",)#端口
            db_index = spider.settings.get("REDIS_DB_INDEX")#索引
            db_psd = spider.settings.get("REDIS_PASSWORD")#密码
            #连接redis，得到一个连接对象
            self.db_conn = redis.StrictRedis(host=host,port=port,db=db_index,
                                             password=db_psd,decode_responses=True)
            self.db_conn.delete("ip")

    #将数据存储于redis数据库
    def process_item(self, item, spider):
        if spider.name == "xici":
            #将item转换为字典类型
            item_dict = dict(item)
            #将item_dict保存于key为ip的集合中
            self.db_conn.sadd("ip",item_dict["url"])
        return item
