# MyAnimeList Telegram Bot

This bot written in python will get the query i.e name of the anime from the user, which then is sent over to the mal scraper script that rips data off myanimelist and sends it over to the bot as reply.

## Files

There are four python files included in this repo:

* mal_scraper.py -> used for scraping info from MAL page of the anime
* config.cfg -> file used to abstract your bot token
* bot.py -> used for connecting to the telegram API
* server.py -> used to communicate with bot.py and handle messages



## Usage

1. Make sure you have all the dependencies ```beautifulsoup4```, ```lxml``` & ```requests```
2. Change the token in ```config.cfg```
3. Run ```server.py```



## Screenshots

<img src="https://i.imgur.com/yFmLadx.png" height="450">  <img src="https://i.imgur.com/r0wtwJ1.png" height="450">  <img src="https://i.imgur.com/9zhOve8.png" height="450">
