from ytcc.download import Download
from ytcl.sel_crawl import video_crawl
downld=Download()
crawl=video_crawl()
dict_id=crawl.get_id('https://www.youtube.com/user/TEDtalksDirector/videos')


captions=downld.get_captions()
print(captions)
print(type(captions))

text_file = open("%s.txt"%id, "w")
text_file.write(captions)
text_file.close()