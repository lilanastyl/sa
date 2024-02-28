import telebot
from telebot import types
import random
import string
import bunker
import group
import person
import story
import messages
bot = telebot.TeleBot('6885805301:AAGcnYkpGfciC65TDPodn6k2nyRLS3NQKlY')
connect = False

markup_start = types.InlineKeyboardMarkup()
markup_start.add(types.InlineKeyboardButton('Создать игру', callback_data='create_group'), types.InlineKeyboardButton('Присоеденится', callback_data='join_group'))

@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
    bot.send_message(message.chat.id, messages.start, reply_markup=markup_start)
    
@bot.message_handler(commands=['rules'])
def start_message(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🔙Назад',callback_data='but_rules'))
    bot.send_message(message.chat.id, messages.rules,reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)

def callback_handler(call: types.CallbackQuery):
    if call.data == 'but_rules':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=messages.start, reply_markup=markup_start )
    if call.data == 'create_group':
        new_group = group.Group("MyGameGroup")
        group.groups[new_group.code] = new_group
        bot.send_message(call.message.chat.id, f"Группа \"{new_group.name}\" создана. Код группы: {new_group.code}")
    if call.data == 'join_group':
        connect = True
        bot.send_message(call.message.chat.id, "Введите код для присоединения к группе.")
   

    

@bot.message_handler(content_types=['text'])
def connect_handler(message: types.Message):
    if connect:
        


     
    # add_btn = types.KeyboardButton('✏Відгуки')
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    


    
    #story_btn = types.KeyboardButton('📚Історія')
    #person_btn = types.KeyboardButton('👨Персона👩')
    #bunker_btn = types.KeyboardButton('☠Бункер')
    

    

    

    #bot.send_message(mess.chat.id, messages.start)
    #bot.send_message(mess.chat.id, 'Оберіть дію', reply_markup=markup)




    #if message.text == '📚Історія':
    #     st = story.story()
    #     bot.send_message(message.chat.id, st.getStory())

    # elif message.text == '👨Персона👩':
    #     prs = person.person()
    #     prs.setPerson()
        # bot.send_message(message.chat.id, prs.getPerson())

    

    # elif message.text == '☠Бункер':
    #     bn = bunker.bunker()
    #     #bn.setBunker()
    #     bot.send_message(message.chat.id, bn.getBunker())

    # elif message.text == '🔙Назад':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #     story_btn = types.KeyboardButton('📚Історія')
    #     person_btn = types.KeyboardButton('👨Персона👩')
    #     bunker_btn = types.KeyboardButton('☠Бункер')
    #     rules_btn = types.KeyboardButton('📝Правила')
    #     add_btn = types.KeyboardButton('✏Відгуки')

    #     markup.add(person_btn, bunker_btn, story_btn, rules_btn, add_btn)

    #     bot.send_message(message.chat.id, 'Оберіть дію', reply_markup=markup)





bot.polling(none_stop=True)
