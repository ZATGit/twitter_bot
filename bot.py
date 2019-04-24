import time
import random

import nltk
from lxml.html import fromstring
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