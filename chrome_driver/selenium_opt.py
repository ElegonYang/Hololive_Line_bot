from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform


class Selenium:

    def __init__(self):

        self.fh = \
            ("Safari: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) "
             "Version/13.0 Safari/605.1.15")

    def opt_add_argv(self):

        option = Options()
        option.add_argument("user-agent={}".format(self.fh))
        option.add_argument("--blink-settings=imagesEnabled=false")
        option.add_argument('--no-sandbox')
        # option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--dns-prefetch-disable')
        option.add_argument("window-size=1920,1080")
        option.add_argument('--headless')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument('--profile-directory=Default')

        return option

    def platform_is(self):

        result = str(platform.system())

        if result == "Linux":
            driver_linux = webdriver.Chrome(
                executable_path="/home/memoryangelff7/repo/Hololive_Line_bot/chrome_driver/chromedriver",
                chrome_options=self.opt_add_argv())

            return driver_linux

        if result == "Windows":
            driver_windows = webdriver.Chrome(
                executable_path=r'D:\PycharmProjects\Hololive_Line_bot\chrome_driver\chromedriver.exe',
                chrome_options=self.opt_add_argv())

            return driver_windows


