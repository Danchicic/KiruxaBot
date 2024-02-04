from aiogram import Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from FSM import FSMTest
from config import config
from db import questions, db
from keyboards import K
from lexicon import LEXICON_EN
from services import translate_text, create_to_user_message

test_router = Router()
bot = Bot(token=config.tg_bot.token)


@test_router.message(StateFilter(FSMTest.question1))
async def send_second_question(message: Message, state: FSMContext):
    user_lang = db.get_user_language(message.from_user.id)
    if user_lang is None:
        await message.answer('Вас нет в базе данных, начните сначала')
        return
    await message.answer(text=translate_text(text=questions['2'],
                                             to_lang=user_lang))
    await state.update_data(ans1=message.text)
    await state.set_state(FSMTest.question2)


@test_router.message(StateFilter(FSMTest.question2))
async def send_third_question(message: Message, state: FSMContext):
    user_lang = db.get_user_language(message.from_user.id)
    await message.answer(text=translate_text(text=questions['3'],
                                             to_lang=user_lang))
    await state.update_data(ans2=message.text)
    await state.set_state(FSMTest.question3)


@test_router.message(StateFilter(FSMTest.question3))
async def send_four_question(message: Message, state: FSMContext):
    user_lang = db.get_user_language(message.from_user.id)
    await message.answer(text=translate_text(text=questions['4'],
                                             to_lang=user_lang),
                         reply_markup=K.create_double_answer_kb(user_lang, True))
    await state.update_data(ans3=message.text)
    await state.set_state(FSMTest.question4)


@test_router.message(StateFilter(FSMTest.question4))
async def send_fiv_question(message: Message, state: FSMContext):
    await state.update_data(ans4=message.text)
    await message.answer(text=LEXICON_EN['end_test'])
    text_bot = await create_to_user_message(await state.get_data())
    print(text_bot)
    await bot.send_message(chat_id=config.chat_id_to_send,
                           text=text_bot)

    # bot_compiled_message = await create_to_user_message(state.get_data())
