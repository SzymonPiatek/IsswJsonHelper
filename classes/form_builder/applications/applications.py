class Applications:
    def __init__(self):
        self.builder_map = None

    def get_application_builder(self, department: str, program: str, priority: str):
        try:
            return self.builder_map[department][program][priority]
        except KeyError:
            raise ValueError(f"Nieobsługiwany wariant: {department}.{program}.{priority}")

