from typing import List, Optional
from classes.form_factory.form_factory import FormFactory


class ApplicationBasicData(FormFactory):
    def __init__(self):
        super().__init__()

    def scope_of_project(self, number: int | str, options: List[str]):
        return self.create_chapter(
            title=f"{number}. Zakres przedsięwzięcia",
            components=[
                self.create_component(
                    component_type="select",
                    name="scopeOfProject",
                    options=options,
                    required=True
                )
            ]
        )

    def scope_of_project_kind(self, number: int | str, options: List[str], calculation_rules: Optional[List[dict]] = None):
        return self.create_chapter(
            title=f"{number}. Przedsięwzięcie jest:",
            components=[
                self.create_component(
                    component_type="select",
                    name="scopeOfProjectKind",
                    options=options,
                    required=True,
                    calculation_rules=calculation_rules
                )
            ]
        )

    def movie_kind(self, number: int | str, options: List[str]):
        return self.create_chapter(
            title=f"{number}. Rodzaj filmowy",
            components=[
                self.create_component(
                    component_type="select",
                    name="movieKind",
                    options=options,
                    required=True
                )
            ]
        )

    def movie_subject(self, number: int | str, options: List[str], validators: Optional[List[dict]] = None, is_film_about_history: bool = False):
        chapter = self.create_chapter(
            title=f"{number}. Tematyka",
            components=[
                self.create_component(
                    component_type="select",
                    name="movieSubject",
                    options=options,
                    validators=validators,
                    required=True
                )
            ]
        )
        if is_film_about_history:
            chapter["components"].append(
                self.create_component(
                    component_type="radio",
                    label="Czy film jest o tematyce historycznej?",
                    name="isFilmAboutHistory",
                    options=[
                        "Tak", "Nie"
                    ],
                    required=True
                )
            )

        return chapter

    def piece_title(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Tytuł utworu audiowizualnego",
            components=[
                self.create_component(
                    component_type="text",
                    name="pieceTitle",
                    required=True,
                    validators=[
                        self.validator.length_validator(max_value=200)
                    ]
                )
            ]
        )

    def short_movie_description(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Krótki opis filmu",
            components=[
                self.create_component(
                    component_type="textarea",
                    name="shortMovieDescription",
                    required=True,
                    validators=[
                        self.validator.length_validator(max_value=5400)
                    ]
                )
            ]
        )

    def category_of_project(self, number: int | str, options: List[str]):
        chapter = self.create_chapter(
            title=f"{number}. Kategoria przedsięwzięcia",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="select",
                            name="categoryOfProject",
                            options=options,
                            required=True
                        )
                    ]
                )
            ]
        )

        value = 'koprodukcja międzynarodowa większościowa'
        second_value = "koprodukcja międzynarodowa mniejszościowa"

        values = []
        if value in options:
            values.append(value)
        if second_value in options:
            values.append(second_value)

        if value in options or second_value in options:
            inside_chapter = self.create_chapter(
                visibility_rules=[
                    self.visibility_rule.depends_on_value(
                        field_name="categoryOfProject",
                        values=[values]
                    )
                ],
                components=[
                    self.create_component(
                        component_type="select",
                        label=f"{number}.1. Wyłączne prawa wnioskodawcy na terytorium Polski",
                        name="movieRights",
                        options=["Tak"],
                        required=True
                    ),
                    self.create_component(
                        component_type="countryMulti",
                        label=f"{number}.2. Kraje koprodukcji",
                        name="coproductionCountries",
                        required=True
                    )
                ]
            )

            if second_value in options:
                inside_chapter["components"].append(
                    self.create_component(
                        component_type="select",
                        label=f"{number}.3. Rodzaj koprodukcji",
                        name="coproductionKind",
                        options=[
                            "koprodukcja dwustronna",
                            "koprodukcja wielostronna"
                        ],
                        required=True
                    )
                )

            chapter["components"].append(inside_chapter)


        if value in options:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="categoryOfProject",
                            values=[value]
                        )
                    ],
                    components=[

                    ]
                )
            )

        return chapter

    def application_relates(self, number: int | str, options: List[str]):
        return self.create_chapter(
            title=f"{number}. Wniosek dotyczy",
            components=[
                self.create_component(
                    component_type="select",
                    name="applicationRelates",
                    options=options,
                    required=True
                )
            ]
        )

    def kind_of_support(self, number, options: List[str]):
        chapter = self.create_chapter(
            title=f"{number}. Rodzaj pomocy",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="select",
                            name="kindOfSupport",
                            options=options,
                            required=True
                        )
                    ]
                )
            ]
        )

        value = "pożyczka"
        if value in options:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="kindOfSupport",
                            values=[value]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.1. Sposób zabezpieczenia pożyczki",
                            name="methodOfSecuringTheLoan",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.2. Proponowane raty spłaty pożyczki",
                            name="proposedLoanPaymentInstallments",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        )
                    ]
                )
            )

        value = "poręczenie"
        if value in options:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="kindOfSupport",
                            values=[value]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.1. Przedmiot zobowiązania",
                            name="subjectOfObligation",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.2. Wysokość i okres poręczenia",
                            name="amountAndPeriodOfGuarantee",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.3. Zabezpieczenie poręczenia",
                            name="securityOfGuarantee",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        )
                    ]
                )
            )

        return chapter

    def one_stage_commission(self, number: int | str):
        return self.create_chapter(
            title=f"{number}.1. Komisja jednoetapowa"
        )

    def two_stages_commission(self, number: int | str, options: List[str], after_name: Optional[str] = ''):
        return self.create_chapter(
            title=f"{number}.1. Komisja dwuetapowa",
            components=[
                self.create_component(
                    component_type="select",
                    label=f"{number}.1.1. Lista pierwszego wyboru",
                    name=f"firstChoiceCommittee{after_name}",
                    options=options,
                    required=True
                ),
                self.create_component(
                    component_type="select",
                    label=f"{number}.1.2. Lista drugiego wyboru",
                    name=f"secondChoiceCommittee{after_name}",
                    options=options,
                    required=True
                ),
                self.create_component(
                    component_type="select",
                    label=f"{number}.1.3. W przypadku niedostępności wybranej komisji",
                    name=f"noCommitteeAvailable{after_name}",
                    options=[
                        "w przypadku niedostępności żadnej z dwóch wybranych komisji składam wniosek do następnej wolnej komisji",
                        "w przypadku niedostępności żadnej z dwóch wybranych komisji wycofuję wniosek z oceny"
                    ],
                    required=True
                )
            ]
        )
