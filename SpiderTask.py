#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from SpiderNTESMusicHotChinaPlayList import SpiderPlayList
from SpiderNTESSongs import SpiderSong
from SpiderComments import SpiderComment
from multiprocessing import Pool

playLists = SpiderPlayList()
#play_page_ids = playLists.getThreePlayListIds()
songs_list = []
def MSpiderSongIds(page):
    cot_key = "comment"
    kword_key = "keyword"
    song_name_key = "song_name"
    print page
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
            #print temp_dict
            songs_list.append(temp_dict)


def runpool():
    pool = Pool(processes=4)
    idx = 0
    stop = False
    while(not  stop):
        ptupe = playLists.getEveryPlayListIds(idx)
        if ptupe[0]:
            pool.apply_async(func=MSpiderSongIds, args=(ptupe[0],))
            idx = ptupe[1]
        else:
            stop = True
    return pool

pool = runpool()
pool.close()
pool.join() 
sort_song_list = sorted(songs_list, key=lambda cx: int(cx["comment"]))
print sort_song_list










