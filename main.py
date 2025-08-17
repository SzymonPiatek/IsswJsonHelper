import os
from dotenv import load_dotenv
import subprocess
from classes.generator.dpf_generator import DPFGenerator
from classes.generator.duk_generator import DUKGenerator
from classes.generator.dwm_generator import DWMGenerator
from classes.web_scraper.web_scraper import WebScraper
from classes.postman.postman import Postman
from classes.form_builder.duk.education.postgraduate_schools.application_builder import PostgraduateSchoolsApplicationBuilder

load_dotenv()

base_url = os.getenv("BASE_URL")
login_info = {
    "url": f"{base_url}/{os.getenv("LOGIN_URL")}",
    "email": os.getenv("LOGIN_EMAIL"),
    "password": os.getenv("LOGIN_PASSWORD"),
}


def main():
    # for generator in [DPFGenerator, DUKGenerator, DWMGenerator]:
    #     generator().generate_applications_and_reports()
    #
    # subprocess.run(["python", "scripts/delete_unused_args.py"], check=True)
    #
    # scraper = WebScraper(
    #     base_url=base_url,
    #     login_data=login_info,
    #     screenshot_path='output/screenshots'
    # )
    # scraper.run()

    application = PostgraduateSchoolsApplicationBuilder()
    application.generate()

    postman = Postman(
        base_url,
        email=login_info["email"],
        password=login_info["password"],
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


if __name__ == '__main__':
    main()
