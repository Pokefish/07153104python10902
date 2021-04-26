
#抓公開資訊網的資料

import os
import requests
import time
import requests
import json
import csv
from datetime import datetime
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from matplotlib.font_manager import FontProperties


#得用正規運算式處理爬取 date&stockNo
date = ["20210301","20210401"]
stockNo = ["2330","1109","1108"]


plt.rcParams['axes.unicode_minus'] = False #負數可正常顯示
font_path =  FontProperties(fname='NotoSansCJKtc-Medium.otf')

df = pd.DataFrame() 
for a in range(len(stockNo)) :
     closing_price_price=[]
     closing_price_date=[]

     for d in range(len(date)) :
          url="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="+ date[d] +"&stockNo="+ stockNo[a] 
          # print(url)
          print(date[d],stockNo[a])
          try :
               res=requests.get(url)
               print(res)
          except Exception :
               if d >= len(date)-1 :
                    # do_some_log()
                    # print(e)
                    pass
          else :
               time.sleep(1)
               print("time.sleep 1 sec")
               pass
     else :
          time.sleep(0.5)
          print("time.sleep 0.5 sec")
     
     # print(a)
     s=json.loads(res.text,encoding='utf8') 
     closing_price_values=list(s.values()) 

     #日期跟收盤價的dataframe 
     for i in range(len(closing_price_values[4])):
          closing_price_price.append(float(closing_price_values[4][i][6]))
          closing_price_date.append(closing_price_values[4][i][0])
          i +=1 
     # print(closing_price_price)
     # print(closing_price_date)
     #公司名
     stock = closing_price_values[2].split(' ',3)  
     title = stock[1]+stock[2] #1是代碼、是公司名
     d += 1    
     df = pd.DataFrame(data = closing_price_price,index = closing_price_date, columns= [title])
# 做圖      
#取當天到前30天 
     df[-30:].plot(figsize = (12, 5),
          fontsize = 15,
          title = title  + "\t趨勢圖",
          linewidth = 2.0) 
     plt.title(title + "\t趨勢圖" ,fontproperties=font_path)
     plt.legend(prop=font_path)
     a += 1

plt.show()