import os
from dotenv import load_dotenv
import subprocess
from classes.generator.dpf_generator import DPFGenerator
from classes.generator.duk_generator import DUKGenerator
from classes.generator.dwm_generator import DWMGenerator
from classes.web_scraper.web_scraper import WebScraper

load_dotenv()

base_url = os.getenv("BASE_URL")
login_info = {
    "url": f"{base_url}/{os.getenv("LOGIN_URL")}",
    "email": os.getenv("LOGIN_EMAIL"),
    "password": os.getenv("LOGIN_PASSWORD"),
}


def main():
    for generator in [DPFGenerator, DUKGenerator, DWMGenerator]:
        generator().generate_applications_and_reports()

    subprocess.run(["python", "scripts/delete_unused_args.py"], check=True)

    scraper = WebScraper(
        base_url=base_url,
        login_data=login_info,
        screenshot_path='output/screenshots'
    )
    scraper.run()


if __name__ == '__main__':
    main()
