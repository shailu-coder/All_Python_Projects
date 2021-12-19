# pip install requests
# pip install bs4
# pip install plyer

#Have Doubt?? Ask Us Insta:- www.instagram.com/python_coderz_

# Python program to illustrate
# desktop news notifier
from bs4 import BeautifulSoup
from plyer import notification
import requests
import time
# rss feed url
url = 'https://news.google.com/news/rss'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'xml')
# find data items
news_list = soup.find_all('item')
# list first 5 news data
news_list = news_list[0:5]
# iterate through news list
for news in news_list:
    # notifier to display News
    notification.notify(title='News Update',
                        message=news.title.text,
                        timeout=20)
    # display new update after
    # every 20 seconds
    time.sleep(20)