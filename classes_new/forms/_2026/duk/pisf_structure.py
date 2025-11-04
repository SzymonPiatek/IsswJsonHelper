from classes_new.pisf_structure import Department, OperationalProgram, Priority


class DUKDepartment(Department):
    def __init__(self):
        super().__init__(
            name="Dział Upowszechniania Kultury Filmowej",
            code="DUK"
        )


class EducationOperationalProgram(OperationalProgram):
    def __init__(self):
        super().__init__(
            name="Edukacja filmowa",
            num=2,
            department=DUKDepartment()
        )


class HigherSchoolsPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Szkoły wyższe",
            num=1,
            operation_program=EducationOperationalProgram()
        )


class SecondarySchoolsPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Szkoły średnie i zawodowe",
            num=2,
            operation_program=EducationOperationalProgram()
        )


class ProfessionalTrainingPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Edukacja profesjonalna i doskonalenie zawodowe",
            num=3,
            operation_program=EducationOperationalProgram()
        )


class AudiencePriority(Priority):
    def __init__(self):
        super().__init__(
            name="Edukacja widowni filmowej",
            num=4,
            operation_program=EducationOperationalProgram()
        )


class DisseminationOperationalProgram(OperationalProgram):
    def __init__(self):
        super().__init__(
            name="Upowszechnianie kultury filmowej",
            num=3,
            department=DUKDepartment()
        )


class FestivalsPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Festiwale filmowe",
            num=1,
            operation_program=DisseminationOperationalProgram()
        )


class InitiativesPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Inicjatywy filmowe",
            num=2,
            operation_program=DisseminationOperationalProgram()
        )


class LiteraturePriority(Priority):
    def __init__(self):
        super().__init__(
            name="Działalność wydawnicza",
            num=3,
            operation_program=DisseminationOperationalProgram()
        )


class ReconstructionPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Rekontrukcja filmowa",
            num=4,
            operation_program=DisseminationOperationalProgram()
        )


class ResearchPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Badania rynku audiowizualnego",
            num=5,
            operation_program=DisseminationOperationalProgram()
        )


class DkfPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Działalność klubów filmowych",
            num=6,
            operation_program=DisseminationOperationalProgram()
        )


class DevelopmentOperationalProgram(OperationalProgram):
    def __init__(self):
        super().__init__(
            name="Rozwój kin",
            num=4,
            department=DUKDepartment()
        )


class ModernizationPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Modernizacja kin",
            num=1,
            operation_program=DevelopmentOperationalProgram()
        )


class DigitalizationPriority(Priority):
    def __init__(self):
        super().__init__(
            name="Cyfryzacja kin",
            num=2,
            operation_program=DevelopmentOperationalProgram()
        )
