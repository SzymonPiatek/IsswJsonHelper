from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class EducationApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'II. Edukacja filmowa'
    OPERATION_NUM = 2

    def __init__(self):
        super().__init__()

        self.program_data_path = self.department_data_path / 'education'

    def create_application_scope_of_project(self, **kwargs):
        data = kwargs["data"]

        part = self.create_part(
            title="III. Zakres przedsięwziecia",
            short_name="III. Zakres przedsięwzięcia",
            class_list=[
                "full-width-grid"
            ],
            chapters=[
                self.create_chapter(
                    title="1. Miejsce realizacji przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="projectLocation",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Opis ogólny przedsięwzięcia (cel i zakres merytoryczny, zastosowane technologie, sposób realizacji przedsięwzięcia, promocja)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectGeneralDescription",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Opis szczegółowy przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            title="<normal>Wartość merytoryczna przedsięwzięcia, w tym ciągłość realizacji przedsięwzięcia oraz wartość edukacyjna</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="scopeAndValueOfContent",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Planowane efekty realizacji przedsięwzięcia oraz jego ewaluacja</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedResultsOfProject",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Dotychczasowe doświadczenia wnioskodawcy w działaniach będących przedmiotem przedsięwzięcia</br><normal>Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez wnioskodawcę w ostatnich 2 latach</normal>",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicantsPastExperience",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="5. Partnerzy, eksperci i specjaliści zaangażowani w przedsięwzięcie i ich dotychczasowy dorobek w tym zakresie",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="involvedPartnersAndSpecialist",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="6. Informacje o praktycznych umiejętnościach nabywanych przez uczestników przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="practicalSkillsAcquiredByParticipants",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                *data["chapters"]
            ]
        )
        self.save_part(part)
