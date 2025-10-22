from classes_new.form_helper.form_helper import FormHelper


def main():
    form_helper = FormHelper(year=2026)
    form_helper.generate_jsons(data_type="application")


if __name__ == '__main__':
    main()
