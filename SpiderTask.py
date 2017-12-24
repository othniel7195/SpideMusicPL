#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from SpiderNTESMusicHotChinaPlayList import SpiderPlayList
from SpiderNTESSongs import SpiderSong
from SpiderComments import SpiderComment
from multiprocessing import Process, Lock, Pool

playLists = SpiderPlayList()
#play_page_ids = playLists.getThreePlayListIds()

idx = 0
stop = False
pool = Pool(processes=3)

songs_list = []
cot_key = "comment"
kword_key = "keyword"
song_name_key = "song_name"

def getSpiderSongIds(page):
    for play_id in page:
        songLists = SpiderSong(str(play_id))
        song_ids = songLists.getAllSongIdAndName()  #type: dict

        for key, value in song_ids.items():
            commentList = SpiderComment(value)
            comments = commentList.getSongCommentTotal()
            keyword = commentList.getSongSingerName()
            temp_dict = {}
            temp_dict[cot_key] = comments
            temp_dict[song_name_key] = key.encode("utf-8") #type: str
            temp_dict[kword_key] = keyword
            print temp_dict
            songs_list.append(temp_dict)


while(not stop):
    ptupe = playLists.getEveryPlayListIds(idx)

    if ptupe[0]:
        print ptupe[0]
        pool.apply_async(getSpiderSongIds(ptupe[0]))
        idx = int(ptupe[1])
    else:
        stop = True

sort_song_list = sorted(songs_list, key=lambda cx: int(cx[cot_key]))

print sort_song_list










