#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re

headers = {
    "Accept":"" "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
    "Connection":"keep-alive",
    "Cookie":"_iuqxldmzr_=32; _ntes_nnid=65e2c886678f983cb0d122cd4f9e2a31,1513921181685; _ntes_nuid=65e2c886678f983cb0d122cd4f9e2a31; __utmc=94650624; __utmz=94650624.1513921182.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __remember_me=true; __utma=94650624.588405226.1513921182.1513921182.1513925272.2; MUSIC_U=a2cee674c453b544c30f74a2cae1bde40cd1c121f26d3274b15999eb4c643fc1332c50d996289d566b0e6c7e1a97adb96c7afb743e45811a; __csrf=409ba73c62f3951c15c4348e65df9d13; __utmb=94650624.4.10.1513925272; JSESSIONID-WYYY=%2Bk1NSpuzsAT0zcH80%2B5nQJhxRI4XapNhHxc0ZryKy4SHkth2owuRXRbxBsZj2wa1RfCbCD4rlatKbXzf%2BhWs2frT%2FmJ8cHeJpBa5J6W%2FhVYHemkwrWvtUWREufzaGBe5d4ZBCdFyHmj5UETQu2qlfoDEsXD2nXAtJka7Rp6YblOAx6AN%3A1513928201531",
    "Host":"music.163.com",
    "Referer":"http://music.163.com/",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

r = requests.get('http://music.163.com/discover/playlist/?order=hot&cat=华语&limit=35&offset=10000', headers = headers)
#print r.text

soup = BeautifulSoup(r.content, "html.parser")
for t in  soup.find_all(href=re.compile("playlist\?id=")):
    r =  re.findall(r'[0-9]\d*',t.attrs["href"])
    print r
    if len(r) > 0:
        print r[0]








