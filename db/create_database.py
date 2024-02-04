import sqlite3

con = sqlite3.connect('./Users.db')
cur = con.cursor()

cur.execute("""CREATE TABLE Users(
user_id TEXT,
user_name TEXT,
user_lang TEXT
);""")
con.commit()
