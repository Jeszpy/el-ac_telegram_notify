from datetime import datetime
import fdb
from aiogram import Bot, Dispatcher, executor, types

con = fdb.connect(dsn='127.0.0.1:C:/Electra/El-Ac/train.fdb',
                  user='SYSDBA',
                  password='masterkey',
                  charset='WIN1251')

token = '2070861903:AAFNwC84mSIkzCUb5q4imWJPGCnQDYFZR3o'
hleb = 556203349


def listen_event():
    try:
        cond = con.event_conduit(["d_new_event"])
        select_num = "select max(num) as NUM from events"
        cur = con.cursor()
        cond.begin()
        cond.wait()
        cur.execute(select_num)
        num = cur.fetchone()
        # print(num[0])
        select_event = f"select * from events where num = {int(num[0])}"
        cur.execute(select_event)
        get_event = cur.fetchone()
        print(get_event)
        event_type = int(get_event[3])
        # print(event_type)
        if event_type == 405:
            name_num = int(get_event[5])
            reader = int(get_event[4])
            select_name = f"select username from users where num = {name_num}"
            select_reader = f"select read_name from d_devices where reader = {reader}"
            cur.execute(select_name)
            name = cur.fetchone()
            name = name[0]
            cur.execute(select_reader)
            reader_name = cur.fetchone()
            reader_name = reader_name[0]
            date_and_time = datetime.now().strftime("Дата: %d.%m.%Y, время: %H:%M:%S")
            print(name)
            print(reader_name)
            print(date_and_time)

    except Exception as e:
        print(e)
    finally:
        # con.close()
        pass


if __name__ == "__main__":
    while True:
        listen_event()
