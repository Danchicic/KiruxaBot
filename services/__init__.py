from googletrans import Translator

from db import questions

google_translator = Translator()


def translate_text(text: str, to_lang: str = 'en'):
    return google_translator.translate(text=text, dest=to_lang).text


async def create_to_user_message(user_data: dict):
    """
    exmple: {'user_country': 'россия',
    'type_learning': 'Б',
    'enter_year': '22',
    'group': 'эфбо-09-23',
    'ans1': 'Да',
    'ans2': 'Да',
    'ans3': 'Да',
    'ans4': 'Нет'}

    :param user_data:
    :return:
    """
    return f"""
#{user_data['type_learning']}{user_data['enter_year']}-{user_data['group']}\n
{user_data['fullname']}\n
{user_data['age']} лет\n
{user_data['user_country']}\n
{user_data['user_id']}\n
{questions['1']} - {user_data['ans1']}\n
{questions['2']} - {user_data['ans2']}\n
{questions['3']} - {user_data['ans3']}\n
{questions['4']} - {user_data['ans4']}
"""


if __name__ == '__main__':
    print(translate_text('my name is danya', 'fr'))
