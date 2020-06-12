from scrapy import  cmdline
while True:
    cmdline.execute("scrapy crawl movies -o movies.csv".split())