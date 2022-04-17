from uuid import uuid4
import sqlite3


# def create_short_url(url, text=''):
#     short_url = is_url_exist(url)
#     if short_url is None:
#         return insert_new_url(url, text)
#     return short_url
#
#
# def is_url_exist(url):
#     connection = sqlite3.connect('test.db')
#     result = connection.execute("SELECT * FROM ShortURL WHERE REAL_URL=?", [url])
#     if result:
#         return result.fetchone()
#     return None


def get_post(url_uuid):
    connection = sqlite3.connect('test.db')
    result = connection.execute("SELECT TEXT FROM Posts WHERE UUID=?", [url_uuid])
    if result:
        return result.fetchone()
    return None


def insert_new_post(text, ip):
    connection = sqlite3.connect('test.db')
    uuid = uuid4().hex
    connection.execute("INSERT INTO Posts VALUES (?, ?, ?)", [uuid, text, ip]);
    connection.commit()
    connection.close()
    return 'localhost:5000/' + uuid

