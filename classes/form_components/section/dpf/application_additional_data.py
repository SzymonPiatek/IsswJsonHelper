from classes.form_builder.form_builder_base import FormBuilderBase


class ApplicationAdditionalData(FormBuilderBase):
    def __init__(self):
        super().__init__()

    def create_section_for_positive_decision(self, name: str):
        return self.create_chapter(
            visibility_rules=[
                self.visibility_rule.depends_on_value(
                    field_name=f"{name}DirectorDecision",
                    values=["Pozytywna"]
                )
            ],
            class_list=[
                "grid",
                "grid-cols-4"
            ],
            components=[
                self.create_component(
                    component_type="text",
                    label="Tytuł projektu",
                    name=f"{name}ProjectTitle",
                    class_list=[
                        "col-start-1",
                        "col-end-3"
                    ]
                ),
                self.create_component(
                    component_type="date",
                    label="Data decyzji",
                    name=f"{name}DecisionDate",
                    class_list=[
                        "col-start-3",
                        "col-end-5"
                    ]
                ),
                self.create_component(
                    component_type="text",
                    mask="fund",
                    label="Kwota dotacji",
                    name=f"{name}SubsidyAmount",
                    unit="PLN",
                    class_list=[
                        "col-start-1",
                        "col-end-3"
                    ]
                ),
                self.create_component(
                    component_type="text",
                    label="Numer umowy (jeśli dotyczy)",
                    name=f"{name}ContractNumber",
                    class_list=[
                        "col-start-3",
                        "col-end-5"
                    ]
                ),
                self.create_component(
                    component_type="textarea",
                    label="Uwagi",
                    name=f"{name}Comments",
                    class_list=[
                        "col-span-4"
                    ]
                ),
                self.create_component(
                    component_type="text",
                    label="Data rozliczenia",
                    name=f"{name}SettlementDate"
                )
            ]
        )

    def create_section_for_negative_decision(self, name: str):
        return self.create_chapter(
            visibility_rules=[
                self.visibility_rule.depends_on_value(
                    field_name=f"{name}DirectorDecision",
                    values=["Negatywna"]
                )
            ],
            multiple_forms_rules={
                "minCount": 1,
                "maxCount": 5
            },
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="file",
                            label="Zgoda Dyrektora PISF na ponowne złożenie wniosku",
                            name=f"{name}ConsentDirectorResubmitApplication",
                        )
                    ]
                )
            ]
        )

    def create_section_with_positive_and_negative_decision(self, name: str):
        chapters = [self.create_section_for_positive_decision(name), self.create_section_for_negative_decision(name)]

        return chapters
