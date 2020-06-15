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

# chap06
## chap6-2

JSON - JavaScript Object Notation
1. 数据在名称/值对中
2. 数据由逗号分隔
3. 花括号保存对象
4. 方括号保存数组

AJAX - Asynhronous JavaScript and XML

# chap07
## chap7-3
selenium极大方便了动态页面数据提取，但要操作浏览器，无法实现异步和大规模页面的爬取。 splash可以

splash是一个官方推荐的JavaScript渲染服务，是一个带有http api的轻量级浏览器，同时对接了python中的twisted和QT库。

