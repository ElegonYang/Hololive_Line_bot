import pymysql


def db_set():

    db_setting = {

        "host": "34.81.126.51",
        "port": 3306,
        "user": "hololive-bbq",
        "password": " kK=LillE'.8o~;vJ",
        "db": "holo_bot"
    }

    connect = pymysql.connect(**db_setting)

    cursor_ = connect.cursor()

    return connect, cursor_


if __name__ == "__main__":
    conn, cursor = db_set()
    conn.close()
