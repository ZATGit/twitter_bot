# Newsy Bot

A Python project that scrapes approved websites for news article content and posts the article and a subsection of its contents to Twitter on a configurable timer. This bot was made using Twitter APIs and the following additional libraries: nltk, twitter, requests and lxml.

## Demo

![twitterBot_npr_snakeStory](https://user-images.githubusercontent.com/46094169/57589236-55fa8d00-74ef-11e9-8893-8260af2d59f0.PNG)

### This program finds the news story URLs from the site's homepage and stores them in a list

![twitterBot_linkList](https://user-images.githubusercontent.com/46094169/57589671-bb507d00-74f3-11e9-8b0a-2def6b2f0305.PNG)

### Then extracts the story's paragraphs and extracts sentences of a specified length from those stories

![twitterBot_sentenceList](https://user-images.githubusercontent.com/46094169/57589682-ec30b200-74f3-11e9-9aec-a8f1d3838a43.PNG)

### After randomizing the paragraphs and sentences, it posts the chosen sentence and corresponding story URL to my Twitter account

## Prerequisites

You will need to install the following software/modules:

pip

Python 2 or Python 3

time & random (standard Python library)

lxml.html

nltk

requests

twitter

## Installing

Make sure you have pip installed on your local machine. Python 3 ships with pip, check if you have pip installed using python -m pip --version on the CLI. Otherwise, to install pip, see the documentation.

python -m pip install -e https://github.com/ZATGit/twitter_bot.git

or

cd path/to/chosen/folder git clone https://github.com/ZATGit/twitter_bot.git

Don't forget to activate your virtual environment if you use one!

## Deployment

cd path/to/chosen/folder/twitter/twitter_bot python twitter_bot

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Author

Zach Trembly
