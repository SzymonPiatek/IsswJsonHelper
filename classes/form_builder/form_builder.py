from typing import Literal, ClassVar

JSONType = Literal['application', 'report']

DepartmentType = Literal['DPF', 'DUK', 'DWM']

SessionType = Literal['I', 'II', 'III', 'IV']

class FormBuilder:
    JSON_TYPE: ClassVar[JSONType]
    DEPARTMENT_NAME: ClassVar[DepartmentType]
    OPERATION_NAME: str
    PRIORITY_NAME: str
    YEAR: int
    SESSION: ClassVar[SessionType]

    def __init__(self) -> None:
        self.json_type = self.JSON_TYPE
        self.department_name = self.DEPARTMENT_NAME
        self.operation_name = self.OPERATION_NAME
        self.priority_name = self.PRIORITY_NAME
        self.year = self.YEAR
        self.session = self.SESSION

    def info(self):
        return f'''
        Type: {'Wniosek' if self.json_type == 'application' else 'Raport'}
        Department: {self.department_name}
        Operation: {self.operation_name}
        Priority: {self.priority_name}
        Year: {self.year}
        Session: {self.session}
        '''

    def generate(self):
        print('generate')