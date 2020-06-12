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
#导入mysql库
import MySQLdb
#将数据保存于MySQL的Item Pipeline
class MySQLPipeline(object):
    #Spider开启时，获取数据库配置信息，连接MySQL数据库服务器
    def open_spider(self,spider):
        #获取配置文件中MySQL配置信息
        db_name = spider.settings.get("MYSQL_DB_NAME","qidian")#数据库名称
        host = spider.settings.get("MYSQL_HOST","localhost")#主机地址
        user = spider.settings.get("MYSQL_USER","root")#用户名
        pwd = spider.settings.get("MYSQL_PASSWORD","1234")#密码
        #连接MySQL数据库服务器
        self.db_conn = MySQLdb.connect(db=db_name,
                                       host=host,
                                       user=user,
                                       password=pwd,
                                       charset="utf8")

        #使用cursor()方法获取操作游标
        self.db_cursor = self.db_conn.cursor()

    #将数据存储于MySQL数据库
    def process_item(self, item, spider):
        #获取item中各个字段，保存于元组中
        values = (item['name'],
                  item["author"],
                  item["type"],
                  item["form"])
        # 插入数据的SQL语句
        sql = 'insert into hot(name,author,type,form)values(%s,%s,%s,%s)'
        #执行SQL语句，实现插入功能
        self.db_cursor.execute(sql,values)
        return item
    #Spider关闭时，执行数据库关闭工作
    def close_spider(self,spider):
        self.db_conn.commit() #提交数据
        self.db_cursor.close()#关闭游标
        self.db_conn.close()  #关闭数据库