import time
from ytcc.download import Download
from ytcl.sel_crawl import video_crawl
from textstat.textstat import textstatistics
downld=Download()
txs=textstatistics()
a=downld.get_captions("Y56lpXvXbs0")
print(txs.dale_chall_readability_score(a))