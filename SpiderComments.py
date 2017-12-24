#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import SpiderSettings
import json
from bs4 import BeautifulSoup

class SpiderComment:

    __song_id = None
    __url_comment = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{0}"
    __url_singer = "http://music.163.com/song?id={0}"

    def __init__(self, songId):
        self.__song_id = songId

    def getSongCommentUrl(self):

        url = self.__url_comment.format(self.__song_id)
        return url

    def getSongSingerUrl(self):
        url = self.__url_singer.format(self.__song_id)
        return url

    def getSongCommentTotal(self):

        response = requests.post(self.getSongCommentUrl(),headers=SpiderSettings.headers,params=SpiderSettings.params)
        #print response.text

        return json.loads(response.text).get(u'total')

    def getSongSingerName(self):
        response = requests.get(self.getSongSingerUrl())
        #print response.url
        soup = BeautifulSoup(response.content, "html.parser")
        #print soup
        metas = soup.find_all("meta")
        for meta in metas:
            if meta.attrs.get(u"name") == "keywords":
                return meta.attrs.get(u"content")




if __name__ == '__main__':

    sc = SpiderComment("330508")
    dis = sc.getSongSingerName()
    total = sc.getSongCommentTotal()
    print total, dis
