from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db import supported_langs
from services import translate_text


class Keyboard:
    @staticmethod
    def langs_keyb(width=2):
        kb_builder = InlineKeyboardBuilder()
        buttons: list[InlineKeyboardButton] = [InlineKeyboardButton(text=lang, callback_data=abbreviation)
                                               for lang, abbreviation in
                                               supported_langs.items()]
        return kb_builder.row(*buttons, width=width).as_markup(resize_keyboard=True)

    @staticmethod
    def create_double_answer_kb(user_lang, one_time_keyboard=False):
        return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=translate_text('Да', user_lang)),
                                              KeyboardButton(text=translate_text('Нет', user_lang))]],
                                   resize_keyboard=True, one_time_keyboard=one_time_keyboard)

    @staticmethod
    def type_learn_kb(user_lang):
        return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=translate_text('М', user_lang)),
                                              KeyboardButton(text=translate_text('Б', user_lang)),
                                              KeyboardButton(text=translate_text('С', user_lang))
                                              ]],
                                   resize_keyboard=True)

    @staticmethod
    def choose_year():
        return ReplyKeyboardMarkup(keyboard=[[
            KeyboardButton(text=str(year)) for year in range(23, 17, -1)
        ]], resize_keyboard=True, one_time_keyboard=True)
