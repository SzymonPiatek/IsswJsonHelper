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
    email: str
    password: str


class WebScraper:
    def __init__(self, base_url: str, login_data: LoginData, headless: bool = True):
        self.base_url = base_url
        self.login_data = login_data

        self.options = Options()
        self.options.headless = headless
        self.driver = webdriver.Firefox(options=self.options)

    def go_to_page(self, url: str, wait_for: str = None):
        self.driver.get(url)
        if wait_for:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), wait_for)
            )
        else:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

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

    @delay_after(1)
    def login(self):
        self.go_to_page(url=f"{self.base_url}/logowanie")
        wait = WebDriverWait(self.driver, 10)

        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email.value")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password.value")))

        email_input.send_keys(self.login_data["email"])
        password_input.send_keys(self.login_data["password"])
        password_input.send_keys(Keys.RETURN)

    def click_button_by_text(self, text: str):
        try:
            WebDriverWait(self.driver, 1).until(
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
        if screen_size == "full":
            self.driver.get_full_page_screenshot_as_file(file_path)
        elif screen_size == "window":
            self.driver.set_window_size(1920, 1080)
            self.driver.save_screenshot(file_path)
        else:
            raise ValueError("screen_size must be either 'window' or 'full'")

        print(f"Zrzut ekranu zapisany jako: {file_path}")

    def close(self):
        self.driver.quit()

    def screenshot_pages_of_form(self, application: dict, output_path: str):
        form_id = application.form_id
        json_type = "wniosek" if application.json_type == "application" else "raport"
        page = 0

        os.makedirs(output_path, exist_ok=True)

        for part in application.parts:
            self.go_to_page(
                url=f"{self.base_url}/{json_type}/{form_id}/edycja?version=-1&strona={page}",
                wait_for=part["title"]
            )
            self.click_button_by_text("Rozumiem")
            self.click_button_by_text("Nie pokazuj więcej")
            self.capture_screenshot(screen_size="full",
                                    file_path=f"{output_path}/page_{page}.png")
            page += 1
