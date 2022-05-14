from db_config.db_setting import *
from datetime import datetime


# 更新頻道狀態
def update_to_db(status_code, title, v_name, live_url):

    conn, cursor = db_set()

    update_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    query = {'online_status': status_code, 'stream_title': title, 'v_name': v_name, 'live_url': live_url, 'check_time': update_datetime}

    sql = "update hololive_status set `online_status`=%(online_status)s, `stream_title`=%(stream_title)s, `live_url`=%(live_url)s, `check_time`=%(check_time)s where `vtuber_name`=%(v_name)s"

    cursor.execute(sql, query)
    conn.commit()
    conn.close()


# 拿到頻道網址
def select_target(v_name):

    conn, cursor = db_set()

    sql = "select ch_domain_page from hololive_status where vtuber_name='%s' " % v_name

    cursor.execute(sql)
    result = cursor.fetchone()[0]

    return result


# 拿到直播狀態碼
def check_stream(v_name):

    conn, cursor = db_set()

    sql = "select online_status from hololive_status where vtuber_name='%s' " % v_name

    cursor.execute(sql)
    status_code = cursor.fetchone()[0]
    print(status_code)

    return status_code


# 拿到直播標題 網址
def stream_url_title(v_name):

    conn, cursor = db_set()

    sql = "select stream_title, live_url from hololive_status where vtuber_name='%s' " % v_name
    cursor.execute(sql)
    result = cursor.fetchall()
    stream_title = result[0][0]
    live_url = result[0][1]

    return stream_title, live_url





# def go():
#
#     names = ['ame', 'ina', 'cali', 'gura', 'kiara']
#
#     for name in names:
#
#         print('checking:', name)
#
#         stream_href = select_target(name)
#
#         online_check, stream_title, stream_href = stream_check(name, stream_href)
#
#         if online_check == 'online':
#
#             update_to_db(1, stream_title, name, stream_href)
#
#         else:
#
#             update_to_db(0, None, name, None)
