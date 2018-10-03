from bs4 import BeautifulSoup
import lxml
import requests

class video_crawl():
    def __init__(self):
        self.vid_id = []
    def get_video_id(self, target_url):
        response = requests.get(target_url)
        soup = BeautifulSoup(response.text, "lxml")
        lis = soup.find_all('li', {'class': 'channels-content-item yt-shelf-grid-item'})

        for li in lis:
            # <a class="yt-uix-sessionlink yt-uix-tile-link  spf-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="Eminem - Phenomenal (Behind The Scenes)" href="/watch?v=NEGjmd_RzLU">Eminem - Phenomenal (Behind The Scenes)</a>
            title = li.find('a', {'title': True})['title']
            video_link = li.find('a', {'href': True})['href'].split("=")[1]
            img_link = li.find('img', {'src': True})['src']
            # <span class="video-time" aria-hidden="true"><span aria-label="8분, 55초">8:55</span></span>
            play_time = li.find('span', {'class': 'video-time'}).text
            # <ul class="yt-lockup-meta-info"><li>조회수 2,902,617회</li><li>6개월 전</li></ul>
            # hits_and_updated_time = li.find('ul', {'class' : 'yt-lockup-meta-info'})
            hits = li.find_all('li')[2].text
            updated_time = li.find_all('li')[3].text
            self.vid_id.append(video_link)
        return self.vid_id


