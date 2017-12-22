#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
爬网易云音乐的华语类热门所有歌单
"""

import requests
from bs4 import BeautifulSoup
import re



class SpiderPlayList:

    __play_list_url = None


    def __init__(self):
        self.__play_list_url = "http://music.163.com/discover/playlist/"

    def spider_pagenumber(self, pageno):
        params = {}
        params["order"] = "hot"
        params["cat"] = "华语"
        params["limit"] = "35"
        params["offset"] = str(pageno)
        #print params
        response = requests.get(self.__play_list_url, params = params)
        return response

    def parse_html(self, response):
        """
        
        :type response: `requests.Response`
        :rtype: list
        """
        hrefs = []
        soup = BeautifulSoup(response.content, "html.parser")
        play_ids = soup.find_all(href=re.compile("playlist\?id="))
        for play_id in play_ids:
            r = re.findall(r'[0-9]\d*', play_id.attrs["href"])
            if len(r) > 0:
                hrefs.append(r[0])
        return hrefs


    def getAllPlayListIds(self):

        stop = True
        index = 0
        hrefs = []
        while(stop):
            rsponse = self.spider_pagenumber(index)
            ehrefs = self.parse_html(rsponse)
            #print ehrefs
            if len(ehrefs) == 0:
                stop = False
            else:
                index = index + 1
                hrefs.append(ehrefs)

        return hrefs

    def getThreePlayListIds(self):

        stop = True
        index = 0
        hrefs = []
        while (index < 3):
            rsponse = self.spider_pagenumber(index)
            ehrefs = self.parse_html(rsponse)
            # print ehrefs
            if len(ehrefs) == 0:
                stop = False
            else:
                index = index + 1
                hrefs.append(ehrefs)

        return hrefs


if __name__ == '__main__':
    s = SpiderPlayList()
    print s.getThreePlayListIds()





