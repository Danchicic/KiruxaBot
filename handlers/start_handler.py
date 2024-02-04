from aiogram import F, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter

from FSM import FSMTest, FSMStartInfo
from config import config
from db import db, questions, start_questions
from db.databaseCRUD import UserRow
from keyboards import K
from lexicon import LEXICON_EN
from services import translate_text

command_router = Router()

bot = Bot(token=config.tg_bot.token)


@command_router.message(F.text == '/start')
async def hello(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_EN['/start'], reply_markup=K.langs_keyb())
    await state.set_state(FSMStartInfo.choose_language)
    await state.update_data(user_id=message.from_user.id)


@command_router.callback_query(StateFilter(FSMStartInfo.choose_language))
async def get_language(callback: CallbackQuery, state: FSMContext):
    print('no')
    db.write_user(UserRow(user_id=str(callback.from_user.id),
                          user_fullname=callback.from_user.full_name,
                          user_language=callback.data
                          ))
    await bot.send_message(chat_id=callback.message.chat.id,
                           text=translate_text(text=start_questions['1'], to_lang=callback.data),

                           )
    await state.set_state(FSMStartInfo.choose_country)


@command_router.message(StateFilter(FSMStartInfo.choose_country))
async def get_country(message: Message, state: FSMContext):
    user_lang = db.get_user_language(message.from_user.id)
    await message.answer(text=translate_text(start_questions['2'],
                                             to_lang=user_lang),
                         reply_markup=K.type_learn_kb(user_lang)
                         )
    await state.update_data(user_country=message.text)
    await state.set_state(FSMStartInfo.type_learning)


@command_router.message(StateFilter(FSMStartInfo.type_learning))
async def get_type(message: Message, state: FSMContext):
    user_lang = db.get_user_language(message.from_user.id)
    await message.answer(text=translate_text(start_questions['3'], to_lang=user_lang),
                         reply_markup=K.choose_year())
    await state.update_data(type_learning=message.text)
    await state.set_state(FSMStartInfo.entering_year)


@command_router.message(StateFilter(FSMStartInfo.entering_year))
async def get_type(message: Message, state: FSMContext):
    user_lang = db.get_user_language(message.from_user.id)
    await message.answer(text=translate_text(start_questions['4'], to_lang=user_lang))
    await state.update_data(enter_year=message.text)
    await state.set_state(FSMStartInfo.age)


@command_router.message(StateFilter(FSMStartInfo.age))
async def get_type(message: Message, state: FSMContext):
    user_lang = db.get_user_language(message.from_user.id)
    await message.answer(text=translate_text(start_questions['5'], to_lang=user_lang))
    await state.update_data(age=message.text)
    await state.set_state(FSMStartInfo.fullname)


@command_router.message(StateFilter(FSMStartInfo.fullname))
async def get_type(message: Message, state: FSMContext):
    user_lang = db.get_user_language(message.from_user.id)
    await message.answer(text=translate_text(start_questions['6'], to_lang=user_lang))
    await state.update_data(fullname=message.text)
    await state.set_state(FSMStartInfo.group_name)


@command_router.message(StateFilter(FSMStartInfo.group_name))
async def send_first_question(message: Message, state: FSMContext):
    await state.update_data(group=message.text)
    user_lang = db.get_user_language(message.from_user.id)
    await message.answer(
        text=translate_text(text=questions['1'], to_lang=user_lang),
        reply_markup=K.create_double_answer_kb(user_lang))
    await state.set_state(FSMTest.question1)
