from classes.form_builder.additional.components.section.section import Section


class ApplicationNameData(Section):
    def __init__(self):
        super().__init__()

    def application_task_name(self, number: str):
        return self.create_chapter(
            title=f"{number}. Nazwa przedsięwzięcia",
            components=[
                self.create_component(
                    component_type="textarea",
                    name="applicationTaskName",
                    required=True,
                    validators=[
                        self.validator.length_validator(max_value=600)
                    ]
                )
            ]
        )

    def events_names_and_dates(self, number: str):
        return self.create_chapter(
            title=f"{number}. Nazwa i termin docelowego wydarzenia",
            multiple_forms_rules={
                "minCount": 1,
                "maxCount": 20
            },
            components=[
                self.create_chapter(
                    title="Wydarzenie",
                    class_list={
                        "main": [
                            "table-1-2",
                            "grid",
                            "grid-cols-2"
                        ],
                        "sub": [
                            "table-1-2__col"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nazwa wydarzenia",
                            name="eventName",
                            required=True,
                            class_list=[
                                "table-full",
                                "col-span-2"
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin od",
                            name="eventDateStart",
                            required=True,
                            validators=[
                                self.validator.related_local_date_lte_validator(
                                    field_name="eventDateEnd",
                                    message="Data początkowa nie może być późniejsza niż data końcowa."
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="eventDateEnd",
                            required=True,
                            validators=[
                                self.validator.related_local_date_gte_validator(
                                    field_name="eventDateStart",
                                    message="Data końcowa nie może być wcześniejsza niż data początkowa."
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def country_and_city_of_events(self, number: str):
        return self.create_chapter(
            title=f"{number}. Miasto i kraj, w którym odbywa sie wydarzenie",
            multiple_forms_rules={
                "minCount": 1,
                "maxCount": 20
            },
            components=[
                self.create_chapter(
                    title="Lokalizacja",
                    class_list={
                        "main": [
                            "table-1-2",
                            "grid",
                            "grid-cols-2"
                        ],
                        "sub": [
                            "table-1-2__col"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="country",
                            label="Kraj",
                            name="eventCountry",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Miasto",
                            name="eventLocation",
                            required=True
                        )
                    ]
                )
            ]
        )

    def project_for_event(self, number: str):
        return self.create_chapter(
            title=f"{number}. Projekt/film, z którym Wnioskodawca bierze udział w wydarzeniu",
            class_list={
                "main": [
                    "table-1-2",
                    "grid",
                    "grid-cols-2"
                ],
                "sub": [
                    "table-1-2__col"
                ]
            },
            components=[
                self.create_component(
                    component_type="text",
                    label="Tytuł filmu",
                    name="eventMovieTitle",
                    required=True,
                    class_list=[
                        "table-full"
                    ]
                ),
                self.create_component(
                    component_type="text",
                    label="Imię i nazwisko reżysera",
                    name="eventMovieDirector",
                    required=True,
                    class_list=[
                        "table-full"
                    ]
                ),
                self.create_component(
                    component_type="number",
                    label="Metraż filmu w minutach",
                    name="eventMovieDuration",
                    required=True
                ),
                self.create_component(
                    component_type="select",
                    label="Rodzaj filmu",
                    name="movieType",
                    options=[
                        "fabularny",
                        "dokumentalny",
                        "animowany"
                    ],
                    required=True
                ),
                self.create_component(
                    component_type="text",
                    label="Sekcja na festiwalu",
                    name="eventEventSession",
                    help_text="Podaj sekcję na festiwalu, w której odbędzie się prezentacja filmu.",
                    required=True,
                    class_list=[
                        "table-full"
                    ]
                ),
                self.create_component(
                    component_type="text",
                    label="Rodzaj premiery",
                    name="eventMoviePremiereType",
                    required=True
                ),
                self.create_component(
                    component_type="text",
                    label="Rok produkcji",
                    name="movieProdYear",
                    required=True
                )
            ]
        )

    def project_is_supported_by_pisf(self, number: str, after_name: str = ''):
        return self.create_chapter(
            title=f"{number}. Czy projekt/film został wsparty przez PISF?",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="radio",
                            name=f"wasMovieProjectSupportedByPisf{after_name}",
                            options=[
                                "Tak",
                                "Nie"
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "table-1-2",
                            "grid",
                            "grid-cols-2"
                        ],
                        "sub": [
                            "table-1-2__col"
                        ]
                    },
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name=f"wasMovieProjectSupportedByPisf{after_name}",
                            values=[
                                "Tak"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Program operacyjny",
                            name=f"movieProjectSupportedByPisfProgram{after_name}",
                            required=True,
                            class_list=[
                                "col-span-2",
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Priorytet",
                            name=f"movieProjectSupportedByPisfPriority{after_name}",
                            required=True,
                            class_list=[
                                "col-span-2",
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Rok przyznania dofinansowania",
                            name=f"movieProjectSupportedPisfYear{after_name}",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Kwota dofinansowania",
                            name=f"movieProjectSupportedPisfAmount{after_name}",
                            unit="PLN",
                            required=True
                        )
                    ]
                )
            ]
        )
