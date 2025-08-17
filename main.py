import os
from dotenv import load_dotenv
import subprocess
from classes.generator.dpf_generator import DPFGenerator
from classes.generator.duk_generator import DUKGenerator
from classes.generator.dwm_generator import DWMGenerator
from classes.web_scraper.web_scraper import WebScraper
from classes.postman.postman import Postman
from classes.form_builder.duk.education.postgraduate_schools.application_builder import PostgraduateSchoolsApplicationBuilder
from classes.generator import applications

load_dotenv()

base_url = os.getenv("BASE_URL")
login_data = {
    "email": os.getenv("LOGIN_EMAIL"),
    "password": os.getenv("LOGIN_PASSWORD"),
}


def example():
    """
    Przykładowa funkcja pokazująca pracę programu
    """

    # 1. Inicjalizacja i generowanie formularza w formacie JSON
    application_class = applications.get_application_builder(department='duk', program='po2', priority='pr1')
    application = application_class()
    application.generate()

    # 2. Podmiana formularza na stronie oraz pobranie pliku pdf
    postman = Postman(
        base_url,
        login_data
    )

    postman.login()
    postman.application_autosave(
        form_id=application.form_id,
        json=application.output_json
    )
    postman.application_pdf(
        output_path=f"output/pdf/{application.department_name}/{application.json_type}/po_{application.operation_num}_pr_{application.priority_num}",
        json=application.output_json
    )

    # 3. Zapisanie widoku strony (widok użytkownika)
    scraper = WebScraper(
        base_url,
        login_data,
        screenshot_path='output/screenshots'
    )

    scraper.login()
    scraper.close_introjs()
    scraper.screenshot_pages_of_application(
        form_id=application.form_id,
        pages=len(application.parts),
        department=application.department_name,
        program=application.operation_num,
        priority=application.priority_num,
        form_type="application"
    )
    scraper.close()


def main():
    example()


if __name__ == '__main__':
    main()
