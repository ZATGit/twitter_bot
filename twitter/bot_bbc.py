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

def bbc_scrape():
    """Scrape articles from bbc.com"""

    HEADERS = {
    }

    r = requests.get

bbc_scrape()