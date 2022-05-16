#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from chrome_driver import *
from db_crud import *
from db_config import *


"""
1.單推的DD烤肉Man: https://www.youtube.com/channel/UCX6fKN_3fpg5aq_G9WinaBg
2.Hololive箱推虎: https://www.youtube.com/channel/UCFREDjq-CjYRqQPCl7qDDzQ
3.山寨猫 Copy Cat: https://www.youtube.com/channel/UCCd5UjY31hqHjo2pE_Q3Y2g
4.OX 死神烤肉: https://www.youtube.com/c/OX%E6%AD%BB%E7%A5%9E%E7%83%A4%E8%82%89
5.R.P.S. Channel: https://www.youtube.com/c/crazypen1011
6.Hololive精華【偶像撿到槍】: https://www.youtube.com/c/%E5%81%B6%E5%83%8F%E6%92%BF%E5%88%B0%E6%A7%8D-Hololive%E7%B2%BE%E8%8F%AF
7.轉生的佛系烤肉檔: https://www.youtube.com/channel/UCLVCG4UED7CwmLfPlcRjvyQ
8.角卷綿羊x赤井心豚牧場: https://www.youtube.com/channel/UC9Z55NM455lDvD3yTGiBodw
9.タク-ふーみ專門店: https://www.youtube.com/channel/UC_C5S9hH9qt-Wnap8hqtYWA
10.Fumichi CH.符咪焼肉屋: https://www.youtube.com/user/vic52895
11.梟の深夜烤肉屋 - Fukurou's Barbecue House -:https://www.youtube.com/c/%E6%A2%9F%E3%81%AE%E6%B7%B1%E5%A4%9C%E7%83%A4%E8%82%89%E5%B1%8B
12.鯊語翻譯機 https://www.youtube.com/channel/UC_6L3F4P9YtAdxf5jZ1dfBg
13.阿崙的熟肉製所 https://www.youtube.com/channel/UCwnVtGbMROSpxoD4g7ia47g
14.杏福冰室 https://www.youtube.com/channel/UCJBzoYg5pMColM0GP6AWpaQ
15.Cinderella https://www.youtube.com/channel/UCerkxejYIKl5405scz4cubA
16.星街家の妹妹醬 https://www.youtube.com/channel/UClvv6a4GB8CMgNl1DW7dQ3A
17.殭屍單推人 Worst Hololive Clipper https://www.youtube.com/channel/UCBtB4w5yxlSjkNNI_XWqVJg
18.羽月的行動烤肉攤 https://www.youtube.com/channel/UCS8kSrD7PN76Pvt5U34UqGA
19.【まる君】神奇圈 一人炙燒屋 https://www.youtube.com/channel/UCP3KPLtWyedBvJ2YWY-IHTA/videos
20.YES! YMD! 山田(ラプラスダークネス)單推し翻譯精華液(可樂) 人手只有兩隻的翻譯小隊 https://www.youtube.com/c/YESYMD
21.W.D.小狂 CRAZY https://www.youtube.com/channel/UCxKaUIZW-LWiiWjeP6iydpA
22.尾丸座の屋根裏 https://www.youtube.com/c/%E5%B0%BE%E4%B8%B8%E5%BA%A7%E3%81%AE%E5%B1%8B%E6%A0%B9%E8%A3%8F
23.一夜Kazuya https://www.youtube.com/channel/UCkw6ffX2AJtTw1i7KW6m4XQ
24.用肝在翻譯【肝指數持續上升中】 https://www.youtube.com/channel/UCLB9LPemPH4fb8Nci1cDzBg
25.NENE社長の遜炮事務所Δ https://www.youtube.com/channel/UCu8ESvuVuvcZU0D3PGeU0yw
26.野生的全熟肉G / 野生のこんがり肉G https://www.youtube.com/channel/UCPdeyZAMwzSWM0hEAsiknug
27.克巴の翻譯 - 烤肉屋 https://www.youtube.com/channel/UCSDc6bjIfFMCYClGbqKigvg
28.沒有耳膜的烤肉men https://www.youtube.com/channel/UCXUeibOXCe30SSPgxgi7b9g
29.Hololive箱推虎 https://www.youtube.com/channel/UCFREDjq-CjYRqQPCl7qDDzQ
30.MakiQ 焼肉屋 https://www.youtube.com/channel/UC6UWd4QedNXaDGi3Hk_OTsA
31.米凱胡烤起來【ミケフ切り抜きch】https://www.youtube.com/channel/UCWBxpy9L8SrR7e7RfYSIpYw

"""


# 爬取 30個頻道 前30部影片並寫入DB
def crawler(con, cur, se_driver, ch_id, ch_url):

    se_driver.get(ch_url+'/videos')

    title_class = se_driver.find_elements(By.CSS_SELECTOR, 'div[id="meta"] h3')
    href_class = se_driver.find_elements(By.CSS_SELECTOR, 'div[id="meta"] h3 a')

    for title, href in zip(title_class, href_class):
        url = href.get_attribute('href')
        print(title.text, url)

        if check_video_in_db(con, cur, url):
            print('insert')
            insert_video(con, cur, ch_id, title.text, url)

        else:
            print('pass')
            continue


if __name__ == '__main__':

    conn, cursor = db_info()

    driver = Selenium().platform_is()
    ch_urls = get_channel_url(conn, cursor)

    for ch_id in range(1, len(ch_urls)):

        crawler(conn, cursor, driver, ch_id, ch_urls[ch_id])

    conn.close()
    driver.quit()
