# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url='http://rate.bot.com.tw/xrt?Lang=zh-TW'

page=requests.get(url)

bsobj=BeautifulSoup(page.content,'html.parser')

for tr in bsobj.find('table').find('tbody').findAll('tr'):
    
    cell=tr.findAll('td')
    
    currency=cell[0].find('div',{'class':'visible-phone'}).contents[0]
    
    currency=currency.replace('\r','')
    currency=currency.replace('\n','')
    currency=currency.replace(' ','')
    
    curr_rate=cell[2].contents[0]
    
    print(currency,':',curr_rate)