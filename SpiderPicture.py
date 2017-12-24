#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import json
import SpiderSettings



# r = requests.get('http://music.163.com/discover/playlist/?order=hot&cat=华语&limit=35&offset=0')
# print r.cookies

# soup = BeautifulSoup(r.content, "html.parser")
# for t in  soup.find_all(href=re.compile("playlist\?id=")):
#     r =  re.findall(r'[0-9]\d*',t.attrs["href"])
#     print r
#     if len(r) > 0:
#         print r[0]




# r = requests.post('http://music.163.com/weapi/v1/resource/comments/R_SO_4_330508',headers= SpiderSettings.headers, params=SpiderSettings.params)
# print json.loads(r.text)[u"total"]
#
# soup = BeautifulSoup(r.content, "html.parser")
# print soup
# for t in  soup.find_all(href=re.compile("/song\?id=[0-9]\d*")):
#
#     l = []
#     r =  re.findall(r'[0-9]\d*',t.attrs["href"])
#     l.append(r)
#     l.append(t.text)
#     print json.dumps(l, encoding="UTF-8", ensure_ascii=False)
#
# url='http://music.163.com/weapi/v1/resource/comments/R_SO_4_465920636?csrf_token=c0f6bfdcd0526ec0ba6c207051a08960'
#
# param={'params':'wxLqdGgw16OHb6UwY/sW16VtLqAhGaDMeI2F4DaESDplHA+CPsscI4mgiKoVCPuWW8lcd9eY0YWR/iai0sJqs0NmtLubVCkGdpN\
# TN3mLhevZpdZy/XM1+z7L18InFz5HbbRkq230i0aOco/3jVsMWcD3/tzzOCLkGuu5xdbo99aUjDxHwDSVfu4pz4spV2KonJ47Rt6vJhOorV7LfpIVmP/qe\
# ZghfaXXuKO2chlqU54=',\
# 'encSecKey':'12d3a1e221cd845231abdc0c29040e9c74a47ee32eb332a1850b6e19ff1f30218eb9e2d6d9a72bd797f75\
# fa115b769ad580fc51128cc9993e51276043ccbd9ca4e1f589a2ec479ab0323c973e7f7b1fe1a7cd0a02ababe2adecadd4ac93d09744be0deafd1eef\
# 0cfbc79903216b1b71a82f9698eea0f0dc594f1269b419393c0'}#这里每行末尾的‘\’是代码过长用来换行的，慎用，换行多了易出现bug。

# r = requests.get("http://music.163.com/song?id=330508")
# soup = BeautifulSoup(r.content,"html.parser")
# #print soup
# l = soup.find_all("meta")
# print l
# for i1 in l:
#    # print i1.attrs.get(u"name") #type:dict
#     if i1.attrs.get(u"name") == "keywords":
#         print i1.attrs.get(u"content")


from multiprocessing import Pool
import time


def fuc(i):
    print i
    time.sleep(1)


pool = Pool(processes=4)

for i in xrange(100):
    pool.apply_async(func=fuc,args=(i,))
pool.close()
pool.join()

