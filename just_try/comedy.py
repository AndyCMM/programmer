# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:58:27 2018

@author: Andy
"""
import requests
from bs4 import BeautifulSoup
import requests.exceptions
def getContent(url,**key):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print('connect erro ',e)
    return response.text

if __name__ =='__main__':
    pass
    url = 'https://bj.lianjia.com/ershoufang/rs%E4%B8%8A%E6%B5%B7/'
    soup = BeautifulSoup(getContent(url),'html5lib')
    with open('temp_yuanshihtml.txt','w',encoding='utf-8') as f:
        f.write(getContent(url))
    f.close()
   # print(type(soup.prettify()))
    #print(soup.prettify)  

    #content = soup.find('ul',{'class':'sellListContent'});
    content = soup.select('.sellListContent')[0]
  #  print(type(content))
#    print(len(content.select('.sellListContent ')) )   
#    print(len(soup.select('.sellListcontent .clear LOGCLICKDATA')))
    with open('temp_html.txt','w',encoding='utf-8') as f:
        f.write(content.prettify())
    f.close()
    print(len(content.find_all('li')))
    b = content.find_all('li')
    print((b[29].a['href']))
#    for item in content.find_all('li'):
#        print((item))
#        break
   
#%%
from selenium import webdriver
browser = webdriver.Chrome()
try:
    browser.get('http://www.taobao.com')
    input = browser.find_element_by_id('q')
    print(input)
    
finally:
    browser.close()





     