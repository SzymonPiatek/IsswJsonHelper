from classes_new.pisf_structure import Department, OperationalProgram, Priority


class DPFDepartment(Department):
    def __init__(self):
        super().__init__(
            name="Dział Produkcji Filmowej",
            code="DPF"
        )


class ProductionOperationalProgram(OperationalProgram):
    def __init__(self):
        super().__init__(
            name="Produkcja filmowa",
            num=1,
            department=DPFDepartment()
        )


class ScreenplayScholarshipPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Stypendia scenariuszowe",
            num=1,
            operation_program=ProductionOperationalProgram()
        )
