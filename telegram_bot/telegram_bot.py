import sys
import time
import telepot
import random
import aiml

from telepot.loop import MessageLoop
from pprint import pprint
from file_ids import *

kernel = aiml.Kernel()
kernel.learn("basic_chat.aiml")

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if 'photo' in msg.keys():
        print(msg['photo'])
    if 'sticker' in msg.keys():
        print('sticker id: {}'.format(msg['sticker']['file_id']))
        if 'set_name' in msg['sticker'].keys():
            print('set name is {}'.format(msg['sticker']['set_name']))
    else:
        print(msg)

    if content_type == 'text':
        msg_text = msg['text']
        if msg_text.lower() == 'hello there':
            bot.sendPhoto(chat_id, files['kenobi'])
        else:
            msg = kernel.respond(msg_text)
            if len(msg) == 0:
                msg = 'соре, не знаю такого'
            bot.sendMessage(chat_id, msg)
            # rnd_value = random.random() * 100
            # if rnd_value > 70:
            #     print('fresh meat alert')
            #     # bot.sendSticker(chat_id, files['fresh meat'])
            # else:
            #     pass
                # bot.sendMessage(chat_id, msg_text)

TOKEN = "692035517:AAHNDPhxgvKIHHegeW7yPXWAc5EDcz3KKcU"

bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
