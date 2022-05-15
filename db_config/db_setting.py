import pymysql


def db_set():

    db_setting = {

        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": 'aa552300',
        "db": "test"
    }

    connect = pymysql.connect(**db_setting)

    cursor_ = connect.cursor()

    return connect, cursor_


if __name__ == "__main__":
    conn, cursor = db_set()
    conn.close()
