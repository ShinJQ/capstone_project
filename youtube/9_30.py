from ytcc.download import Download
from ytcl.crawl import video_crawl
crawl=video_crawl()
aa="https://www.youtube.com/channel/UCy-H-BPCHctNmUb80MeapvQ/videos"
id=crawl.get_video_id(aa)
#captions=downld.get_captions(vid_id)

