import sqlite3
from dataclasses import dataclass


@dataclass
class UserRow:
    user_id: str
    user_fullname: str
    user_language: str


class UserDataBase:

    def __init__(self):
        self.conn = sqlite3.Connection('./db/Users.db')
        self.cur = self.conn.cursor()

    def write_user(self, data: UserRow):
        self.cur.execute(f"""SELECT user_id FROM Users  WHERE user_id='{data.user_id}';""")
        is_already_in = self.cur.fetchone()
        if is_already_in is not None:
            self.cur.execute(f"""
            UPDATE Users SET user_id='{data.user_id}', user_name='{data.user_fullname}', user_lang='{data.user_language}'
            """)
            self.conn.commit()
            return

        self.cur.execute(f"""
        INSERT INTO Users(user_id, user_name, user_lang) VALUES (?,?,?)
        """, (data.user_id, data.user_fullname, data.user_language)
                         )
        self.conn.commit()

    def get_user_language(self, user_id):
        self.cur.execute(f"""SELECT user_lang FROM Users WHERE user_id='{user_id}' """)
        lang = self.cur.fetchone()
        if lang is not None:
            return lang[0]
        return None
