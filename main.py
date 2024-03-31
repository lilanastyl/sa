from telebot import types
from telebot.async_telebot import AsyncTeleBot
import messages
import asyncio
from group import Group, groups
from middleware import MyMiddleware, MiddlewareData
from markups import markup_start

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

@bot.callback_query_handler()
async def choose_callback(call: types.CallbackQuery, data):
    try:
        data = MiddlewareData(**data)
        if call.data == 'join_group':
            data.group.add_user(call.from_user)
        if call.data == 'choose':
            data.user.choose = not data.user.choose
        if call.data == 'choose_exit':
            data.group.delete(call.from_user)
        if call.data == 'physical_char':
            await bot.answer_callback_query
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
