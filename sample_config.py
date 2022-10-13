HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]


# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "5683784122:AAGRjeCs13st5HPH7eHgEK9tmh1bK06hWhg"

