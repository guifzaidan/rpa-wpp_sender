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

    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def screen_status(self, selection:bool):
        if selection == False:
            self.options.add_argument("--headless")

    def get_wpp_site(self):
        self.driver.get("https://web.whatsapp.com/")
        self._wait_loading()

    def _wait_loading(self):
        while len(self.driver.find_elements(By.ID, "side")) < 1:
            self._get_page_screenshot()
            time.sleep(1)

    def _get_page_screenshot(self):
        self.driver.get_screenshot_as_file("qr_code.png")


class WppSenderLayout():
    
    def __init__(self):
        pass


if __name__ == "__main__":
    pass
