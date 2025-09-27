from typing import ClassVar
from classes.form_builder.form_builder import FormBuilder
from classes.types import DepartmentType


class Department(FormBuilder):
    DEPARTMENT_NAME: ClassVar[DepartmentType]

    def __init__(self):
        super().__init__()
