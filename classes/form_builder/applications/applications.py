class Applications:
    def __init__(self):
        self.builder_map = None

    def get_builder(self, data_type: str, department: str, program: str, priority: str):
        if data_type == "application" or data_type == "report":
            try:
                return self.builder_map[data_type][department][program][priority]
            except KeyError:
                raise ValueError(f"Nieobsługiwany wariant: applications.{department}.{program}.{priority}")
        else:
            raise ValueError(f"Nie obsługiwany typ formularza: {data_type}")

    def get_application_builder(self, department: str, program: str, priority: str):
        return self.get_builder(data_type="application", department=department, program=program, priority=priority)

    def get_report_builder(self, department: str, program: str, priority: str):
        return self.get_builder(data_type="report", department=department, program=program, priority=priority)
