import subprocess
from classes.generator.dpf_generator import DPFGenerator
from classes.generator.duk_generator import DUKGenerator
from classes.generator.dwm_generator import DWMGenerator


def main():
    for generator in [DPFGenerator, DUKGenerator, DWMGenerator]:
        generator().generate_applications_and_reports()

    subprocess.run(["python", "scripts/delete_unused_args.py"], check=True)


if __name__ == '__main__':
    main()
