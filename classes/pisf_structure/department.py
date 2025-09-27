from typing import Literal, ClassVar
from classes.form_builder.form_builder import FormBuilder


DepartmentType = Literal['DPF', 'DUK', 'DWM', 'ZACHĘTY']


class Department(FormBuilder):
    DEPARTMENT_NAME: ClassVar[DepartmentType]

    def __init__(self):
        super().__init__()
