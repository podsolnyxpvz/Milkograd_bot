import telebot
import random
from telebot import types
import os

bot = telebot.TeleBot('5514650900:AAHZghYZTVBQV4D2PUEIUxXc8-KVeghQ8Jg')
          
@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Открыть🃏")
        item2=types.KeyboardButton("Карты и их редкость🗂️")
        item3=types.KeyboardButton("Милкоград🍼")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Привет! Что бы начать открытие, нажимай на кнопки снизу👋',  reply_markup=markup)
        
@bot.message_handler(content_types=['text'])
def photo(message):
  if message.text == 'Открыть🃏':
  	photo = open('Cards/' + random.choice(os.listdir('Cards')), 'rb')
  	bot.send_photo(message.chat.id, photo, reply_to_message_id=message.message_id)
  if message.text == 'Карты и их редкость🗂️':
  	bot.reply_to(message, '''КАРТЫ И ИХ РЕДКОСТЬ:\n\n@Dramoed-редкий
@windings - эпический🟣
@zzu_61 - обычный🔵
@shirona_shirona - редкий🟢
@OKUASU_ABCHIHBA - обычный🔵
@Blevota_kozla - обычный🔵
@Western_shock - редкий🟢
@tetris_ines - эпический🟣
@bibizyanya - эпический🟣
@Nenabobibi - обычный🔵
@BLET_SUPE - редкий🟢
@Crade9801 - легендарный🟡
@Krutoibober95 - легендарный🟡
@gera_oF - эпический🟣
@shirona_shir0na - редкий🟢
@myBroyyyyy - редкий🟢
@SkocthFactit_ines - легендарный🟡
@tetbanjojosnus - эпический🟣
@blag0o - легендарный🟡
@xsv19 - легендарный🟡
@MechusYt - эпический🟣
@gegestudio - легендарный🟡
@shheeedo - редкий🟢
@xawar228 - обычный🔵
@oko_ines - эпический🟣
@JoRriK7 - редкий🟢
@mashaluy - эпический🟣
@legenda_pes - эпический🟣
@Epplot - редкий🟢
@ijustwntualltoshtup - обычный🔵
@Izolenta_Kypera - редкий🟢
@xx_loshad_xx - редкий🟢
@elfrvioF - эпический🟣
@Kilkaaa662 - обычный🔵
@garry_boy21 - обычный🔵
@qwin0ki_oF - редкий🟢
@agentmoloko - IMPOSSIBLE☠️🍀
@cakaoF - IMPOSSIBLE☠️🍀''')
  if message.text == 'Милкоград🍼':
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Милкоград", url='https://t.me/+Zn2mJhxQkjM2NmYy')
    markup.add(button1)
    bot.send_message(message.chat.id, "Лучший чат в Млечном Пути".format(message.from_user), reply_markup=markup)
    
    
bot.infinity_polling(none_stop=True)