from classes.form_builder.additional.components.component.dwm.dwm_component import DWMComponent
from classes.form_builder.pisf_structure.department import Department
from classes.form_builder.additional.components.section.dwm.dwm_section import DWMSection


class DWMDepartment(Department):
    DEPARTMENT_NAME = 'DWM'

    def __init__(self):
        super().__init__()

        self.section = DWMSection()
        self.component = DWMComponent()
