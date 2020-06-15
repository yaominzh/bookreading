[toc]
# chap04
start_requests() 爬虫启动时，引擎自动调用该方法，并且只会被调用一次
伪装浏览器、自动登录等功能都是在request对象中设置的
### chap4.1.4
scrapy提取数据有自己的一套机制

# chap05
## chap5-2 mongodb1
SQL 与MongoDB中的术语对照

| 术语 | SQL | MongoDB
| --- | --- | ---
| 数据库| database | database
| 表-集合 | table | collection
| 行-文档 | row | document
| 列-域 | column | field
| 索引 | index | index
| 主键 | primary key | primary key 

db操作时如db = db_client["test"]指定的数据库不存在的话会自动创建一个该名称的数据库

## chap5-3 redis
