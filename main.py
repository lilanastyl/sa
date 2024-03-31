from telebot import types
from telebot.async_telebot import AsyncTeleBot
import messages
import asyncio
from group import Group, groups
from middleware import MyMiddleware, MiddlewareData
from markups import markup_start, markup_game
from threading import Timer

bot = AsyncTeleBot('6885805301:AAGcnYkpGfciC65TDPodn6k2nyRLS3NQKlY')

@bot.message_handler(commands=['start'])
async def start_message(message: types.Message):
    try:
        new_game = Group()
        groups[message.chat.id] = new_game
        await bot.send_message(message.chat.id, messages.start, reply_markup=markup_start)
    except Exception as error:
        print(error)

@bot.message_handler(commands=['rules']) #сделать через кнопку в главном сообщении
async def start_message(message: types.Message):
    try:
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('🔙Назад',callback_data='but_rules'))
        await bot.send_message(message.from_user.id, messages.rules,reply_markup=markup)
    except Exception as error:
        print(error)

async def start_game(data: MiddlewareData, chat_id):
    t = 3 
    while t:
        m, s = divmod(t, 60)
        timer = f'{m:02d} минут и {s:02d} секунд'
        await bot.send_message(chat_id, f'У вас есть {timer} для выбора участника, который покинет игру. Таймер уже тикает!')
        await asyncio.sleep(1)
        t -= 1
    await bot.send_message(chat_id, 'Время вышло, начнём голосование!')
    

@bot.callback_query_handler(func=lambda call: call.data)
async def choose_callback(call: types.CallbackQuery, data):
    try:
        data = MiddlewareData(**data)
        if call.data == 'join_group':
            data.group.add_user(call.from_user)
        if call.data == 'choose':
            data.user.choose = not data.user.choose
            if len(data.group.players) >= 1 and data.group.check_ready() and not data.group.game_status:
                await bot.edit_message_text(f'Игра начинается!\n\nУчастники:\n{data.group.get_users()}', call.message.chat.id, 
                                                call.message.message_id)
                await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup_game)
                data.group.game_status = True
                await start_game(data, call.message.chat.id)
        if call.data == 'choose_exit':
            data.group.delete(call.from_user)
        if call.data == 'physical_char':
            await bot.answer_callback_query(call.id, data.user.getPersonPhys(), True)
        if call.data == 'personally_char':
            await bot.answer_callback_query(call.id, data.user.getPersonPersonally(), True)
    except Exception as error:
        print(error)

@bot.message_handler()
async def message_handler(message: types.Message):
    try:
        group = groups[message.chat.id]
        if group.game_status and not group.get_user(message.from_user):
            await bot.delete_message(message.chat.id, message.message_id)
    except Exception as error:
        print(error)

bot.setup_middleware(MyMiddleware(bot))

async def main():
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())

asyncio.run(bot.polling(none_stop=True))
