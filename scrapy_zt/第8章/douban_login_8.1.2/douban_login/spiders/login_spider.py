from scrapy import FormRequest,Request
from scrapy.spiders import Spider
from douban_login.items import DoubanLoginItem
import json
import re
class LoginSpider(Spider):
    name = "login"
    #初始请求函数-用于登录功能
    def start_requests(self):
        url = "https://accounts.douban.com/j/mobile/login/basic"
        data={#字典形式的表单数据
            "ck":"",
            "name":"你的用户名",#用户名
            "password":"你的密码",#密码
            "remember":"True",#自动登录，注意是字符串形式
            "ticket":""
        }
        #生成FormRequest形式的请求，提交表单，实现登录功能。
        yield FormRequest(url,formdata=data,method="POST")#默认为POST方式
    #解析函数-判断登录是否成功，并生成访问“我喜欢的电影”的请求
    def parse(self, response):
        result = json.loads(response.text)#将字符串转换为json
        if result["status"] == "success":#登录成功
            #“我的豆列”中“我喜欢的电影”url
            url = "https://www.douban.com/doulist/112189590/"#更改为自己的地址
            yield Request(url,callback=self.parse_doulist)
        else:
            self.logger.info("用户名或密码错误。")

    #解析函数-爬取“我喜欢的电影”信息
    def parse_doulist(self,response):
        doulist = response.xpath("//div[@class='doulist-item']")
        item = DoubanLoginItem()
        for one in doulist:
            try:
                #书名
                title=one.xpath(".//div[@class='title']/a/text()").extract()[0]
                #书籍详情
                details = one.xpath(".//div[@class='abstract']/text()").extract()
                author = re.findall("作者: (.*?)\n",details[0])[0]#作者
                publishing_house = re.findall("出版社: (.*?)\n",details[1])[0]#出版社
                publish_time = re.findall("出版年: (.*?)\n",details[2])[0]#出版年
                #存储到item中
                item["title"] = title.strip("\n").strip(" ").strip("\n")#书名
                item["author"] = author#作者
                item["publishing_house"] = publishing_house#出版社
                item["publish_time"] = publish_time#出版时间
                yield item
            except:
                pass



