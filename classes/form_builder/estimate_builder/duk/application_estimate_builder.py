from classes.form_builder.estimate_builder.application_estimate_builder import ApplicationEstimateBuilder


class DUKApplicationEstimateBuilder(ApplicationEstimateBuilder):
    def __init__(self, data):
        super().__init__()

        self.data = data

    def generate(self):
        # Container
        full_chapter = self.create_chapter()

        sections = self.data["sections"]
        section_structure = self.data["section_structure"]

        sum_costs = []

        for section in sections:
            # Full section chapter
            full_section_chapter = self.create_chapter(
                title=section["title"],
            )

            for cost in section["costs"]:
                if cost.get('isSum', False):
                    sum_costs.append(cost["name"])

                # Section chapter
                section_chapter = self.create_chapter(
                    title=cost["title"],
                )

                for structure in section_structure:
                    component = self.create_component(
                        component_type='text',
                        mask='fund',
                        label=structure.get('label', ''),
                        name=cost.get('name', '')+structure.get('name', ''),
                        value=0,
                        unit='PLN'
                    )
                    section_chapter["components"].append(component)

                full_section_chapter["components"].append(section_chapter)

            full_chapter["components"].append(full_section_chapter)

        return full_chapter
