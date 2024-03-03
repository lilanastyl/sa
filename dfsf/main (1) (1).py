import telebot
from telebot import types
from telebot.async_telebot import AsyncTeleBot
import random
import string
import bunker
import group
import person
import story
import messages
import asyncio
bot = AsyncTeleBot('6885805301:AAGcnYkpGfciC65TDPodn6k2nyRLS3NQKlY')
connect = False

markup_start = types.InlineKeyboardMarkup()
markup_start.add(types.InlineKeyboardButton('Создать игру', callback_data='create_group'), types.InlineKeyboardButton('Присоеденится', callback_data='join_group'))

@bot.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, messages.start, reply_markup=markup_start)
    
@bot.message_handler(commands=['rules'])
async def start_message(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🔙Назад',callback_data='but_rules'))
    await bot.send_message(message.chat.id, messages.rules,reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
async def callback_handler(call: types.CallbackQuery):
    global connect  
    if call.data == 'but_rules':
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=messages.start, reply_markup=markup_start)
    if call.data == 'create_group':
        new_group = group.Group("MyGameGroup")
        group.groups[new_group.code] = new_group
        await bot.send_message(call.message.chat.id, f"Группа \"{new_group.name}\" создана. Код группы: {new_group.code}")
    if call.data == 'join_group':
        connect = True
        await bot.send_message(call.message.chat.id, "Введите код для присоединения к группе.")

async def connect_handler(message: types.Message):
    global connect
    group_code = message.text
    if group_code in group.groups:
        group_instance: group.Group = group.groups[group_code]
        group_instance.players_connect(group_code, message)
        await bot.send_message(message.chat.id, f"Вы успешно присоединились к группе \"{group_instance.name}\".")
    else:
        await bot.send_message(message.chat.id, "Неверный код группы.")
    connect = False
    

@bot.message_handler(content_types=['text'])
async def messages_sendler(message: types.Message):
    if connect == True:
        await connect_handler(message)
        # message.new_chat_member
        
        


     
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





asyncio.run(bot.polling(none_stop=True))
