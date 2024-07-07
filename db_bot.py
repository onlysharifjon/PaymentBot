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


async def check_card_informations(user_id):
    data = cursor.execute('SELECT card_id,uzb_id,usd_id,rub_id FROM users WHERE user_id=?', (user_id,)).fetchone()
    return data


#
# cursor.execute('CREATE TABLE IF NOT EXISTS cards(user_id TEXT UNIQUE,uzcard_humo TEXT,rub TEXT,usz TEXT,usd TEXT)')
#
async def card_humo_update_add(card_id, user_id):
    cursor.execute('UPDATE users SET card_id=? WHERE user_id=?', (card_id, user_id))
    connect.commit()
    return 'Updated'


async def rub_update(rub_id, user_id):
    cursor.execute('UPDATE users SET rub_id=? WHERE user_id=?', (rub_id, user_id))
    connect.commit()
    return 'Updated'


async def usd_update(usd_id, user_id):
    cursor.execute('UPDATE users SET usd_id=? WHERE user_id=?', (usd_id, user_id))
    connect.commit()
    return 'Updated'


async def uzb_update(uzb_id, user_id):
    cursor.execute('UPDATE users SET uzb_id=? WHERE user_id=?', (uzb_id, user_id))
    connect.commit()
    return 'Updated'
