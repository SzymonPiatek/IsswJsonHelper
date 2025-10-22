from classes_new.pisf_structure import Department, OperationalProgram, Priority


class DWMDepartment(Department):
    def __init__(self):
        super().__init__(
            name="Dział Współpracy Międzynarodowej",
            code="DWM"
        )


class PromotionOperationalProgram(OperationalProgram):
    def __init__(self):
        super().__init__(
            name="Promocja Polskiego Filmu za granicą",
            num=5,
            department=DWMDepartment()
        )


class PromotionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Promocja Polskiego Filmu za granicą",
            num=1,
            operation_program=PromotionOperationalProgram()
        )
