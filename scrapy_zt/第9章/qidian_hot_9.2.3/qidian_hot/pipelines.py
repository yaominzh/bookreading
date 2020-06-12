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

#将数据保存于文本文档中的Item Pipeline
class SaveToTxtPipeline(object):
    file = None              #文件对象
    @classmethod
    def from_crawler(cls,crawler):
        #获取配置文件中的FILE_NAME的值
        # 如果获取失败，使用默认值"hot2.txt"
        cls.file_name = crawler.settings.get("FILE_NAME","hot2.txt")
        return cls()
    #Spider开启时，执行打开文件操作
    def open_spider(self,spider):
        #以追加形式打开文件
        self.file = open(self.file_name,"a",encoding="utf-8")

    #数据处理
    def process_item(self, item, spider):
        #获取item中各个字段，将其连接成一个字符串
        # 字段之间用分号隔开
        # 字符串末尾要有换行符\n
        novel_str = item['name']+";"+\
                    item["author"]+";"+\
                    item["type"]+";"+\
                    item["form"]+"\n"
        # 将字符串写入到文件中
        self.file.write(novel_str)
        return item

    #Spider关闭时，执行关闭文件操作
    def close_spider(self,spider):
        #关闭文件
        self.file.close()