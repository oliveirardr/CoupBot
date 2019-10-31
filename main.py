from telegram.ext import Updater, CommandHandler 

import requests
import re
import os 

def com():
    

def main():
    
    bot_key = open("bot_key.txt","r+") 
    updater = Updater(bot_key.read())
   

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('xxxxx', com))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()