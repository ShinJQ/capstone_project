import time
from ytcc.download import Download
from ytcl.sel_crawl import video_crawl
downld=Download()
crawl=video_crawl()
dict_id=crawl.get_id('https://www.youtube.com/user/TEDtalksDirector/videos')
import os
os.chdir('/home/kyoo/capstone_project/youtube/sub_data')
rmlst =[]
for i in dict_id.keys():
    name=i.replace("/", "")
    vid_id=dict_id[i].split("=")[1]
    try:
        captions=downld.get_captions(vid_id)
    except:
        rmlst.append(i)
    time.sleep(0.1)
    text_file = open("%s.txt" %name, "w")
    text_file.write(captions)
    text_file.close()
    time.sleep(0.1)

import glob
os.chdir('/home/kyoo/capstone_project/youtube/sub_data')
for files in glob.glob("*.vtt"):
    os.remove(files)

for i in rmlst:
    del dict_id[i]


print(len(dict_id.keys()))