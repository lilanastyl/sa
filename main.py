from telebot import types
from telebot.async_telebot import AsyncTeleBot
from group import Game, games
from person import Person
from telebot.apihelper import ApiException
import messages
import asyncio

bot = AsyncTeleBot('6885805301:AAGcnYkpGfciC65TDPodn6k2nyRLS3NQKlY')

markup_start = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Присоединиться', callback_data='join_group'))
markup_start1 = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Присоединиться', callback_data='join_group'), 
                                                types.InlineKeyboardButton('Смена готовности', callback_data='choose'), 
                                                types.InlineKeyboardButton('Выйти', callback_data='choose_exit'),
                                                row_width=1)

@bot.message_handler(commands=['start'])
async def start_message(message: types.Message):
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
        reply_markup=markup_start1
    )

async def start_game(chat_id, message_id):
    print(chat_id, message_id)
    group = games[chat_id]
    await bot.edit_message_text(f'Игра начинается!\n\nУчастники:\n{group.get_users()}', chat_id, message_id)
    group.game_status = True

@bot.callback_query_handler(func=lambda call: call.data == 'choose' or call.data == 'choose_exit')
async def choose_callback(call: types.CallbackQuery):
    group = games[call.message.chat.id]
    user: Person = group.check_user(call.from_user)
    if not user:
        await bot.answer_callback_query(call.id, text="Вы не участвуете в игре!", show_alert=True)
        return
    if call.data == 'choose':
        user.choose = not user.choose
        if len(group.players) >= 2 and group.check_ready():
            print(call.message.chat.id, call.message.message_id)
            await start_game(call.message.chat.id, call.message.message_id)
            return
    if call.data == 'choose_exit':
        group.delete(call.from_user)
        if len(group.players) < 1:
            await bot.edit_message_text(messages.start, call.message.chat.id,
                                        call.message.message_id, reply_markup=markup_start)
            return
    await bot.edit_message_text(
        f"Участники:\n{group.get_users()}",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup_start1
    )

@bot.message_handler()
async def message_handler(message: types.Message):
    group = games[message.chat.id]
    if group.game_status and not group.check_user(message.from_user):
        await bot.delete_message(message.chat.id, message.message_id)

async def main():
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())

asyncio.run(bot.polling(none_stop=True))
