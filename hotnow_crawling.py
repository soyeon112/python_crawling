from asyncio.windows_events import NULL
from os import link
from sqlite3 import Time
from numpy import append
from selenium import webdriver
import time
import pandas as pd
import csv
from bs4 import BeautifulSoup as bs
import urllib.request

driver = webdriver.Chrome('C:/Users/kimso/Desktop/Kosta_python/chromedriver')
url = 'https://www.krispykreme.co.kr/popup/pop_today_hot_hour.asp'  #hotnow popup llink
driver.get(url)
driver.implicitly_wait(time_to_wait=20) #로딩 기다림

#hotnow 클릭
#driver.find_element_by_css_selector(".btn_store_search > a").click()
#time.sleep(2)


def setTime(in_time):
    #시간 설정
    driver.find_element_by_xpath("//option[@value='" + str(in_time) + "']").click()
    #검색btn 클릭
    driver.find_element_by_xpath("//input[@type = 'image']").click()  
    time.sleep(2)
    
    #매장 갯수 저장
    store_cnt = driver.find_element_by_css_selector("span.data_txt").text
    store_cnt = int(store_cnt)
    print('count = ',store_cnt)  
    
    
    if store_cnt > 0:
         #해당 시간에 hotnow하는 매장 정보
        storeInfo = driver.find_elements_by_class_name("clfix")
        
        for info in storeInfo:
            imgURL = info.find_element_by_css_selector("span.img > img").get_attribute("src")
            imgsave = info.find_element_by_css_selector("span.img > img").get_attribute("alt")
            urllib.request.urlretrieve(imgURL,imgsave+'.jpg')
            name = info.find_element_by_css_selector("div.info > span.place_name").text
            times = info.find_element_by_css_selector("div.info > span.time").text
            link = info.find_element_by_css_selector("div.info > a").get_attribute("href")
            print(imgURL,imgsave,name,times,link)
            
            #값 저장
            sto_cnt.append(in_time)
            img_li.append(imgURL)
            imgname_li.append(imgsave)
            name_li.append(name)
            time_li.append(times)
            link_li.append(link)
    else:
        sto_cnt.append(in_time)
        img_li.append('NONE')
        imgname_li.append('NONE')
        name_li.append('NONE')
        time_li.append('NONE')
        link_li.append('NONE')
        print('매장 없음')    
   
sto_cnt=[]
name_li=[]
time_li=[]
link_li=[]
img_li =[]
imgname_li=[]
   
for idx in range(7,25,1): #7시-24시 모두 검색
    setTime(idx)

# csv 
df = pd.DataFrame()
df['time'] = sto_cnt
df['img'] = img_li
df['imgname'] = imgname_li
df['store'] = name_li
df['times'] = time_li
df['link'] = link_li

df.to_csv('hotnow_test_img.csv',encoding='cp949') 

print('============')

driver.quit(); #프로세스 종료.