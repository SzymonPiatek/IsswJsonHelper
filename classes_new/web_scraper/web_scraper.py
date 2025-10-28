from typing import TypedDict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class LoginData(TypedDict):
    email: str
    password: str


class WebScraper:
    def __init__(self, base_url: str, login_data: LoginData, headless: bool = True):
        self.base_url = base_url
        self.login_data = login_data

        self.options = Options()
        self.options.headless = headless

        self.options.set_preference("permissions.default.image", 2)
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.implicitly_wait(0)

        self.wait = WebDriverWait(self.driver, 1)

    def go_to_page(self, url: str, wait_for: str = None):
        self.driver.get(url)
        if wait_for:
            self.wait.until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), wait_for)
            )
        else:
            self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

    def login(self):
        self.go_to_page(f"{self.base_url}/logowanie")

        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email.value")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password.value")))

        email_input.send_keys(self.login_data["email"])
        password_input.send_keys(self.login_data["password"])
        password_input.send_keys(Keys.RETURN)

    def handle_intro_modal(self):
        try:
            checkbox_label = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[.//span[contains(text(), 'NIE POKAZUJ WIĘCEJ')]]"))
            )
            checkbox = checkbox_label.find_element(By.TAG_NAME, "input")
            if not checkbox.is_selected():
                self.driver.execute_script("arguments[0].click();", checkbox)

            button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Rozumiem')]")
            self.driver.execute_script("arguments[0].click();", button)
        except Exception:
            pass

    def click_button_by_text(self, text: str):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//button[contains(text(), '{text}')]"))
            )
            buttons = self.driver.find_elements(By.XPATH, f"//button[contains(text(), '{text}')]")
            for button in buttons:
                if button.is_displayed() and button.is_enabled():
                    self.driver.execute_script("arguments[0].click();", button)
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

        os.makedirs(output_path, exist_ok=True)

        for page, part in enumerate(application.parts):
            try:
                self.driver.get(f"{self.base_url}/{json_type}/{form_id}/edycja?version=-1&strona={page}")
                WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{part['title']}')]"))
                )
            except Exception:
                pass

            self.handle_intro_modal()
            self.click_button_by_text("Nie pokazuj więcej")

            self.capture_screenshot(
                screen_size="full",
                file_path=f"{output_path}/page_{page}.png"
            )
