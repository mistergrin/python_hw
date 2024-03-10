import sqlite3


def execute_query(query, args=()):
    connection = sqlite3.Connection('chinook.db')
    cursor = connection.cursor()
    cursor.execute(query, args)
    connection.commit()
    result = cursor.fetchall()
    return result
