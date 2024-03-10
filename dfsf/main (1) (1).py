import telebot
from telebot import types
from telebot.async_telebot import AsyncTeleBot
import random
import string
import bunker
import group
import person
from telebot import TeleBot
from telebot.apihelper import ApiException
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
    
@bot.callback_query_handler(func=lambda call: call.data == 'create_group')
async def create_group_callback(call):
    join_markup = types.InlineKeyboardMarkup()
    join_markup.add(types.InlineKeyboardButton('Присоеденится', callback_data='join_group'))
    await bot.send_message(call.message.chat.id, f"Группа создана, если хотите присоединиться, @{call.message.from_user.username}, нажмите кнопку снизу", reply_markup=join_markup)

@bot.callback_query_handler(func=lambda call: call.data == 'join_group')
async def join_group_callback(call):
    group.add_user(call.message.chat.id, call.from_user.username)
    users = group.get_users(call.message.chat.id)
    users_text = "\n".join(f"@{user}" for user in users)
    await bot.edit_message_text(
        f"Группа создана, присоединился @{call.from_user.username}\n\nУчастники:\n{users_text}",
        call.message.chat.id,
        call.message.message_id
    )

async def main():
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())




# @bot.callback_query_handler(func=lambda call: True)
# async def callback_handler(call: types.CallbackQuery):
#     global connect  
#     if call.data == 'but_rules':
#         await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=messages.start, reply_markup=markup_start)
#     if call.data == 'create_group':
#         new_group = group.Group("MyGameGroup")
#         group.groups[new_group.code] = new_group
#         await bot.send_message(call.message.chat.id, f"Группа \"{new_group.name}\" создана. Код группы: {new_group.code}")
#     if call.data == 'join_group':
#         connect = True
#         await bot.send_message(call.message.chat.id, "Введите код для присоединения к группе.")

# async def connect_handler(message: types.Message):
#     global connect
#     group_code = message.text
#     if group_code in group.groups:
#         group_instance: group.Group = group.groups[group_code]
#         group_instance.players_connect(group_code, message)
#         await bot.send_message(message.chat.id, f"Вы успешно присоединились к группе \"{group_instance.name}\".")
#     else:
#         await bot.send_message(message.chat.id, "Неверный код группы.")
#     connect = False
    





asyncio.run(bot.polling(none_stop=True))
