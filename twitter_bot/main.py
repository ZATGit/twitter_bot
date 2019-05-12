import time
import random
from lxml.html import fromstring
import nltk
#dl dataset for parse paragraphs & tokenize
nltk.download('punkt')
import requests
from twitter import OAuth, Twitter

import credentials

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

def npr_scrape():
    """Scrape articles from npr.org"""

    #fetch & save page info to r
    url = 'https://npr.org'
    r = requests.get(url, headers=HEADERS)
    #r.content 'inspect element' source html, pass to fromstring (lxml library)
    tree = fromstring(r.content)
    links = tree.xpath('//section[@class="featured-group"]//div[@class="story-text"]/a/@href')
    print(links)

    #fetch paragraphs and extract text
    for link in links:
        r = requests.get(link, headers=HEADERS)
        page_tree = fromstring(r.content)
        paragraphs = page_tree.xpath('//div[@id="storytext"]/p')
        paragraph = extract_text_paragraph(paragraphs)
        text = extract_sentence(paragraph)

        if not text:
            continue

        #yield instead of return to avoid always getting first article in list and fewer requests
        yield '"%s" %s' % (text, link)

def extract_text_paragraph(paragraphs):
    """Extracts text from paragraph elements and returns random tokenized paragraph."""

    paragraphs = [paragraph.text_content() for paragraph in paragraphs if paragraph.text_content()]
    paragraph = random.choice(paragraphs)
    print(paragraphs)
    return tokenizer.tokenize(paragraph)

def extract_sentence(paragraph):
    """Returns random text if correct length from a paragraph."""

    # sort text from random paragraph.
    for _ in range(10):
        text = random.choice(paragraph)
        if text and 180 < len(text) < 280:
            return text

    #skip to next article if no matching sentence in 10 attempts.
    return None

def main():
  """Main actions of the Twitter bot."""

  print('----Good morning, Dave. I am a TWIT 9000 bot----')
  #Scraper functions list (add more sites when those modules are complete)
  #Remove if decide to modularize again.
  news_functions = ['npr_scrape']
  #Likely change to news_'iterators = [bot_npr.npr_scrape]' if modularize again.
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
              #sleep for half a day (in seconds)
              time.sleep(43200)
          except StopIteration:
              news_iterators[i] = globals()[news_functions[i]]()

if __name__ == "__main__":
    main()