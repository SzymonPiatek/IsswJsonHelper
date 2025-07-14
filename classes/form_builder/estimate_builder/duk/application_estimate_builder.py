from classes.form_builder.estimate_builder.application_estimate_builder import ApplicationEstimateBuilder


class DUKApplicationEstimateBuilder(ApplicationEstimateBuilder):
    def __init__(self, data):
        super().__init__()

        self.data = data

    def generate(self):
        chapters = self.data['chapters']

        # Estimate
        estimate = chapters['estimate']
        estimate_sections = estimate["sections"]
        estimate_section_structure = estimate["section_structure"]
        estimate_section_construct = estimate["section_construct"]

        # Sum Estimate
        sum_estimate = chapters['sum_estimate']
        sum_estimate_sections = sum_estimate["sections"]
        sum_estimate_section_structure = sum_estimate["section_structure"]
        sum_estimate_section_construct = sum_estimate["section_construct"]

        # Vault
        sum_costs = [
            cost["name"]
            for section in estimate_sections
            for cost in section["costs"]
            if cost.get("isSum")
        ]

        # Containter
        full_chapter = self.create_chapter()

        # Estimate
        estimate_chapter = self.create_chapter(
            components=[
                self.create_chapter(
                    title=section["title"],
                    class_list=estimate_section_construct['chapter_title']["classList"],
                    components=[
                        self.create_chapter(
                            title=cost["title"],
                            class_list=estimate_section_construct['section_title']["classList"],
                            components=[
                                self.create_component(
                                    component_type='text',
                                    mask='fund',
                                    label=structure["label"],
                                    name=cost["name"]+structure["name"],
                                    value=0,
                                    unit='PLN',
                                    read_only=cost.get("readOnly", False)
                                ) for structure in estimate_section_structure
                            ]
                        ) for cost in section["costs"]
                    ]
                ) for section in estimate_sections
            ]
        )
        full_chapter["components"].append(estimate_chapter)

        # Sum estimate
        sum_estimate_chapter = self.create_chapter(
            title=sum_estimate_sections[0]['title'],
            class_list=sum_estimate_section_construct["section_title"]['classList'],
            components=[
                self.create_component(
                    component_type='text',
                    mask='fund',
                    label=structure["label"],
                    name=f'{sum_estimate_sections[0]['costs'][0]['name']}{structure["name"]}',
                    unit=structure["unit"],
                    calculation_rules=[
                        {
                            "name": "sumInputs",
                            "kwargs": {
                                "fields": [
                                    [f'{sum_cost}{structure["name"]}' for sum_cost in sum_costs]
                                ]
                            }
                        } if structure.get('isSum', False) else {
                            "name": "shareCalculator",
                            "kwargs": {
                                "dividendField": structure["dividend"],
                                "divisorField": structure["divisor"]
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
                        } if structure.get('isSum', False) else {
                            "name": "RelatedShareValidator",
                            "kwargs": {
                                "dividend": structure["dividend"],
                                "divisor": structure["divisor"]
                            }
                        }
                    ],
                    read_only=True
                ) for structure in sum_estimate_section_structure
            ]
        )
        full_chapter["components"].append(sum_estimate_chapter)

        return full_chapter
