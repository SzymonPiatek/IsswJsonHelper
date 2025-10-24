import time
from classes_new.form_helper.form_helper import FormHelper


def main():
    start_time = time.time()

    form_helper = FormHelper(year=2026)
    form_helper.generate_jsons(data_type="application")
    form_helper.generate_jsons(data_type="report")

    end_time = time.time()
    elapsed = end_time - start_time

    print(f"Time elapsed: {elapsed:.2f} seconds")


if __name__ == '__main__':
    main()
