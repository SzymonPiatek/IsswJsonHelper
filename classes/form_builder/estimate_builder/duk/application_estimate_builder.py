from classes.form_builder.estimate_builder.application_estimate_builder import ApplicationEstimateBuilder


class DUKApplicationEstimateBuilder(ApplicationEstimateBuilder):
    def __init__(self, data):
        super().__init__()

        self.data = data

    def generate(self):
        sections = self.data["sections"]
        section_structure = self.data["section_structure"]
        section_construct = self.data["section_construct"]

        sum_costs = [
            cost["name"]
            for section in sections
            for cost in section["costs"]
            if cost.get("isSum")
        ]

        full_chapter = self.create_chapter(
            components=[
                self.create_chapter(
                    title=section["title"],
                    class_list=section_construct['chapter_title']["classList"],
                    components=[
                        self.create_chapter(
                            title=cost["title"],
                            class_list=section_construct['section_title']["classList"],
                            components=[
                                self.create_component(
                                    component_type='text',
                                    mask='fund',
                                    label=structure["label"],
                                    name=cost["name"]+structure["name"],
                                    value=0,
                                    unit='PLN'
                                ) for structure in section_structure
                            ]
                        ) for cost in section["costs"]
                    ]
                ) for section in sections
            ]
        )

        sum_chapter = self.create_chapter(
            title="Podsumowanie",
            components=[
                self.create_component(
                    component_type='text',
                    mask='fund',
                    label=structure["label"],
                    name=f'total{structure["name"]}',
                    calculation_rules=[
                        {
                            "name": "sumInputs",
                            "kwargs": {
                                "fields": [
                                    [f'{sum_cost}{structure["name"]}' for sum_cost in sum_costs]
                                ]
                            }
                        }
                    ],
                    validators=[
                        {
                            "name": "RelatedSumValidator",
                            "kwargs": {
                                "field_names": [
                                    [f'{sum_cost}{structure["name"]}' for sum_cost in sum_costs]
                                ]
                            }
                        }
                    ],
                    read_only=True
                ) for structure in section_structure
            ]
        )

        full_chapter["components"].append(sum_chapter)

        return full_chapter
