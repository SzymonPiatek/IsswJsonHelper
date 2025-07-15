from classes.form_builder.form_builder_base import FormBuilderBase


class DUKApplicationEstimateBuilder(FormBuilderBase):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def build_component(self, name, label, structure, is_sum=False, sub_fields=None):
        component = self.create_component(
            component_type="text" if not structure.get("isShare") else "number",
            mask="fund" if not structure.get("isShare") else None,
            label=label,
            name=f"{name}{structure['name']}",
            value=0,
            unit=structure.get("unit", "PLN"),
            read_only=structure.get("readOnly", is_sum),
        )

        if is_sum and sub_fields:
            component["calculationRules"] = [{
                "name": "sumInputs",
                "kwargs": {"fields": sub_fields}
            }]
            component["validators"] = [{
                "name": "RelatedSumValidator",
                "kwargs": {"field_names": sub_fields}
            }]
        elif structure.get("isShare"):
            component["calculationRules"] = [{
                "name": "shareCalculator",
                "kwargs": {
                    "dividendField": structure["dividend"],
                    "divisorField": structure["divisor"]
                }
            }]
            component["validators"] = [{
                "name": "RelatedShareValidator",
                "kwargs": {
                    "dividend": structure["dividend"],
                    "divisor": structure["divisor"]
                }
            }]

        return component

    def build_section_chapter(self, section, section_structure, construct):
        costs = section["costs"]
        components = []

        for cost in costs:
            is_sum = cost.get("isSum", False)
            cost_components = []
            for structure in section_structure:
                sub_fields = [f"{sub['name']}{structure['name']}" for sub in costs if not sub.get("isSum")]
                cost_components.append(
                    self.build_component(
                        cost["name"],
                        structure["label"],
                        structure,
                        is_sum,
                        sub_fields if is_sum else None
                    )
                )

            components.append({
                "kind": "chapter",
                "title": cost["title"],
                "classList": construct["section_title"]["classList"],
                "components": cost_components
            })

        return {
            "kind": "chapter",
            "title": section["title"],
            "classList": construct["chapter_title"]["classList"],
            "components": components
        }

    def build_summary_chapter(self, section, structure_list, construct, all_costs):
        components = [
            self.build_component(
                name=cost["name"],
                label=structure["label"],
                structure=structure,
                is_sum=True,
                sub_fields=[f"{c}{structure['name']}" for c in all_costs])
            for structure in structure_list
            for cost in section["costs"]
        ]

        return self.create_chapter(
            title=section["title"],
            class_list=construct["section_title"]["classList"],
            components=components
        )

    def get_chapter_data(self, data):
        sections = data["sections"]
        structure = data["section_structure"]
        construct = data["section_construct"]

        return sections, structure, construct

    def generate_estimate(self):
        estimate = self.data['chapters']['estimate']
        sum_estimate = self.data['chapters']['sum_estimate']

        estimate_sections, section_structure, section_construct = self.get_chapter_data(data=estimate)
        sum_estimate_sections, sum_estimate_structure, sum_construct = self.get_chapter_data(data=sum_estimate)

        all_cost_names = [cost["name"] for section in estimate_sections for cost in section["costs"] if cost.get("isSum")]

        full_chapter = self.create_chapter(
            title="Koszty z podziałem na źródło finansowania",
            components=[
                self.build_section_chapter(section, section_structure, section_construct)
                for section in estimate_sections
            ] + [
                self.build_summary_chapter(sum_estimate_sections[0], sum_estimate_structure, sum_construct, all_cost_names)
            ]
        )

        return full_chapter

    def generate_estimate_top(self):
        return self.create_chapter(
            components=[
                self.create_component(
                    component_type="text",
                    label='Nazwa przedsięwzięcia',
                    name='projectNameRepeat',
                    calculation_rules=[
                        {
                            "name": "copyValue",
                            "from": "applicationTaskName"
                        }
                    ],
                    validators=[
                        {
                            "name": "RequiredValidator"
                        }
                    ],
                    read_only=True,
                    required=True,
                ),
                self.create_component(
                    component_type='radio',
                    label='Wszystkie kwoty zaznaczone w kosztorysie są kwotami (w przypadku kosztów wynagrodzeń rozliczanych listą płac lub rachunkiem do umowy o dzieło/zlecenie należy wykazać kwotę brutto z uwzględnieniem narzutów ZUS pracodawcy)',
                    name='isVatPayer',
                    value=False,
                    options=[
                        "netto (zaznacza Wnioskodawca, który jest podatnikiem VAT)",
                        "brutto (zaznacza Wnioskodawca, który NIE jest podatnikiem VAT)"
                    ],
                    validators=[
                        {
                            "name": "ExactValidator",
                            "kwargs": {
                                "values": [
                                    "netto (zaznacza Wnioskodawca, który jest podatnikiem VAT)",
                                    "brutto (zaznacza Wnioskodawca, który NIE jest podatnikiem VAT)"
                                ]
                            }
                        }
                    ]

                )
            ]
        )

    def generate_estimate_bottom(self):
        return self.create_chapter(
            title="Uwaga! <br /><small>Koszt jest kwalifikowany jeżeli spełnia następujące kryteria: <normal><br />- został/zostanie poniesiony w okresie realizacji przedsięwzięcia określonym w harmonogramie, jednak nie wcześniej niż od daty rozpoczęcia naboru wniosków w sesji, <br />- jest celowy, tj. został/zostanie poniesiony w związku z realizacją przedsięwzięcia, na które została przyznana dotacja, <br />- jest rzetelnie udokumentowany i możliwy do zweryfikowania, <br />- jest zgodny z obowiązującymi przepisami prawa. </normal></small>"
        )

    def generate(self):
        return self.create_part(
            title='VII. Kosztorys przedsięwzięcia',
            short_name='VII. Kosztorys przedsięwzięcia',
            chapters=[
                self.generate_estimate_top(),
                self.generate_estimate(),
                self.generate_estimate_bottom()
            ]
        )
