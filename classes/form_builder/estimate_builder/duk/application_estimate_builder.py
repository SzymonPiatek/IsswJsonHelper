from classes.form_builder.form_builder_base import FormBuilderBase
from classes.form_builder.duk.estimate_data import estimate_section_structure, sum_estimate_section_structure, sum_estimate_sections


class DUKApplicationEstimateBuilder(FormBuilderBase):
    def __init__(self, estimate_sections):
        super().__init__()
        self.data = self.convert_data(estimate_sections=estimate_sections)

    def convert_data(self, estimate_sections):
        return {
            'chapters': {
                'estimate': {
                    'sections': estimate_sections,
                    'section_structure': estimate_section_structure,
                    'section_construct': {
                        'chapter_title': {
                            'classList': {
                                "main": [
                                    "no-title"
                                ],
                                "sub": [
                                    "table-1-2-top",
                                ]
                            }
                        },
                        'section_title': {
                            "classList": {
                                "main": [
                                    "table-1-3-narrow",
                                    "grid",
                                    "grid-cols-5",
                                    "no-title"
                                ],
                                "sub": [
                                    "table-1-3__col"
                                ]
                            }
                        },
                        'cost': {
                            'classList': [
                                "no-label"
                            ]
                        },
                        'cost_desc': {
                            'classList': [
                                "col-span-2",
                                "displayNoneFrontend",
                                "full-width",
                                "no-label"
                            ]
                        }
                    }
                },
                'sum_estimate': {
                    'sections': sum_estimate_sections,
                    'section_structure': sum_estimate_section_structure,
                    'section_construct': {
                        'section_title': {
                            'classList': {
                                "main": [
                                    "table-1-3-narrow",
                                    "grid",
                                    "grid-cols-3"
                                ],
                                "sub": [
                                    "table-1-3__col"
                                ]
                            }
                        }
                    }
                }
            }
        }

    def build_component(self, name, label, structure, is_sum=False, sub_fields=None, field_overrides=None):
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

        if field_overrides:
            if "validators" in field_overrides:
                component.setdefault("validators", []).extend(field_overrides["validators"])
            if "calculationRules" in field_overrides:
                component.setdefault("calculationRules", []).extend(field_overrides["calculationRules"])
            if "read_only" in field_overrides:
                component["read_only"] = field_overrides["read_only"]
            if "required" in field_overrides:
                component["required"] = field_overrides["required"]

        return component

    def build_section_chapter(self, section, section_structure, construct):
        costs = section["costs"]
        components = []

        for cost in costs:
            is_sum = cost.get("isSum", False)
            cost_components = []

            for structure in section_structure:
                field_name = f"{cost['name']}{structure['name']}"

                # DESC
                if structure.get("isDesc", False):
                    cost_components.append(
                        self.create_component(
                            component_type="text",
                            label='',
                            name=field_name,
                            value=f'{section["title"]} - {cost["title"]}' if is_sum else cost["title"],
                            read_only=True,
                            class_list=construct["cost_desc"]["classList"]
                        )
                    )
                else:
                    sub_fields = [f"{sub['name']}{structure['name']}" for sub in costs if not sub.get("isSum")]
                    field_overrides = cost.get("overrides", {}).get(structure["name"], {})
                    component = self.build_component(
                        name=cost["name"],
                        label=structure["label"],
                        structure=structure,
                        is_sum=is_sum,
                        sub_fields=sub_fields if is_sum else None,
                        field_overrides=field_overrides
                    )
                    component["classList"] = construct["cost"]["classList"]
                    cost_components.append(component)

            components.append(
                self.create_chapter(
                    title=cost["title"],
                    class_list=construct["section_title"]["classList"],
                    components=cost_components
                )
            )

        return self.create_chapter(
            title=section["title"],
            class_list=construct["chapter_title"]["classList"],
            components=components
        )

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
                self.create_chapter(
                    class_list=[
                        "grid",
                        "grid-cols-5"
                    ],
                    components=[
                        self.create_component(
                            component_type='header',
                            name='headerComponentDesc',
                            value='Rodzaj kosztu',
                            class_list=[
                                "displayNoneFrontend",
                                "col-span-2"
                            ]
                        ),
                        self.create_component(
                            component_type='header',
                            name='headerComponentSumAmount',
                            value='Koszt ogółem',
                            class_list=[
                                "displayNoneFrontend",
                            ]
                        ),
                        self.create_component(
                            component_type='header',
                            name='headerComponentRequestedAmount',
                            value='Wnioskowana dotacja PISF',
                            class_list=[
                                "displayNoneFrontend",
                            ]
                        ),
                        self.create_component(
                            component_type='header',
                            name='headerComponentOtherFundsAmount',
                            value='Pozostałe środki',
                            class_list=[
                                "displayNoneFrontend",
                            ]
                        )
                    ]
                )
            ] + [
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
