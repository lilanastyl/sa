from telebot import types


connect_button = types.InlineKeyboardButton('Присоединиться', callback_data='join_group')
change_ready_button = types.InlineKeyboardButton('Смена готовности', callback_data='choose')
exit_button = types.InlineKeyboardButton('Выйти', callback_data='choose_exit')
physical_char_button = types.InlineKeyboardButton('Физические характеристики', callback_data='physical_char')
personally_char_button = types.InlineKeyboardButton('Личностные характеристики', callback_data='personally_char')


markup_start = types.InlineKeyboardMarkup().add(connect_button)
markup_start1 = types.InlineKeyboardMarkup().add(connect_button, change_ready_button, exit_button,row_width=1)
markup_game = types.InlineKeyboardMarkup().add(physical_char_button, personally_char_button, row_width=1)