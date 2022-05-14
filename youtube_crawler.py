from selenium.webdriver.common.by import By

"""
Watson Amelia https://www.youtube.com/channel/UCyl1z3jo3XHR1riLFKG5UAg
Ninomae Ina'nis https://www.youtube.com/channel/UCMwGHR0BTZuLsmjY_NT5Pwg
Gawr Gura https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g
Mori Calliope https://www.youtube.com/channel/UCL_qhgtOy0dy1Agp8vkySQg
Takanashi Kiara https://www.youtube.com/channel/UCHsx4Hqa-1ORjQTh9TYDhww

"""


def stream_check(crawler, vtuber, url):

    crawler.get(url)

    try:
        # 確認有沒有在直播
        stream_block = crawler.find_element(By.CSS_SELECTOR, 'ytd-channel-featured-content-renderer[class="style-scope ytd-item-section-renderer"]')
        # 拿到標題
        stream_title = crawler.find_element(By.CSS_SELECTOR, 'h3[class="title-and-badge style-scope ytd-video-renderer"]').text
        stream_href = crawler.find_element(By.CSS_SELECTOR, 'h3[class="title-and-badge style-scope ytd-video-renderer"] a').get_attribute('href')
        print(stream_href)

        return "online", stream_title, stream_href

    except:

        return 'offline', None, None










