from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import streamlit as st
import pandas as pd
import urllib
import time


class WppSender():

    # Global Vars
    footer_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'
    send_button_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'

    @staticmethod
    def _cycle_sleep_time():
        time.sleep(20)

    @staticmethod
    def _message_format(message:str):
        message_mod = urllib.parse.quote(f"{message}")
        return message_mod

    def __init__(self, headless:bool):
        self._service = Service(ChromeDriverManager().install())
        self._options = webdriver.ChromeOptions()
        self.screen = self._screen_headless(selection=headless)
        self._driver = webdriver.Chrome(service=self._service, options=self._options)

    def _screen_headless(self, selection:bool):
        if selection == True:
            self._options.add_argument("--headless")
            # self._options.add_argument("disable-infobars")
            # self._options.add_argument("--disable-extensions")
            # self._options.add_argument("--disable-dev-shm-usage")
            # self._options.add_argument("--no-sandbox")

    def get_wpp_site(self):
        self._driver.get("https://web.whatsapp.com/")
        self._initial_wait()
        self._driver.minimize_window()

    def _initial_wait(self):
        while len(self._driver.find_elements(By.ID, "side")) < 1:
            # self._get_page_screenshot()
            time.sleep(1)

    def _get_page_screenshot(self):
        self._driver.get_screenshot_as_file("qr_code.png")

    def send_messages(self, message:str, contacts:list):
        message_mod = self._message_format(message)
        progress_bar = st.progress(0, text="Enviando...")

        for i,contact in enumerate(contacts):
            url = f"https://web.whatsapp.com/send?phone={contact}&text={message_mod}"
            self._driver.get(url)

            self._messages_wait()
            self._click_send_button()

            progress_reference = ((i + 1) / len(contacts))
            progress_bar.progress(progress_reference, text="Enviando...")
            
            if progress_reference < 1:
                self._cycle_sleep_time()

        progress_bar.empty()

    def _messages_wait(self):
        while len(self._driver.find_elements(By.XPATH, self.footer_xpath)) < 1:
            time.sleep(2)

    def _click_send_button(self):
        self._driver.find_element(By.XPATH, self.send_button_xpath).click()


if __name__ == "__main__":
    pass