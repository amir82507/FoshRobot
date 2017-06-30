#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import telebot
    import os
    import sys
    import random
except ImportError :
    print "[-] You need to install Modules \n\nsudo pip install pytelegrambotapi"
    exit()
reload(sys)
sys.setdefaultencoding("utf-8")
TOKEN = '<<<< 372473342:AAHpNK7SceyufnI8CfTKMO4lLEAPRWFpdgI >>>>>'
bot = telebot.TeleBot(TOKEN)

def banner():
    print """

  L         iX        7R  LM7RiXLM7R XLM7RiXL   i LM      7R
  7         LM        iX          iX M       R     Ri    Ri
  i         7Ri      XLM         XL  R       X  7   LM  iX
  L         i LM    LM R        LM   X       M  i     iXL
  7         L  Ri  M7  X       M7    M7RiXLM7   L    XLM7
  i         7   L  Ri  M       R     R XLM      7   LM  iX
  L         i   7RiX   R      iX     X   RiX    i  M7    M7
   RiXLM7R  L    XL    X     XL      M     M7R  L 7R      iX

"""

def clearing():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

banner(),clearing()

f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n \033[01;34m Bot Username: {} \033[0m".format(bot.get_me().username)
i = "\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n \033[01;31m Bot Is Online Now! \033[0m"
print(f + u + i + c)

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'voice', 'location'])
def us(m):
    file = open("koskesh.db","r")
    file = file.read()
    new = file.split(",")
    bot.send_message(m.chat.id, random.choice(new))


bot.polling(True)
