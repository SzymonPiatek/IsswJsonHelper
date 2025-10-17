import os
from dotenv import load_dotenv
from classes.analyzer.analyzer import Analyzer
from classes.postman.postman import Postman
from classes.web_scraper.web_scraper import WebScraper
from classes.applications import Applications2025, Applications2026


class FormHelper:
    def __init__(self, year: str = '2026'):
        load_dotenv()

        self.base_url = os.getenv('BASE_URL')
        self.login_data = {
            "email": os.getenv('LOGIN_EMAIL'),
            "password": os.getenv('LOGIN_PASSWORD')
        }

        self.year = year
        self.all_applications = {
            "2025": Applications2025(),
            "2026": Applications2026(),
        }
        self.applications = self.all_applications[self.year]

        self.setup = {
            "autosave_or_update": True,
            "force_autosave": True,
            "pdf": False,
            "web": False,
            "analyze": False,
        }

        self.postman = Postman(base_url=self.base_url, login_data=self.login_data)
        self.analyzer = Analyzer()
        self.scraper = None
        if self.setup["web"]:
            self.scraper = WebScraper(self.base_url, self.login_data)
            self.scraper.login()

    def generate_json(self, data_type: str, department: str, program: str, priority: str):
        if data_type == "application":
            builder_class = self.applications.get_application_builder(
                department=department, program=program, priority=priority
            )
        elif data_type == "report":
            builder_class = self.applications.get_report_builder(
                department=department, program=program, priority=priority
            )
        else:
            raise ValueError(f"Nieobsługiwany typ formularza: {data_type}")

        builder = builder_class()
        builder.generate()
        return builder

    def generate_process(self, data_type: str):
        if data_type not in {"application", "report"}:
            raise ValueError(f"Nieobsługiwany typ formularza: {data_type}")

        for department, programs in self.applications.builder_map.get(data_type, {}).items():
            for program, priorities in programs.items():
                for priority in priorities:
                    print("=" * 50)
                    print(f"[{department.upper()}] {program.upper()} {priority.upper()} - {data_type.upper()}")

                    app = self.generate_json(data_type, department, program, priority)

                    if self.setup["autosave_or_update"]:
                        is_success = False
                        if not self.setup["force_autosave"]:
                            is_success = self.postman.application_update_schema(
                                form_id=app.form_id,
                                json=app.output_json,
                            )

                        if self.setup["force_autosave"] or not is_success:
                            self.postman.application_autosave(
                                form_id=app.form_id,
                                json=app.output_json,
                            )

                    if self.setup["pdf"] and app.json_type == "application":
                        self.postman.application_pdf(
                            output_path=f"output/pdf/{app.year}/{app.department_name}/{app.json_type}/po_{app.operation_num}_pr_{app.priority_num}",
                            json=app.output_json,
                            form_id=app.form_id,
                        )

                    if self.setup["web"]:
                        self.scraper.screenshot_pages_of_form(application=app, output_path=f"output/png/{app.department_name}/{app.json_type}/po_{app.operation_num}_pr_{app.priority_num}")

        if self.setup["analyze"]:
            self.run_analysis(data_type)

    def run_analysis(self, data_type: str):
        for department in ["DPF", "DUK", "DWM"]:
            base_dir = f"./output/json/{self.year}/{department}/{data_type}"
            output_dir = f"./output/analyzer/{self.year}/{department}/{data_type}"

            self.analyzer.report_missing_validators(base_dir, output_dir, file_name="missing_validators")
            self.analyzer.report_unknown_rules(base_dir, output_dir, file_name="unknown_rules")
            self.analyzer.report_redundant_validators(base_dir, output_dir, file_name="redundant_validators")
            self.analyzer.report_many_validators(base_dir, output_dir, file_name="many_validators", validators_num=3)

    def example(self):
        app = self.generate_json(data_type="application", department="duk", program="po2", priority="pr1")

        self.postman.application_autosave(form_id=app.form_id, json=app.output_json)
        self.postman.application_pdf(
            output_path=f"output/pdf/{app.department_name}/{app.json_type}/po_{app.operation_num}_pr_{app.priority_num}",
            json=app.output_json,
        )

        scraper = WebScraper(self.base_url, self.login_data, output_path="output/screenshots")
        scraper.login()
        scraper.close_introjs()
        scraper.screenshot_pages_of_form(application=app, output_path="output/png")
        scraper.close()
