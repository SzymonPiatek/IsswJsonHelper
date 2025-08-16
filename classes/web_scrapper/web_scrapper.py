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
    def __init__(self, base_url: str, login_data: LoginData, screenshot_path: str, headless: bool = True):
        self.base_url = base_url
        self.login_data = login_data
        self.screenshot_path = screenshot_path

        self.options = Options()
        self.options.headless = headless
        self.driver = webdriver.Firefox(options=self.options)

    @delay_after(1)
    def go_to_page(self, url: str):
        self.driver.get(url)

    @delay_after(1)
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

    @delay_after(2)
    def login(self):
        self.go_to_page(url=self.login_data['url'])
        wait = WebDriverWait(self.driver, 10)

        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email.value")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password.value")))

        email_input.send_keys(self.login_data["email"])
        password_input.send_keys(self.login_data["password"])
        password_input.send_keys(Keys.RETURN)

    @delay_after(1)
    def click_button_by_text(self, text: str):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, f"//button[contains(text(), '{text}')]"))
            )
            buttons = self.driver.find_elements(By.XPATH, f"//button[contains(text(), '{text}')]")
            for button in buttons:
                if button.is_displayed() and button.is_enabled():
                    try:
                        self.driver.execute_script("arguments[0].click();", button)
                    except Exception as e:
                        print(f"Nie udało się kliknąć przycisku '{text}':", e)
                    break
        except Exception:
            pass

    def capture_screenshot(self, screen_size: str, file_path: str):
        file_name = f"{self.screenshot_path}/{file_path}.png"

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

    def screenshot_pages_of_application(self, form_id: int, pages: int, department: str, program: str, priority: str, form_type: str):
        os.makedirs(f"{self.screenshot_path}/{department}/{form_type}/po_{program}_pr_{priority}", exist_ok=True)

        for page in range(0, pages):
            self.go_to_page(url=f"{self.base_url}/wniosek/{form_id}/edycja?version=-1&strona={page}")
            self.click_button_by_text("Rozumiem")
            self.click_button_by_text("Nie pokazuj więcej")
            self.capture_screenshot(screen_size="full", file_path=f"{department}/{form_type}/po_{program}_pr_{priority}/page_{page}")

    def run(self):
        try:
            self.login()
            self.close_introjs()

            self.screenshot_pages_of_application(
                form_id=2312,
                pages=9,
                department="DPF",
                program="1",
                priority="3",
                form_type="application",
            )
        finally:
            self.close()
