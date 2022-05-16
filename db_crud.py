from db_config import *
from datetime import datetime
from itertools import chain


# 拿到頻道網址
def get_channel_url(con, cur):
    sql = "select ch_id, ch_url from channel_info"
    cur.execute(sql)
    result = cur.fetchall()

    url_dict = {}

    for res in result:
        url_dict[res[0]] = res[1]

    return url_dict


# 防重複寫入
def check_video_in_db(con, cur, v_url):
    sql = "select v_url from bbq_info where v_url='%s'" % v_url
    cur.execute(sql)
    result = cur.fetchone()

    return not result


# 寫入資料
def insert_video(con, cur, ch_id, v_title, v_url):
    create_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    query = {'ch_id': ch_id, 'v_title': v_title, 'v_url': v_url, 'create_datetime': create_datetime}

    sql = "insert into bbq_info (`ch_id`, `v_title`, `v_url`, `create_datetime`) values ( %(ch_id)s, %(v_title)s, %(v_url)s, %(create_datetime)s)"

    cur.execute(sql, query)
    con.commit()
