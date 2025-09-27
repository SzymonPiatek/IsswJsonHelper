from classes.form_helper.form_helper import FormHelper


def main():
    helper = FormHelper(year="2026")
    # helper.generate_process("application")
    helper.generate_process("report")


if __name__ == '__main__':
    main()
