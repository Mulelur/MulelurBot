#!/usr/bin/env python
import os

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.bot import Bot
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from dadjokes import Dadjoke


is_config = os.path.exists("config.py")

if is_config:
    from config import *
else:
    from sample_config import *


updater = Updater(bot_token,
				use_context=True)


async def  start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello, Welcome to the MulelurBot. Please write\
		/Hello get a dad joke")
    

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
    /Hello - bot then replies with a dad joke
	""")

def chat(update: Update, context: CallbackContext):
    if (update.message.text == 'Hello' or update.message.text == "hello"):
        dadjoke = Dadjoke()

        update.message.reply_text(
	    dadjoke.joke
        )
    else:  
        update.message.reply_text(
        "Sorry '%s' please type hello" % update.message.text
        )

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands


# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))


updater.start_polling()

print(
    """
    MuleluR Bot Started! 

    """)

