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

from bot_npr import *

#recognized as real client
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                  'AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'
}

def extract_text_paragraph(paragraphs):
    """Extracts text from paragraph elements and returns random tokenized paragraph."""
    paragraphs = [paragraph.text_content() for paragraph in paragraphs if paragraph.text_content()]
    paragraph = random.choice(paragraphs)

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

    npr_scrape()

if __name__ == "__main__":
    main()
