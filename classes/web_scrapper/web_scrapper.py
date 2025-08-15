from typing import TypedDict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from functools import wraps
import base64


def delay_after(seconds=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(seconds)
            return result

        return wrapper

    return decorator


class LoginData(TypedDict):
    url: str
    email: str
    password: str


class WebScrapper:
    def __init__(self, login_data: LoginData, screenshot_path: str, headless: bool = True):
        self.login_data = login_data
        self.screenshot_path = screenshot_path

        self.options = Options()
        self.options.headless = headless
        self.driver = webdriver.Firefox(options=self.options)

    @delay_after(3)
    def go_to_page(self, url: str):
        self.driver.get(url)

    @delay_after(3)
    def close_introjs(self):
        while True:
            try:
                tooltip = self.driver.find_element(By.CLASS_NAME, "introjs-tooltip")
            except Exception:
                break

            try:
                header = tooltip.find_element(By.CLASS_NAME, "introjs-tooltip-header")
                skip_btn = header.find_element(By.CLASS_NAME, "introjs-skipbutton")
                skip_btn.click()
                time.sleep(1)
            except Exception:
                break

    @delay_after(3)
    def login(self):
        self.go_to_page(url=self.login_data['url'])
        wait = WebDriverWait(self.driver, 10)

        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email.value")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password.value")))

        email_input.send_keys(self.login_data["email"])
        password_input.send_keys(self.login_data["password"])
        password_input.send_keys(Keys.RETURN)

    def capture_screenshot(self, screen_size: str):
        timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
        file_name = f"{self.screenshot_path}/{timestamp}.png"

        if screen_size == "full":
            self.driver.get_full_page_screenshot_as_file(file_name)
        elif screen_size == "window":
            self.driver.set_window_size(1920, 1080)
            self.driver.save_screenshot(file_name)
        else:
            raise ValueError("screen_size must be either 'window' or 'full'")

        print(f"Zrzut ekranu zapisany jako: {file_name}")

    def close(self):
        self.driver.quit()

    def run(self):
        try:
            self.login()
            self.close_introjs()
            self.capture_screenshot(screen_size='full')
        finally:
            self.close()
