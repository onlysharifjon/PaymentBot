import sqlite3

connect = sqlite3.connect('PayBot')
cursor = connect.cursor()


async def check_user(user_id):
    a = cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()
    return a


async def add_user(user_id, phone):
    cursor.execute('INSERT INTO users (user_id,phone) VALUES(?,?)', (user_id, phone,))
    connect.commit()
    return 'saved'

#
# cursor.execute('CREATE TABLE IF NOT EXISTS cards(user_id TEXT UNIQUE,uzcard_humo TEXT,rub TEXT,usz TEXT,usd TEXT)')
#
