# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from douban.items import DoubanItem  #导入Item类
import json
class MoviesSpider(Spider):
    name = 'movies'
    currentPage = 1#当前页，默认为1

    def start_requests(self):#获取初始请求
        url = "https://movie.douban.com/j/new_search_subjects?tags=电影&start=0&countries=中国大陆"
        #生成请求对象
        yield Request(url)

    def parse(self, response):#数据解析
        item = DoubanItem()#生成DoubanItem对象
        #获取到json格式的数据
        json_text = response.text
        #使用json.loads解码json数据，返回Python支持的数据类型
        #这里的movie_dict是一个字典类型
        movie_dict = json.loads(json_text)
        if len(movie_dict["data"]) == 0:#如果没有数据，退出爬虫
            return
        #for循环遍历每部电影
        for one_movie in movie_dict["data"]:
            #获取电影名称
            item["title"] = one_movie["title"]
            #获取导演
            item["directors"] = one_movie["directors"]
            #获取演员
            item["casts"] = one_movie["casts"]
            #获取评分
            item["rate"] = one_movie["rate"]

            yield item
        #爬取更多数据
        url_next = 'https://movie.douban.com/j/new_search_subjects?tags=电影&start=%d&countries=中国大陆'%(self.currentPage*20)
        self.currentPage+=1
        yield Request(url_next)
