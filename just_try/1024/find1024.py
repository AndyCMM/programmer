# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 23:00:18 2018

@author: Andy
"""
import json
import requests
import time
from bs4 import BeautifulSoup
import chardet
import os
import pymongo
from hashlib import md5
from multiprocessing import Pool
from functools import partial
import random
from urllib.parse import urlencode

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


client = pymongo.MongoClient('localhost')
db = client['1024']
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko)\
     Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/\
    16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
#    with open('F:\Andy_private\python\effectIP.txt','r') as f:
#    proxy = json.load(f)
#    f.close()
broswer = webdriver.Chrome()
wait = WebDriverWait(broswer, 20)

proxies = [
    'https://218.22.7.62:53281',
    'http://58.251.250.96:8118',
    'https://113.116.146.141:9000',
    'https://114.249.112.180:9000'
]
# proxy  = {
#  "http": "http://115.154.38.147:1080",
# # "https": "http://10.10.1.10:1080",
# }


def findPage(url):
    """
    :return:int
    """

    try:
        # pro = {'http': random.choice(proxies)}
        # print(pro)
        # response = requests.get(
        #     url,
        #     headers={
        #         'User-Agent': random.choice(my_headers)},
        #     proxies=pro)
       # pageCode = chardet.detect(response.content)
        # print(pageCode)
        broswer.get(url)
        #time.sleep(10)
        #broswer.get(url)
        key = wait.until(
            EC.presence_of_element_located(By.CSS_SELECTOR,'#cate_6 > tr:nth-child(5) > 、th:nth-child(2) > h2 > a')
        )

        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
    #    print(response.text)
        element = soup.select(' .tr3')
      #  print(element)
       # print(type(element))
        # response.close()
        # print(element[1])
        for ele in element[-3:-2]:
            yield ele.select('th h2 a')[0].attrs['href']
    #   response.close()
    except TimeoutException as e:
        print('请求出错', e)
    #  findPage(url)

# 获取每个类型具体信息列表


def findPageDetial(url):
    response = requests.get(url, {'http': random.choice(proxies)})
    pageCode = chardet.detect(response.content)
   # print(pageCode)
    response.encoding = pageCode['encoding']

    soup = BeautifulSoup(response.text, 'lxml')
    pool = Pool()
    args = []
    partial_get = partial(getContentPage, suburl=url)
    for element in soup.select('.tr3')[9:]:
        args.append((element.select_one('h3 a').attrs['href']))
    print(args)
    pool.map(partial_get, args)


def getContentPage(posturl, suburl):
    print('get content page is running')
    if suburl.find(r'://') > 0:
        url = suburl
    elif suburl.find('//') == 0:
        url = 'https:' + suburl
    else:
        url = posturl[0:posturl.rfind('/') + 1] + suburl
    # print(url)
    getPicturePage(url)


def getPicturePage(url):
    response = requests.get(url)
    pageCode = chardet.detect(response.content)
    response.encoding = pageCode['encoding']
    soup = BeautifulSoup(response.text, 'lxml')
    temp = soup.select_one('#main .do_not_catch td h4')
    if temp is None:
        print('this is empty')
        return
    temp = temp.parent.select_one('.tpc_content')
    title = temp.parent.select_one('h4').text
    path = os.path.join(os.getcwd(), title)
    if os.path.exists(path) != True:
        os.mkdir(path)
    db['達蓋爾的旗幟'].insert_one({'title': title,
                             'path': path
                             })

    for ele in temp.select('input'):
        downloadPicture(ele.attrs['data-src'], path)
        # print(ele.attrs['data-src'])
    # print(temp.select_one('.f16').text)


def downloadPicture(url, path):
    content = requests.get(url).content
    md = md5(content).hexdigest()
    file = r'{}\{}.jpg'.format(path, md)
    print('正在下载图片')
    with open(file, 'wb') as f:
        f.write(content)
        f.close()


def main():
    url = 'https://www.jd.com'
#    url ='https://www.whatismyip.com/'
#    url = 'https://www.baidu.com/?' + urlencode({'wd':'IP'})
#    url = 'https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0xaae71b2f00053236&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=3&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&prefixsug=ip&rsp=1&inputT=1170&rsv_sug4=2881'
#    print(url)
    for suburl in findPage(url):
        surl = url[:url.rfind('/') + 1] + suburl
        print(surl)
        findPageDetial(surl)
    client.close()


if __name__ == '__main__':
    print('开始爬取')
    main()
