# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from scrapy.exceptions import DropItem#异常
# import logging
# logger = logging.getLogger("SaveFilePipeline")

class SeabornFileDownloadPipeline(object):
    def process_item(self, item, spider):
        return item

from scrapy.pipelines.files import FilesPipeline#导入文件管道类
from scrapy import Request
#定义新的文件管道，继承于FilesPipeline
class SaveFilePipeline(FilesPipeline):
    # #构造并返回下载Request请求
    # def get_media_requests(self, item, info):
    #     # 获取文件url，构造文件下载Request请求
    #     yield  Request(url = item["file_urls"][0])
    # #文件下载（或下载失败）后调用该方法
    # def item_completed(self, results, item, info):#判断是否正确下载
    #     if not results[0][0]:
    #         raise DropItem("文件下载失败")
    #     #打印日志
    #     logger.debug("文件下载成功")
    #
    #     return item

    #设定文件名称，并返回
    def file_path(self, request, response=None, info=None):
        #获取文件名，并返回
        return request.url.split("/")[-1]
        #获取文件名
        # file_name = request.url.split("/")[-1]
        # #确定文件夹的名称
        # folder_name = file_name.split(".")[0]
        # #返回文件夹和文件组合的字符串
        # return folder_name+"/"+file_name
