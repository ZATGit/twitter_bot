# Twitter News Bot

A bot to scrape and post news content. 

## Screenshot of the Bot in Action

![twitterBot_npr_snakeStory](https://user-images.githubusercontent.com/46094169/57589236-55fa8d00-74ef-11e9-8893-8260af2d59f0.PNG)

### It finds the news story links and stores them in a list

![twitterBot_linkList](https://user-images.githubusercontent.com/46094169/57589671-bb507d00-74f3-11e9-8b0a-2def6b2f0305.PNG)

### Then extracts the story's paragraphs and extracts sentences of a specified length from them

![twitterBot_sentenceList](https://user-images.githubusercontent.com/46094169/57589682-ec30b200-74f3-11e9-9aec-a8f1d3838a43.PNG)

### After randomizing the paragraphs and sentences, it posts the chosen sentence and corresponding story link to Twitter

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
