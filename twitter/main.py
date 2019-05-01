import time
import random
from lxml.html import fromstring
import nltk
#dl dataset for parse paragraphs & tokenize
nltk.download('punkt')
import requests
from twitter import OAuth, Twitter

import credentials
from bot_npr import *

#recognized as real client
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                  'AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'
}

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

oauth = OAuth(
    credentials.ACCESS_TOKEN,
    credentials.ACCESS_SECRET,
    credentials.CONSUMER_KEY,
    credentials.CONSUMER_SECRET
)

t = Twitter(auth=oauth)


def main():
  """Main actions of the Twitter bot."""

  print('----Good morning, Dave. I am a TWIT 9000 bot----')
  #Scraper functions list
  news_functions = ['npr_scrape', 'bbc_scrape']
  news_iterators = []

  #returns dictionary varNames:variables
  for function in news_functions:
      news_iterators.append(globals()[function]())

  while True:

      for i, iterator in enumerate(news_iterators):
          try:
              tweet = next(iterator)
              t.statuses.update(status=tweet)
              print(tweet, end='\n\n')
              #sleep for 10 minutes
              time.sleep(10)
          except StopIteration:
              news_iterators[i] = globals()[newsfunctions[i]]()

if __name__ == "__main__":
    main()
