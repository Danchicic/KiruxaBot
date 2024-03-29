from .databaseCRUD import UserDataBase

db = UserDataBase()
start_questions = {
    '1': 'Введите свою страну',
    '2': 'Выберите ваш тип обучения',
    '3': 'Выберите год поступления',
    '4': 'Введите свою группу',
    '5': 'Введите свой возраст',
    '6': 'Введите свое полное имя:\n{Имя} {Фамилия}'
}
questions = {
    '1': 'Играли ли вы когда нибудь в баскетбол?',
    '2': 'Играли ли вы в какой нибудь команде?',
    '3': 'Знаете ли вы правила баскетбола?',
    '4': 'Хотите ли вы выступать за команду по баскетболу?',
}
supported_langs = {
    'English 🏴󠁧󠁢󠁥󠁮󠁧󠁿': 'en',
    'Spanish 🇪🇸': 'es',
    'Italian 🇮🇹': 'it',
    "French 🇫🇷": 'fr',
    "Russian 🇷🇺": 'ru'
}
