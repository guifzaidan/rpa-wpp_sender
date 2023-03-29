from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
# import urllib
import time


class WppSender():

    @staticmethod
    def _sleep_time():
        time.sleep(30)

    def __init__(self, headless:bool):
        self._service = Service(ChromeDriverManager().install())
        self._options = webdriver.ChromeOptions()
        self.screen = self.screen_headless(selection=headless)
        self._driver = webdriver.Chrome(service=self._service, options=self._options)

    def screen_headless(self, selection:bool):
        if selection == True:
            self._options.add_argument("--headless")
            # self._options.add_argument("disable-infobars")
            # self._options.add_argument("--disable-extensions")
            # self._options.add_argument("--disable-dev-shm-usage")
            # self._options.add_argument("--no-sandbox")

    def get_wpp_site(self):
        self._driver.get("https://web.whatsapp.com/")
        self._wait_loading()

    def _wait_loading(self):
        while len(self._driver.find_elements(By.ID, "side")) < 1:
            self._get_page_screenshot()
            time.sleep(1)

    def _get_page_screenshot(self):
        self._driver.get_screenshot_as_file("qr_code.png")

    def receivers_dataframe():
        pass        


class WppSenderLayout():
    
    def __init__(self):
        pass


if __name__ == "__main__":
    pass
