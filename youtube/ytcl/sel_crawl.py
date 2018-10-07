from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup
import time
import lxml
import requests
class video_crawl():
    def __init__(self):
        self.vid = {}
        self.driver = webdriver.Chrome('/home/kyoo/capstone_project/youtube/ytcl/chromedriver')

    def get_id(self, target_url):
        self.driver.get(target_url)
        search_more = 0
        for i in range(1, 2):
            self.driver.find_element_by_tag_name("body").send_keys(Keys.END)
            try:
                self.driver.find_element_by_xpath('//*[@class="active  style-scope paper-spinner"]')
                time.sleep(0.3)
            except:
                None
        id = self.driver.find_elements_by_xpath('//*[@id="video-title"]')
        for i in id:
            self.vid[((i.text))]=i.get_property('href')

        self.driver.close()
        return self.vid
