import time
import random

from lxml.html import fromstring
import nltk
#dl dataset for parse paragraphs & tokenize
nltk.download('punkt')
import requests
from twitter import OAuth, Twitter

import credentials

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

oauth = OAuth(
    credentials.ACCESS_TOKEN,
    credentials.ACCESS_SECRET,
    credentials.CONSUMER_KEY,
    credentials.CONSUMER_SECRET
)
t = Twitter(auth=oauth)



def npr_scrape():
    #recognized as real client
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
            'AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'
        }
    #fetch & save page info to r
    r = requests.get('https://npr.org', headers=HEADERS)
    #r.content 'inspect element' source html, pass to fromstring (lxml library)
    tree = fromstring(r.content)
    links = tree.xpath('//section[@class="featured-group"]//div[@class="story-text"]/a/@href')
    print(links)

    #fetch article
    for link in links:
        r = requests.get(link, headers=HEADERS)
        page_tree = fromstring(r.content)



npr_scrape()