from dotenv import load_dotenv
import os
import json
from pathlib import Path
from classes_new.postman.postman import Postman
from classes_new.forms._2026.forms import Forms2026


class FormHelper:
    def __init__(
            self,
            year: int = 2026,
            setup: dict = None
    ):
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

        self.setup = setup

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
        self.postman = {
            "local": self.local_postman,
            "uat": self.uat_postman
        }

        self.forms_index: list[dict] = []

    def generate_jsons(self):
        for data_type in self.forms.builder_map.keys():
            if data_type not in {"application", "report"}:
                raise ValueError(f"Nieobsługiwany typ formularza: {data_type}")

            for department, programs in self.forms.builder_map.get(data_type, {}).items():
                if isinstance(programs, dict) and programs.get("skip", False):
                    continue

                for program, priorities in programs.items():
                    if program == "skip":
                        continue

                    for priority, builder in priorities.items():
                        if priority == "skip":
                            continue

                        if builder:
                            form = builder()

                            print(f'{"=" * 50}')
                            if form.priority is not None:
                                print(f"DP: {str(form.priority.operation_program.department)}")
                                print(f"PO: {str(form.priority.operation_program)}")
                                print(f"PR: {str(form.priority)}")
                                print(f"JT: {form.json_type.title()} - {form.session}")
                                print(f"{'-' * 50}")
                            else:
                                print(f"[{department.upper()}] {program.upper()} {priority.upper()} - {data_type.upper()}\n")

                            for server in self.setup.keys():
                                postman = self.postman[server]
                                server_form_id = form.form_id[server]

                                if server_form_id:
                                    form_url = f"{postman.base_url}/{'wniosek' if form.json_type == 'application' else 'raport'}/{server_form_id}"

                                    self.forms_index.append({
                                        "name": f"{program.upper()} {priority.upper()}",
                                        "json_type": form.json_type,
                                        "server": server,
                                        "url": form_url
                                    })

                                if self.setup[server][form.json_type]["json"]:
                                    form.generate()

                                if server_form_id and self.setup[server][form.json_type]["autosave_or_update"]:
                                    is_success = False

                                    if not self.setup[server][form.json_type]["force_autosave"]:
                                        is_success = postman.form_update_schema(
                                            form_id=server_form_id,
                                            json=form,
                                        )

                                    if self.setup[server][form.json_type]["force_autosave"] or not is_success:
                                        postman.form_autosave(
                                            form_id=server_form_id,
                                            json=form,
                                        )

                                if server == 'local' and self.setup['local'][form.json_type]["pdf"]:
                                    postman.form_pdf(
                                        output_path=form.prepare_output_file_path(
                                            dir_name='pdfs'
                                        ),
                                        output_file=form.prepare_output_file_name(
                                            file_type="pdf"
                                        ),
                                        json_type=form.json_type,
                                        form_id=server_form_id
                                    )

        self.save_forms_index()

    def save_forms_index(self):
        output_path = Path("./output")
        output_path.mkdir(parents=True, exist_ok=True)

        output_file = output_path / "forms_index.json"

        grouped = {}

        for entry in self.forms_index:
            key = entry["name"]
            if key not in grouped:
                grouped[key] = {}

            grouped[key][entry["json_type"]] = {
                entry["server"]: f"{entry["url"]}/edycja?version=-1",
            }

        with output_file.open("w", encoding="utf-8") as f:
            json.dump(grouped, f, ensure_ascii=False, indent=2)

        print(f"\n📄 Utworzono index formularzy: {output_file.resolve()}")

