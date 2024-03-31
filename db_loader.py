import os
import sqlite3
from request_api import room_info, days_info


def loader():
    conn = sqlite3.connect("house_of_student_db.sqlite")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS apartment_data
                    (date TEXT, apartment_numbers TEXT, light_status TEXT)''')
    data = [
        ('2022-01-01', '1,2,3;4,5,6', 'True,True,True;False,False,False'),
        ('2022-01-02', '1,2,3;4,5,6', 'False,True,False;True,False,True')
    ]
    cursor.executemany('INSERT INTO apartment_data VALUES (?,?,?)', data)
    conn.commit()
    conn.close()


loader()
