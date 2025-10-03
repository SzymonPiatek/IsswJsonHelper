from classes.form_components import DUKSection
from classes.pisf_structure.department import Department


class DUKDepartment(Department):
    DEPARTMENT_NAME = 'DUK'

    def __init__(self):
        super().__init__()

        self.section = DUKSection()
