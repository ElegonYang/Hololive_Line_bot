import pymysql


def db_set():

    connect = pymysql.connect(**db_setting)

    cursor_ = connect.cursor()

    return connect, cursor_


if __name__ == "__main__":
    conn, cursor = db_set()
    conn.close()
