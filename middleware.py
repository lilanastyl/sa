from telebot import types, asyncio_handler_backends
from telebot.async_telebot import AsyncTeleBot
from group import Group, groups
from person import Person
from dataclasses import dataclass
from markups import markup_start1, markup_start
import messages
import re

@dataclass
class MiddlewareData():
    group: Group
    user: Person

class MyMiddleware(asyncio_handler_backends.BaseMiddleware):
    def __init__(self, bot):
        self.bot: AsyncTeleBot = bot
        self.update_sensitive = True
        self.update_types = ['callback_query']
    
    async def pre_process_callback_query(self, call: types.CallbackQuery, data: MiddlewareData):
        group = groups[call.message.chat.id]
        user = group.get_user(call.from_user.id)

        if call.data == 'join_group' and user:
            await self.bot.answer_callback_query(callback_query_id=call.id, text="Вы уже участвуете в игре!", show_alert=True)
            return asyncio_handler_backends.CancelUpdate()

        if not user and not call.data == 'join_group':
            await self.bot.answer_callback_query(call.id, text="Вы не участвуете в игре!", show_alert=True)
            return asyncio_handler_backends.CancelUpdate()
        
        match = re.match(r'^user_(\d+)$', call.data)
        if match and user.choose:
            await self.bot.answer_callback_query(call.id, text="Вы уже проголосовали!", show_alert=True)
            return asyncio_handler_backends.CancelUpdate()
        if match and user.user_info.id == int(match.group(1)):
            await self.bot.answer_callback_query(call.id, text="Нельзя голосовать против себя!", show_alert=True)
            return asyncio_handler_backends.CancelUpdate()

        data['group'] = group
        data['user'] = user

        return asyncio_handler_backends.ContinueHandling()

    async def post_process_callback_query(self, call:types.CallbackQuery, data, exception):
        data = MiddlewareData(**data)

        if len(data.group.players) < 1:
            await self.bot.edit_message_text(messages.start, call.message.chat.id,
                                            call.message.message_id, reply_markup=markup_start)
            return asyncio_handler_backends.ContinueHandling()

        if not data.group.game_status:
            await self.bot.edit_message_text(
                f"Участники:\n{data.group.get_users()}",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=markup_start1
            )

        return asyncio_handler_backends.ContinueHandling()