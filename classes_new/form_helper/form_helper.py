from dotenv import load_dotenv
import os
from classes_new.postman.postman import Postman
from classes_new.forms._2026.forms import Forms2026


class FormHelper:
    def __init__(self, year: int = 2026):
        load_dotenv()

        self.data = {
            "local": {
                "base_url": os.getenv('LOCAL_BASE_URL'),
                "login_email": os.getenv('LOCAL_LOGIN_EMAIL'),
                "login_password": os.getenv('LOCAL_LOGIN_PASSWORD')
            },
            "uat": {
                "base_url": os.getenv('UAT_BASE_URL'),
                "login_email": os.getenv('UAT_LOGIN_EMAIL'),
                "login_password": os.getenv('UAT_LOGIN_PASSWORD')
            }
        }

        self.all_forms = {
            "2026": Forms2026()
        }
        self.forms = self.all_forms[str(year)]

        self.setup = {
            "uat": {
                "autosave_or_update": False,
                "force_autosave": False,
                "pdf": False,
            },
            "local": {
                "autosave_or_update": True,
                "force_autosave": True,
                "pdf": False,
            }
        }

        self.uat_postman = Postman(
            base_url=self.data["uat"]["base_url"],
            login_data={
                "email": self.data["uat"]["login_email"],
                "password": self.data["uat"]["login_password"]
            }
        )

        self.local_postman = Postman(
            base_url=self.data["local"]["base_url"],
            login_data={
                "email": self.data["local"]["login_email"],
                "password": self.data["local"]["login_password"]
            }
        )

    def generate_jsons(self, data_type: str):
        if data_type not in {"application", "report"}:
            raise ValueError(f"Nieobsługiwany typ formularza: {data_type}")

        for department, programs in self.forms.builder_map.get(data_type, {}).items():
            for program, priorities in programs.items():
                for priority, builder in priorities.items():
                    if builder:
                        print(f'{"=" * 130}')
                        print(f"[{department.upper()}] {program.upper()} {priority.upper()} - {data_type.upper()}\n")

                        form = builder()
                        form.generate()

                        for server in self.setup.keys():
                            postman = self.local_postman if server == "local" else self.uat_postman
                            server_form_id = form.form_id[server]

                            if server_form_id and self.setup[server]["autosave_or_update"]:
                                is_success = False
                                if not self.setup[server]["force_autosave"]:
                                    is_success = postman.application_update_schema(
                                        form_id=server_form_id,
                                        json=form.output_json,
                                    )

                                if self.setup[server]["force_autosave"] or not is_success:
                                    postman.application_autosave(
                                        form_id=server_form_id,
                                        json=form.output_json,
                                    )

                            if server == 'local' and self.setup['local']["pdf"] and form.json_type == "application":
                                postman.application_pdf(
                                    output_path=form.prepare_output_file_path(
                                        dir_name="pdfs"
                                    ),
                                    output_file=form.prepare_output_file_name(
                                        file_type="pdf"
                                    ),
                                    json=form.output_json,
                                    form_id=server_form_id
                                )

        print(f'{"=" * 130}\n')
