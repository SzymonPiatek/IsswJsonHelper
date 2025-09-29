from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .priority import FestivalsPriority


class FestivalsApplicationBuilder(DisseminationApplicationBuilder, FestivalsPriority):
    FORM_ID = 9184

    def __init__(self):
        super().__init__()

    def create_application_basic_data(self):
        part = self.create_part(
            title="I. Dane podstawowe",
            short_name="I. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    title="1. Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskName",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Rodzaj przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="projectType",
                            options=["Organizacja festiwali filmowych o charakterze ogólnopolskim lub międzynarodowym, będących wydarzeniami cyklicznymi, obejmujących szeroki program filmowy, sekcje konkursowe oceniane przez jury oraz wydarzenia towarzyszące, takie jak spotkania z twórcami, panele dyskusyjne czy warsztaty."]
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Poprzednia edycja przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    label="Czy poprzednia edycja przedsięwzięcia została dofinansowana przez PISF?",
                                    name="previousApplicationForProject",
                                    options=[
                                        "Tak", "Nie"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="previousApplicationForProject",
                                    values=[
                                        "Tak"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    name="fiveDigitNumberOfApplication",
                                    label="Numer wniosku dotyczący poprzedniej edycji przedsięwzięcia",
                                    validators=[
                                        self.validator.related_required_if_equal_validator(
                                            field_name="previousApplicationForProject",
                                            value="Tak"
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)
