#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import json
import SpiderSettings



r = requests.get('http://music.163.com/discover/playlist/?order=hot&cat=华语&limit=35&offset=0')
print r.cookies

# soup = BeautifulSoup(r.content, "html.parser")
# for t in  soup.find_all(href=re.compile("playlist\?id=")):
#     r =  re.findall(r'[0-9]\d*',t.attrs["href"])
#     print r
#     if len(r) > 0:
#         print r[0]




r = requests.get('http://music.163.com/playlist?id=2016578967', headers = SpiderSettings.headers)
#print r.text

soup = BeautifulSoup(r.content, "html.parser")
#print soup
for t in  soup.find_all(href=re.compile("/song\?id=[0-9]\d*")):

    l = []
    r =  re.findall(r'[0-9]\d*',t.attrs["href"])
    l.append(r)
    l.append(t.text)
    print json.dumps(l, encoding="UTF-8", ensure_ascii=False)




