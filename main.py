import time
from classes.form_helper.form_helper import FormHelper


def main():
    start_time = time.time()

    helper = FormHelper(year="2026")
    helper.generate_process("application")
    # helper.generate_process("report")

    end_time = time.time()
    elapsed = end_time - start_time
    helper.scraper.close()

    print(f"Time elapsed: {elapsed:.2f} seconds")


if __name__ == '__main__':
    main()
