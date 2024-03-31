import os
import sqlite3
from request_api import func_light_in_one_room, days_info


def loader():
    data = []
    conn = sqlite3.connect("house_of_student_db.sqlite")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS apartment_data
                    (date TEXT, rooms_windows_status TEXT, rooms TEXT)''')
    dates = days_info()
    for day in days_info():
        rooms_windows_status = ';'.join([','.join(floor) for floor in func_light_in_one_room(*day.split('-'))[0]])
        rooms = ';'.join([','.join(floor) for floor in func_light_in_one_room(*day.split('-'))[1]])
        data.append(day, rooms_windows_status, rooms)
    cursor.executemany('INSERT INTO apartment_data VALUES (?,?,?)', data)
    conn.commit()
    conn.close()
