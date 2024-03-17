from telebot import types
from telebot.async_telebot import AsyncTeleBot
import random
import string
import bunker
from group import Game, games
import person
from telebot.apihelper import ApiException
import story
import messages
import asyncio
import json

bot = AsyncTeleBot('6885805301:AAGcnYkpGfciC65TDPodn6k2nyRLS3NQKlY')
connect = False\

markup_start = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Присоеденится', callback_data='join_group'))
markup_choose = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Смена готовности', callback_data='choose'), types.InlineKeyboardButton('Выйти', callback_data='choose_exit'))

@bot.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.set_chat_permissions(message.chat.id, types.ChatPermissions(True))
    new_game = Game()
    games[message.chat.id] = new_game
    await bot.send_message(message.chat.id, messages.start, reply_markup=markup_start)
    
@bot.message_handler(commands=['rules']) #сделать через кнопку в главном сообщении
async def start_message(message: types.Message):
    markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🔙Назад',callback_data='but_rules'))
    await bot.send_message(message.from_user.id, messages.rules,reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: call.data == 'join_group')
async def join_group_callback(call: types.CallbackQuery):
    group = games[call.message.chat.id]
    if group.add_user(call.from_user):
        await bot.answer_callback_query(callback_query_id=call.id, text="Вы уже участвуете в игре!", show_alert=True)
        return
    await bot.edit_message_text(
        f"Участники:\n{group.get_users()}",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup_start
    )
    print(call.message.message_id, call.message.chat.id)
    await bot.send_message(call.from_user.id, "Нажми на кнопку ниже, если готов начать игру или выйти", reply_markup=markup_choose, 
                            reply_parameters=types.ReplyParameters(message_id=call.message.message_id, chat_id=call.message.chat.id))


async def start_game(chat_id, message_id):
    print('ok')
    group = games[chat_id]
    await bot.edit_message_text(f'Игра начинается!\n\nУчастники:\n{group.get_users()}', chat_id, message_id)
    await bot.set_chat_permissions(chat_id, types.ChatPermissions(False))
    # for user in bot.members
    for user in group.players:
        member = await bot.get_chat_member(chat_id, user[0].id)
        print(member.can_send_messages)
        if member.status != 'creator':
            await bot.restrict_chat_member(chat_id, user[0].id, permissions=types.ChatPermissions(True))
        member = await bot.get_chat_member(chat_id, user[0].id)
        print(member.can_send_messages)

@bot.callback_query_handler(func=lambda call: call.data == 'choose' or call.data == 'choose_exit')
async def choose_callback(call: types.CallbackQuery):
    group = games[call.message.external_reply.chat.id]
    for user in group.players:
        if user[0].id == call.from_user.id:
            if call.data == 'choose':
                user[1] = not user[1]
                if len(group.players) >= 1 and group.check_ready():
                    await start_game(call.message.external_reply.chat.id, call.message.external_reply.message_id)
            if call.data == 'choose_exit':
                group.delete(call.from_user)
                if len(group.players) < 1:
                    await bot.edit_message_text(messages.start, call.message.external_reply.chat.id,
                                                call.message.external_reply.message_id, reply_markup=markup_start)
                    return
    await bot.edit_message_text(
        f"Участники:\n{group.get_users()}",
        call.message.external_reply.chat.id,
        call.message.external_reply.message_id,
        reply_markup=markup_start
    )

async def main():
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())

asyncio.run(bot.polling(none_stop=True))
