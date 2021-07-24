from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

drivePath = './chromedriver'
browser = webdriver.Chrome(drivePath) #打開
browser.implicitly_wait(10) #等十秒
browser.set_window_size(800,700) #視窗大小

#網頁本身
url = 'https://www.dcard.tw/f/makeup'
browser.get(url)


name_arr = []
title_arr = []
url_arr = []

#作者
author = browser.find_elements_by_class_name('tgn9uw-1.ceKcvN')
for item in author : 
     if item:
          name_arr.append(item.text)

title = browser.find_elements_by_class_name('tgn9uw-3.cUGTXH')
for item in title : 
     if item:
          title_arr.append(item.text)# 標題
          url_arr.append(item.get_attribute('href'))# 超連結

#用title數量才正確
# for i in range(len(title_arr)):
#      print('name:',name_arr[i])
#      print('title:',title_arr[i])
#      print('url:',url_arr[i])

#進去文章抓內文
ans = []
for i in range(len(title_arr)):
     url_content = url_arr[i]
     browser.get(url_content)
     content = browser.find_elements_by_class_name('phqjxq-0.fQNVmg')
     ans.append(content.text)
# (sc-1npvbtq-0.gfjrnD)
# (phqjxq-0.fQNVmg)
print(ans)

browser.close()

