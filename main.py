import subprocess
from generators import dpf, duk, dwm


def main():
    for department in [dpf, duk, dwm]:
        department.generate_applications()
        department.generate_reports()

    subprocess.run(["python", "scripts/delete_unused_args.py"], check=True)


if __name__ == '__main__':
    main()
