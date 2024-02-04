from aiogram.filters.state import State, StatesGroup


class FSMTest(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()


class FSMStartInfo(StatesGroup):
    choose_language = State()
    choose_country = State()
    type_learning = State()
    entering_year = State()
    group_name = State()
    age = State()
    fullname = State()

