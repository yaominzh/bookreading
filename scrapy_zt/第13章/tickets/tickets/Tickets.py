#coding:utf-8
from selenium import webdriver#导入浏览器引擎模块
from selenium.webdriver.common.by import By#导入定位方式模块
from selenium.webdriver.support.ui import WebDriverWait#导入等待模块
from selenium.webdriver.support import expected_conditions as EC#导入预期条件模块
from selenium.common.exceptions import TimeoutException#导入异常模块
from tickets.SitesCode import SitesCode#导入站点处理类
from selenium.webdriver.support.select import Select#导入Select模块
import time
import yagmail#导入邮件模块

class Tickets(object):
    #构造函数
    def __init__(self):
        #1、创建Chrome的对象driver
        self.driver = webdriver.Chrome()#驱动chrome浏览器进行操作
        #2、获取购票信息（出发地、目的地、出发日、乘客、车次）
        self.tickets_info=[]
        self.read_tickets_from_file()
        #生成站点处理类的实例
        self.sites = SitesCode()

    #从文件中读取购票信息
    def read_tickets_from_file(self):
        with open('buy_tickets.txt',"r",encoding="utf-8") as f:
            for line in f:
                self.tickets_info.append(line.strip("\n"))

    #展示登录页面
    def login(self):
        #打开URL对应的页面（登录页面）
        self.driver.get("https://kyfw.12306.cn/otn/login/init")
        try:
            #设置显式等待,最长等待100秒
            wait = WebDriverWait(self.driver, 100)
            #如果登录成功，则会跳转到下面的url页面中
            wait.until(EC.url_to_be('https://kyfw.12306.cn/otn/view/index.html'))
        except TimeoutException:#因超时抛出异常
            return False#异常
        return True


    #查询车票信息
    def query_tickets(self,flag=0):
        if flag == 0:#0：跳转到票务查询页面并填充查询条件
            #1、跳转到车票查询页面
            self.driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
            try:
                #2、设置出发地
                #显式等待，直到出发地输入框被加载
                from_station_input = WebDriverWait(self.driver, 100).until(
                    EC.presence_of_element_located((By.ID, "fromStationText"))# 设定预期条件
                )
                from_station_input.clear()#清除输入框中默认文字
                from_station_input.send_keys(self.tickets_info[0])#输入框中输入出发地
                site_code = self.sites.name_2_code(self.tickets_info[0])#获取站点编码
                #js：设置隐藏的输入框的值为出发地的编码
                js = "document.getElementById(\"fromStation\").value=\""+site_code+"\";"
                #执行js
                self.driver.execute_script(js)

                #3、设置目的地
                time.sleep(1)#暂停1秒
                #显式等待，直到目的地输入框被加载
                to_station_input = WebDriverWait(self.driver, 100).until(
                    EC.presence_of_element_located((By.ID, "toStationText"))# 设定预期条件
                )
                to_station_input.clear()#清除输入框中默认文字
                to_station_input.send_keys(self.tickets_info[1])#输入框中输入出发地

                site_code = self.sites.name_2_code(self.tickets_info[1])#获取站点编码
                #js：设置隐藏的输入框的值为目的地的编码
                js = "document.getElementById(\"toStation\").value=\""+site_code+"\";"
                #执行js
                self.driver.execute_script(js)

                #4、设置出发日
                time.sleep(1)#暂停1秒
                #显式等待，直到出发日输入框被加载
                WebDriverWait(self.driver, 100).until(
                    EC.presence_of_element_located((By.ID, "train_date"))#设定预期条件
                )

                #js：设置输入框的值设值为出发日
                js = "document.getElementById(\"train_date\").value=\""+self.tickets_info[2]+"\";"
                #执行js
                self.driver.execute_script(js)
            except TimeoutException:#因超时抛出异常
                return False#超时

        try:
            #5、点击“查询”按钮
            # 显式等待，直到查询按钮被加载
            WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.ID,"query_ticket")))
            # 如果可以点击找到查询按钮执行点击事件
            searchButton = self.driver.find_element_by_id("query_ticket")
            searchButton.click()
            # 显式等待，直到车票信息被加载
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr")))
        except:
            return False
        return True

    #获取购买车票的详细信息
    def get_ticket(self):
        #1、获取所有车票信息的列表
        #获取所有不包含datatran属性的tr标签
        tr_list = self.driver.find_elements_by_xpath(".//tbody[@id ='queryLeftTable']"
                                                     "/tr[not(@datatran)]")
        #2、定位到购买的车次，获取余票数量，执行预定功能
        for tr in tr_list:
            train_number = tr.find_element_by_class_name('number').text#获取车次编号
            if train_number == self.tickets_info[3]:#找到购买的车次
                if self.tickets_info[4] in ["商务座","特等座"] :
                    #获取商务座余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[2]/div').text
                elif  self.tickets_info[4] == "一等座":
                    #获取一等座余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[3]').text
                elif self.tickets_info[4] == "二等座":#席别：二等座
                    #获取二等座余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[4]').text
                elif  self.tickets_info[4] == "高级软卧":
                    #获取高级软卧余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[5]').text
                elif  self.tickets_info[4] in ["软卧","一等卧"]:
                    #获取软卧/一等卧余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[6]').text
                elif  self.tickets_info[4] == "动卧":
                    #获取动卧余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[7]').text
                elif  self.tickets_info[4] in ["硬卧","二等卧"]:
                    #获取硬卧/二等卧余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[8]').text
                elif  self.tickets_info[4] == "软座":
                    #获取软座"余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[9]').text
                elif  self.tickets_info[4] == "硬座":
                    #获取硬座余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[10]').text
                elif  self.tickets_info[4] == "无座":
                    #获取无座余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[11]').text
                elif  self.tickets_info[4] == "其他":
                    #获取其他余票数量
                    left_ticket = tr.find_element_by_xpath('.//td[12]').text
                else:
                    return -1#席别不存在

                if left_ticket == '--':#席别不存在
                    return -1#席别不存在
                #有票的情况（显示‘有’或具体的余票数量）
                if left_ticket == '有' or left_ticket.isdigit():
                    orderButton = tr.find_element_by_class_name('btn72')#获取预定按钮
                    if orderButton.is_enabled():#按钮可点击
                        orderButton.click()#点击“预定”按钮
                        return 1#按钮可点击，点击了“预定”按钮
                    else:
                        time.sleep(3)#暂停3秒钟
                        return -2#无票
                else:#无票的情况
                    time.sleep(3)#暂停3秒钟
                    return -2#无票或车票还未开售
        return -3#车次不存在

    #关闭温馨提示框
    def children_dialog(self):
        try:
            # 显式等待，直到提示框的确认按钮被加载
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, 'dialog_xsertcj_ok')))
            #获取“确认”按钮
            okButton = self.driver.find_element_by_id('dialog_xsertcj_ok')
            #点击“确认”按钮
            okButton.click()
        except:#抛出异常
            pass

    #预定车票
    def order_ticket(self):
        try:
            #显式等待，直到显示乘客确认页面
            WebDriverWait(self.driver, 100).until(
                EC.url_to_be('https://kyfw.12306.cn/otn/confirmPassenger/initDc'))
            #显式等待，直到所有的乘客信息被加载完毕
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (By.XPATH, ".//ul[@id='normal_passenger_id']/li")))
        except TimeoutException:#因超时抛出异常
            return False
        #获取所有的乘客信息
        passanger_labels = self.driver.find_elements_by_xpath(
            ".//ul[@id='normal_passenger_id']/li/label")
        order_passangers = self.tickets_info[5].split(",")#获取购票的乘客姓名
        #勾选所有购票的乘客
        amount = 0#购票乘客数量
        for passanger_label in passanger_labels:#遍历所有的label标签
            name = passanger_label.text#获取乘客的姓名
            if name in order_passangers:#判断姓名是否与购票乘客的名字吻合
                amount+=1
                passanger_label.click()#选择购票乘客（checkbox为选中状态）
                self.children_dialog()#如果是儿童，会弹出提示框，需要点击确认
        #席别
        SEAT_TYPE = {
            "商务座": '9',  #商务座
            "特等座": 'P',  #特等座
            "一等座": 'M',  #一等座
            "二等座": 'O',  #二等座
            "高级软卧": '6',  #高级软卧
            "软卧": '4',  #软卧
            "硬卧": '3',  #硬卧
            "软座": '2',  #软座
            "硬座": '1',  #硬座
            "无座": '1',  #无座
        }
        #选择席别
        for i in range(1,amount+1):#遍历所有
            id = 'seatType_%d'%i
            #根据value值选择坐席
            value = SEAT_TYPE[self.tickets_info[4]]#获取预定的席别
            Select(self.driver.find_element_by_id(id)).select_by_value(value)

        #获取提交订单的按钮
        submitButton = self.driver.find_element_by_id('submitOrder_id')
        submitButton.click()#点击提交按钮，提交订单
        return True

    #核对信息确认框
    def confirm_dialog(self):
        try:
            #显式等待，直到核对订单确认框被加载
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'dhtmlx_wins_body_outer')))
            # 显式等待，直到确认按钮被加载
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.ID, 'qr_submit_id')))
            time.sleep(2)#等待“确认”按钮可用
            #点击“确认”按钮
            ConButton = self.driver.find_element_by_id('qr_submit_id')
            # 如果页面显示确认按钮，则点击该按钮
            if ConButton.is_displayed():
                ConButton.click()
                return True
            else:
                return False #余票不足，需要重新回到票务信息页面
        except TimeoutException:#因超时抛出异常
            return False

    #发送邮件
    def mail_to(self,):
        try:
            #显式等待，直到购票页面被加载（说明购票成功）
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'i-lock')))
            #连接邮件服务器
            yag = yagmail.SMTP(user='user@163.com',#用户名
                               password='XXXXXX',#密码
                               host='smtp.163.com',#主机
                               port='465')#端口
            message = "亲，抢票成功，请在半个小时之内前往支付!"
            #发送邮件
            yag.send(to=self.tickets_info[6],#目标邮箱地址（从buy_tickets.txt中获取）
                     subject='12306购票成功通知',#邮件标题
                     contents=message)#邮件内容
        except TimeoutException:#因超时抛出异常
            return False
        return True

    #保持登录状态
    def keep_loading(self):
        try:
            #获取链接
            link = self.driver.find_element_by_id('login_user')
            #点击链接
            link.click()
        except:#抛出异常
            pass

    #显示提示框
    def show_message(self,msg):
        pass
        # 调用js
        self.driver.execute_script("alert(\""+msg+"\");")

    #判断站点是否存在
    def site_is_exist(self):
        if False==self.sites.is_exist(self.tickets_info[0]):#判断出发地的站点是否存在
            return -1
        if False==self.sites.is_exist(self.tickets_info[1]):#判断目的地的站点是否存在
            return -2
        return 0

