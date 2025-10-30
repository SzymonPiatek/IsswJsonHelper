import time
from classes_new.form_helper.form_helper import FormHelper


def main():
    start_time = time.time()

    form_helper = FormHelper(
        year=2026,
        setup={
            "uat": {
                "application": {
                    "json": False,
                    "autosave_or_update": False,
                    "force_autosave": False,
                    "pdf": False,
                },
                "report": {
                    "json": False,
                    "autosave_or_update": False,
                    "force_autosave": False,
                    "pdf": False,
                }
            },
            "local": {
                "application": {
                    "json": True,
                    "autosave_or_update": True,
                    "force_autosave": True,
                    "pdf": True,
                },
                "report": {
                    "json": True,
                    "autosave_or_update": True,
                    "force_autosave": False,
                    "pdf": True,
                }
            }
        }
    )
    # form_helper.generate_jsons(data_type="application")
    form_helper.generate_jsons(data_type="report")

    end_time = time.time()
    elapsed = end_time - start_time

    print(f"\nTime elapsed: {elapsed:.2f} seconds")


if __name__ == '__main__':
    main()
