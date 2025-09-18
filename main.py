import os
from dotenv import load_dotenv
from classes.web_scraper.web_scraper import WebScraper
from classes.postman.postman import Postman
from classes.analyzer.analyzer import Analyzer
from classes.form_builder.applications._2025.applications import Applications2025
from classes.form_builder.applications._2026.applications import Applications2026

load_dotenv()

base_url = os.getenv("BASE_URL")
login_data = {
    "email": os.getenv("LOGIN_EMAIL"),
    "password": os.getenv("LOGIN_PASSWORD"),
}

year = "2026"

all_applications = {
    "2025": Applications2025(),
    "2026": Applications2026(),
}

analyzer = Analyzer()

applications = all_applications[year]

postman = Postman(
    base_url,
    login_data,
)

setup = {
    "autosave_or_update": True,
    "force_autosave": False,
    "pdf": True,
    "web": False,
    "analyze": False
}


def example():
    """
    Przykładowa funkcja pokazująca pracę programu
    """

    # 1. Inicjalizacja i generowanie formularza w formacie JSON
    application = generate_application(
        department='duk',
        program='po2',
        priority='pr1'
    )

    # 2. Podmiana formularza na stronie oraz pobranie pliku pdf
    postman = Postman(
        base_url,
        login_data,
    )
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
        output_path='output/screenshots'
    )

    scraper.login()
    scraper.close_introjs()
    scraper.screenshot_pages_of_form(
        application=application,
        output_path='output/png'
    )
    scraper.close()


def generate_application(department: str, program: str, priority: str):
    application_class = applications.get_application_builder(department=department, program=program, priority=priority)
    application = application_class()
    application.generate()
    return application


def main():
    for department, programs in applications.builder_map.items():
        for program, priorities in programs.items():
            for priority in priorities:
                print("====="*10)
                print(f"[{department.upper()}] {program.upper()} {priority.upper()}")

                # Generowanie
                application = generate_application(
                    department=department,
                    program=program,
                    priority=priority
                )

                if setup.get("autosave_or_update", False):
                    is_success = False
                    if not setup.get("force_autosave", False):
                        # Aktualizacja
                        is_success = postman.application_update_schema(
                            form_id=application.form_id,
                            json=application.output_json
                        )

                    if setup.get("force_autosave", False) or not is_success:
                        # Podmiana
                        postman.application_autosave(
                            form_id=application.form_id,
                            json=application.output_json
                        )

                if setup.get("pdf", False):
                    # PDF
                    postman.application_pdf(
                        output_path=f"output/pdf/{application.year}/{application.department_name}/{application.json_type}/po_{application.operation_num}_pr_{application.priority_num}",
                        json=application.output_json
                    )

    if setup.get("analyze", False):
        for department in ["DPF", "DUK", "DWM"]:
            # analyzer.report_duplicates(
            #     base_dir=f"./output/json/{year}/{department}/application",
            #     output_path=f"./output/analyzer/{year}/{department}/application",
            #     file_name="duplicate_names"
            # )

            analyzer.report_missing_validators(
                base_dir=f"./output/json/{year}/{department}/application",
                output_path=f"./output/analyzer/{year}/{department}/application",
                file_name="missing_validators"
            )

            analyzer.report_unknown_rules(
                base_dir=f"./output/json/{year}/{department}/application",
                output_path=f"./output/analyzer/{year}/{department}/application",
                file_name="unknown_rules"
            )

            analyzer.report_redundant_validators(
                base_dir=f"./output/json/{year}/{department}/application",
                output_path=f"./output/analyzer/{year}/{department}/application",
                file_name="redundant_validators"
            )

            analyzer.report_many_validators(
                base_dir=f"./output/json/{year}/{department}/application",
                output_path=f"./output/analyzer/{year}/{department}/application",
                file_name="many_validators",
                validators_num=3
            )


if __name__ == '__main__':
    main()
