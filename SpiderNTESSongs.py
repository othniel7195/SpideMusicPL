#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import requests
import SpiderSettings
from bs4 import BeautifulSoup
import re
import json

class SpiderSong:

    __play_list_id = None

    def __init__(self, list_id):
        self.__play_list_id = list_id


    def list_url(self, slistId):
        sListUrl = "http://music.163.com/playlist?id={0}".format(slistId)
        return sListUrl

    def getAllSongIdAndName(self):
        response = requests.get(self.list_url(self.__play_list_id), headers=SpiderSettings.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        songs = {}
        for song in soup.find_all(href=re.compile("/song\?id=[0-9]\d*")):
            sattrs = re.findall(r'[0-9]\d*', song.attrs["href"])
            songs[song.text] = sattrs[0]

        return songs







if __name__ == '__main__':
    s = SpiderSong("2016578967")
    print json.dumps(s.getAllSongIdAndName(), encoding="UTF-8", ensure_ascii=False)
