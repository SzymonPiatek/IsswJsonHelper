from .estimate_data import estimate_section_structure, sum_estimate_section_structure, \
    sum_estimate_sections
from classes.form_factory.form_factory import FormFactory


class ReconstructionApplicationEstimateBuilder(FormFactory):
    def __init__(self, estimate_sections: list, after_name: str = '', estimate_section_structure: list = estimate_section_structure):
        super().__init__()


        self.estimate_section_structure = estimate_section_structure
        self.estimate_sections = estimate_sections
        self.data = self.convert_data()
        self.after_name = after_name

    def convert_data(self):
        return {
            'chapters': {
                'estimate': {
                    'section': self.estimate_sections,
                    'section_structure': self.estimate_section_structure,
                    'section_construct': {
                        'chapter_title': {
                            'classList': {
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
                                    "grid-cols-3"
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
                    'section': sum_estimate_sections,
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

    def get_chapter_data(self, data):
        sections = data["section"]
        structure = data["section_structure"]
        construct = data["section_construct"]

        return sections, structure, construct

    def generate_estimate(self):
        estimate = self.data['chapters']['estimate']
        sum_estimate = self.data['chapters']['sum_estimate']

        estimate_sections, section_structure, section_construct = self.get_chapter_data(data=estimate)
        sum_estimate_sections, sum_estimate_structure, sum_construct = self.get_chapter_data(data=sum_estimate)

        all_cost_names = []
        for section in estimate_sections:
            for cost in section.get('costs', []):
                all_cost_names.append(cost.get('name', ''))

        return self.create_chapter(
            components=[
                *[
                    self.build_section_chapter(
                        section,
                        section_structure,
                        section_construct,
                        title=f"{self.helpers.int_to_roman(idx)}. {section.get('title', '')}"
                    )
                    for idx, section in enumerate(estimate_sections, start=1)
                ],
                self.build_summary_chapter(sum_estimate_sections[0], sum_estimate_structure, sum_construct,
                                           all_cost_names)
            ]
        )

    def generate_estimate_top(self):
        return self.create_chapter(
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="text",
                            label='Nazwa przedsięwzięcia',
                            name='applicationTaskNameRepeat',
                            calculation_rules=[
                                {
                                    "name": "copyValue",
                                    "from": "applicationTaskName"
                                }
                            ],
                            read_only=True,
                            required=True,
                        ),
                        self.create_component(
                            component_type="radio",
                            name="isVatPayer",
                            label="Status wnioskodawcy w zakresie podatku VAT:",
                            help_text="W przypadku wynagrodzeń rozliczanych listą płac lub rachunkiem do umowy o dzieło lub umowy zlecenie należy wykazać kwotą brutto z uwzględnieniem narzutów ZUS pracodawcy.",
                            options=[
                                "Wnioskodawca jest czynnym podatnikiem VAT i ma prawo do odliczenia podatku VAT od wydatków ponoszonych w ramach przedsięwzięcia. Wydatki będą rozliczane w kwotach netto.",
                                "Wnioskodawca jest czynnym podatnikiem VAT, ale nie ma możliwości odliczenia podatku VAT w odniesieniu do wydatków ponoszonych w ramach przedsięwzięcia. Wydatki będą rozliczane w kwotach brutto.",
                                "Wnioskodawca nie jest podatnikiem VAT. Wydatki będą rozliczane w kwotach brutto."
                            ]
                        )
                    ]
                )
            ]
        )

    def generate_estimate_bottom(self):
        return self.create_chapter(
            title="Uwaga! <br /><small>Koszt jest kwalifikowany jeżeli spełnia następujące kryteria: <normal><br />- został/zostanie poniesiony w okresie realizacji przedsięwzięcia określonym w harmonogramie, jednak nie wcześniej niż od daty rozpoczęcia naboru wniosków w sesji, <br />- jest celowy, tj. został/zostanie poniesiony w związku z realizacją przedsięwzięcia, na które została przyznana dotacja, <br />- jest rzetelnie udokumentowany i możliwy do zweryfikowania, <br />- jest zgodny z obowiązującymi przepisami prawa. </normal></small>"
        )

    def build_calculations_and_validators(self, structure: dict, name: str, is_sum: bool = False, sub_fields=None):
        rules = []
        validators = []

        if structure["name"] == "CostTotal":
            cost_single_field = f"{name}CostSingle{self.after_name}"
            amount_field = f"{name}Amount{self.after_name}"
            rules.append(
                self.calculation_rule.multiply_inputs(fields=[cost_single_field, amount_field])
            )
            validators.append(
                self.validator.related_multiplication_validator(field_names=[cost_single_field, amount_field])
            )

        elif "sumFields" in structure:
            fields = [f"{name}{field}{self.after_name}" for field in structure["sumFields"]]
            rules.append(self.calculation_rule.dynamic_sum_inputs(fields=fields))
            validators.append(self.validator.related_sum_validator(field_names=fields))
        elif structure.get("isShare"):
            dividend = f"{structure["dividend"]}{self.after_name}"
            divisor = f"{structure["divisor"]}{self.after_name}"
            rules.append(
                self.calculation_rule.share_calculator(
                    dividend_field=dividend,
                    divisor_field=divisor,
                )
            )
            validators.append(
                self.validator.related_share_validator(
                    dividend=dividend,
                    divisor=divisor,
                )
            )
        elif is_sum and sub_fields:
            rules.append(
                self.calculation_rule.dynamic_sum_inputs(fields=sub_fields)
            )
            validators.append(self.validator.related_sum_validator(field_names=sub_fields))

        return rules, validators

    def build_component(self, name, label, structure, is_sum=False, sub_fields=None, field_overrides=None):
        field_overrides = field_overrides.copy() if field_overrides else {}

        rules, validators = self.build_calculations_and_validators(structure, name, is_sum, sub_fields)

        field_overrides.setdefault("calculationRules", []).extend(rules)
        field_overrides.setdefault("validators", []).extend(validators)

        component = self.create_component(
            component_type="text",
            mask="fund",
            label=label,
            name=f"{name}{structure['name']}{self.after_name}",
            unit=structure.get("unit", "PLN"),
            read_only=True if structure.get("isShare") else structure.get("readOnly", True if is_sum and sub_fields else False),
        )

        for key in ("validators", "calculationRules", "readOnly", "required"):
            if key in field_overrides:
                if isinstance(field_overrides[key], list):
                    component.setdefault(key, []).extend(field_overrides[key])
                else:
                    component[key] = field_overrides[key]

        return component

    def build_section_chapter(self, section, section_structure, construct, title):
        costs = section.get("costs", [])
        components = []
        section_index = 0

        for cost in costs:
            section_index += 1
            cost_components = []

            for structure in section_structure:
                field_name = f"{cost['name']}{structure['name']}{self.after_name}"
                is_sum = cost.get("isSum", False)

                sub_fields = [
                    f"{sub['name']}{structure['name']}{self.after_name}"
                    for sub in costs if not sub.get("isSum")
                ]

                override = cost.get("overrides", {}).get(structure["name"], {})
                rules, validators = self.build_calculations_and_validators(
                    structure, cost["name"], is_sum, sub_fields if is_sum else None
                )

                component_type = override.get("type", structure.get("type", "text"))
                options = override.get("options", structure.get("options", [] if component_type in ["select", "radio"] else None))

                component = self.create_component(
                    component_type=override.get("type", structure.get("type", "text")),
                    mask=override.get("mask", structure.get("mask")),
                    label=structure["label"],
                    name=field_name,
                    unit=override.get("unit", structure.get("unit", "")),
                    read_only=override.get("readOnly", structure.get("readOnly", is_sum)),
                    options=options,
                    calculation_rules=override.get("calculationRules", []) + rules,
                    validators=override.get("validators", []) + validators,
                )

                component["dataBDD"] = f"{cost['name']}-{structure['name'].lower()}"
                cost_components.append(component)

            single_cost_chapter = self.create_chapter(
                title="",
                class_list=construct["section_title"].get("classList", {}),
                components=cost_components
            )

            full_cost_chapter = self.create_chapter(
                title=f"{section_index}. {cost['title']}",
                class_list={
                    "sub": construct["chapter_title"]["classList"]["sub"]
                },
                components=[single_cost_chapter],
                help_text=cost.get("helpText", '')
            )

            components.append(full_cost_chapter)

        title = f'<p style="color: #e00d1d">{title}<p>'

        # np. Etap I
        final_chapter = self.create_chapter(
            title=title,
            components=components,
            class_list=construct["chapter_title"]["classList"],
            help_text=section.get("helpText", '')
        )

        return final_chapter

    def build_summary_chapter(self, section, structure_list, construct, all_costs):
        components = []

        for structure in structure_list:
            name = structure["name"]

            if name == "SumAmount":
                field_to_sum = "CostTotal"
            else:
                field_to_sum = name

            sub_fields = [
                f"{cost}{field_to_sum}{self.after_name}" for cost in all_costs
            ]

            for cost in section["costs"]:
                components.append(
                    self.build_component(
                        name=cost["name"],
                        label=structure["label"],
                        structure=structure,
                        is_sum=True,
                        sub_fields=sub_fields
                    )
                )

        return self.create_chapter(
            title=f'<p style="color: #e00d1d">{section["title"]}</p>',
            class_list=construct["section_title"]["classList"],
            components=components
        )
