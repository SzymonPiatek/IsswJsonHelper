from classes.form_components import DWMComponent, DWMSection
from classes.pisf_structure.department import Department


class DWMDepartment(Department):
    DEPARTMENT_NAME = 'DWM'

    def __init__(self):
        super().__init__()

        self.section = DWMSection()
        self.component = DWMComponent()
