import emoji
import os
import telebot

if 'TOKEN' not in os.environ:
    print("missing TOKEN.Leaving...")
    os._exit(1)
token = os.environ.get('TOKEN')

bot = telebot.TeleBot(token)
bot.skip_pending = True
botname = "@%s" % bot.get_me().username


@bot.message_handler(commands=["start", "start%s" % botname])
def start(message):
    startmessage = ''' *Welcome to the conchi bot*

This bot is designed to ease interaction with your chats

'''
    bot.reply_to(message, startmessage, parse_mode='Markdown')


@bot.message_handler(commands=["help", "help%s" % botname])
def help(message):
    helpmessage = '''Those are the commands available:
/help this help
'''
    bot.reply_to(message, helpmessage)


@bot.message_handler(func=lambda m: True)
@bot.message_handler(content_types=['sticker'])
@bot.message_handler(content_types=['document'])
@bot.message_handler(content_types=['audio'])
@bot.message_handler(content_types=['photo'])
@bot.message_handler(content_types=['voice'])
def custom(message):
    try:
        if message.reply_to_message is not None and message.reply_to_message.text is not None:
            print("Sending a smiley for %s" % message.chat.title)
            bot.reply_to(message, 'Troll level set for your group')
            if message.document is not None or message.photo is not None or message.audio is not None\
                    or message.voice is not None:
                bot.reply_to(message, ':)')
        else:
            print("Handling the message")
            bot.reply_to(message, '%s' % emoji.emojize(':thumbs_up:'))
            return
    except Exception as e:
        print(e)


print("Ready for answering for you!")
bot.polling()
