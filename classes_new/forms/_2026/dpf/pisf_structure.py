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


class FilmProjectDevelopmentPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Rozwój projektów filmowych",
            num=1,
            operation_program=ProductionOperationalProgram()
        )


class FeaturedFilmProductionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Produkcja filmów fabularnych",
            num=2,
            operation_program=ProductionOperationalProgram()
        )


class DebutsFeaturedFilmProductionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Produkcja filmów fabularnych pełnometrażowych - DEBIUTY",
            num=3,
            operation_program=ProductionOperationalProgram()
        )


class DocumentaryFilmProductionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Produkcja filmów dokumentalnych",
            num=4,
            operation_program=ProductionOperationalProgram()
        )


class AnimatedFilmProductionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Produkcja filmów animowanych",
            num=5,
            operation_program=ProductionOperationalProgram()
        )


class FamilyFilmProductionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Produkcja filmów kina familijnego",
            num=6,
            operation_program=ProductionOperationalProgram()
        )


class InternationalMinorityCoProductionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Produkcja filmów w koprodukcji międzynarodowej mniejszościowej",
            num=7,
            operation_program=ProductionOperationalProgram()
        )



class InternationalMinorityCoPostproductionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Postprodukcja filmów w koprodukcji międzynarodowej mniejszościowej",
            num=8,
            operation_program=ProductionOperationalProgram()
        )



class PolishGermanFilmFundPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Polsko-Niemiecki Fundusz Filmowy",
            num=9,
            operation_program=ProductionOperationalProgram()
        )


class ScreenplayScholarshipPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Stypendia scenariuszowe",
            num=10,
            operation_program=ProductionOperationalProgram()
        )


class IntentLetterFilmProductionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="List intencyjny PISF na produkcję filmów",
            num=11,
            operation_program=ProductionOperationalProgram()
        )
