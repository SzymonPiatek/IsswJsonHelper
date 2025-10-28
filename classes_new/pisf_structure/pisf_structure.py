from classes_new.additional.form_helpers import FormHelpers


class Department:
    def __init__(
            self,
            name: str,
            code: str
    ):
        self.name = name
        self.code = code

    def __str__(self):
        return f"{self.code.upper()} - {self.name}"


class OperationalProgram:
    def __init__(
            self,
            name: str,
            num: int,
            department: Department
    ):
        self.name = name
        self.num = num
        self.roman_num = FormHelpers.int_to_roman(num)
        self.department = department

    def __str__(self):
        return f"{self.roman_num}. {self.name}"


class Priority:
    def __init__(
            self,
            name: str,
            num: int,
            operation_program: OperationalProgram
    ):
        self.name = name
        self.num = num
        self.roman_num = FormHelpers.int_to_roman(num)
        self.operation_program = operation_program

    def __str__(self):
        return f"{self.roman_num}. {self.name}"


class Session:
    def __init__(
            self,
            num: int,
            year: int
    ):
        self.num = num
        self.roman_num = FormHelpers.int_to_roman(num)
        self.year = year

    def __str__(self):
        return f"Sesja {self.roman_num}/{self.year}"
