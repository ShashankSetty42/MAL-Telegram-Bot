from bot import telegram_chatbot
import mal_scraper

bot = telegram_chatbot("config.cfg")

#get anime name and return info string
def make_reply(msg):
    reply = None
    if msg is not None:
        reply = format_reply(mal_scraper.scrape_page(msg))
    return reply

#convert the dictonary value returned from scraping MAL
def format_reply(msg):
    return_string = ""
    for item in msg:
        return_string += item + " : " + msg[item] + "\n"
    return return_string

#set initialize updateID
update_id = None

#keep the server running
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]	#get userID to reply back
            reply = make_reply(message) 			#set reply to a string from 
            bot.send_message(reply, from_)			#send message reply to bot.py
