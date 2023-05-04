import os
import telebot
import bs4
import requests
import re
import codecs
from fpdf import FPDF
import shelve
from keep_alive import keep_alive


API_KEY=
bot=telebot.TeleBot(API_KEY)
keep_alive()
@bot.message_handler(commands=['start','hrlp'])
def greet(message):
  # usr_n=up_d.update(message).user
  bot.reply_to(message,"Hi hello namaskara.\nThis bot created by Sharat S Bhat")
  bot.reply_to(message,"Enter car name of your choice")
  
@bot.message_handler(func=lambda message: True)
def get_specs(message):
  word=message.text
  res=requests.get('https://www.google.com/search?q='+word+' specs')
  res.raise_for_status()
  obj1=re.compile(r'\d* [bB]hp')
  obj2=re.compile(r'\d* Nm')
  obj3=re.compile(r'\d* cc')
  mo1=obj1.search(res.text)
  mo2=obj2.search(res.text)
  mo3=obj3.search(res.text)
  try:
    text_reply="Power : "+mo1.group()+"\nTorque : "+mo2.group()+"\nEngine Displacement : "+mo3.group()
    bot.reply_to(message,text_reply)
  except:
    bot.reply_to(message,"Some unknown error, we are working on it")
  


bot.polling()

