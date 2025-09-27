from classes.form_factory.form_factory import FormFactory


class ApplicationScopeOfProject(FormFactory):
    def __init__(self):
        super().__init__()

    def project_implementation_place(self):
        return self.create_chapter(
            title="1. Miejsce realizacji przedsięwzięcia",
            class_list=["grid", "grid-cols-2"],
            components=[
                self.create_component(component_type="text", label="Nazwa kina", name="cinemaName", required=True,
                                      validators=[self.validator.length_validator(max_value=100)]),
                self.create_component(component_type="text", label="Ulica, nr domu, nr lokalu", name="cinemaStreet",
                                      required=True, validators=[self.validator.length_validator(max_value=100)]),
                self.create_component(component_type="text", label="Kod pocztowy", name="cinemaZipcode",
                                      mask="polishPostalCode", required=True),
                self.create_component(component_type="text", label="Miejscowość", name="cinemaLocation", required=True,
                                      validators=[self.validator.length_validator(max_value=100)])
            ]
        )

    def project_implementation_place_education(self):
        return self.create_chapter(
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
        )

    def general_project_description(self):
        return self.create_chapter(
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
        )

    def applicant_experience_summary(self):
        return self.create_chapter(
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
        )

    def project_partners_and_experts(self):
        return self.create_chapter(
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
        )

    def participants_acquired_skills(self):
        return self.create_chapter(
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
        )

    def cinema_detailed_infomration_years_functioning(self):
        return self.create_chapter(
            class_list=["grid", "grid-cols-2"],
            components=[
                self.create_component(component_type="text", label="Od ilu lat prowadzone jest kino",
                                      name="yearsFunctioning", required=True)
            ]
        )

    def cinema_detailed_information_basic_data(self):
        chapter = self.cinema_detailed_infomration_years_functioning()
        chapter["components"].append(
            self.create_component(component_type="radio", label="Kino działa", name="weekdaysActive", required=True,
                                  options=["przez cały tydzień", "weekendowo", "w inny sposób"]))
        chapter["components"].append(
            self.create_component(component_type="radio", label="Czy kino działa w okresie wakacyjnym?",
                                  name="summertimeActive", required=True, options=["Tak", "Nie"]))
        return chapter

    def characteristics_of_cinema_halls(self):
        return self.create_chapter(
            title="<normal>Charakterystyka sal kinowych </normal>",
            multiple_forms_rules={"minCount": 1, "maxCount": 20},
            components=[
                self.create_chapter(
                    class_list=["grid", "grid-cols-2"],
                    components=[
                        self.create_component(component_type="text", label="Liczba miejsc", name="seatsCapacity",
                                              required=True),
                        self.create_component(component_type="text", label="Powierzchnia w metrach kwadratowych",
                                              name="roomArea", required=True),
                        self.create_component(component_type="text", label="Wymiar ekranu (szerokość w metrach)",
                                              name="screenWidth", required=True),
                        self.create_component(component_type="text", label="Wymiar ekranu (wysokość w metrach)",
                                              name="screenHeight", required=True),
                        self.create_component(component_type="text", label="System dźwięku", name="soundSystem",
                                              required=True)
                    ]
                )
            ]
        )

    def number_of_seats_in_room_for_digitization(self):
        return self.create_chapter(
            title="<normal>Liczba miejsc na sali przeznaczonej do cyfryzacji </normal>",
            components=[
                self.create_component(component_type="number", label="Liczba miejsc", name="seatsDigitizationRoom",
                                      required=True)
            ]
        )

    def cinema_projectors_information(self):
        return self.create_chapter(
            title="<normal>Informacja o projektorach znajdujących się w kinie </normal>",
            class_list=["grid", "grid-cols-2"],
            components=[
                self.create_component(component_type="number", label="35 mm", name="numProjectors35", unit="szt."),
                self.create_component(component_type="number", label="16 mm", name="numProjectors16", unit="szt."),
                self.create_component(component_type="number", label="cyfrowy HD", name="numProjectorsDigitalHd",
                                      unit="szt."),
                self.create_component(component_type="number", label="cyfrowy 2K", name="numProjectorsDigital2k",
                                      unit="szt."),
                self.create_component(component_type="number", label="cyfrowy 4K", name="numProjectorsDigital4k",
                                      unit="szt.")
            ]
        )

    def information_about_sound_in_room_for_digitization(self):
        return self.create_chapter(
            title="<normal>Informacja o dźwięku w sali przeznaczonej do cyfryzacji </normal>",
            class_list=["grid", "grid-cols-2"],
            components=[
                self.create_component(component_type="text", label="System dźwięku", name="soundSystemDigitizationRoom",
                                      required=True),
                self.create_component(component_type="text", label="Nazwa procesora", name="cpuNameDigitizationRoom",
                                      required=True),
                self.create_component(component_type="text", label="Powierzchnia kabiny projekcyjnej",
                                      name="projectionCabinAreaDigitizationRoom", required=True)
            ]
        )

    def information_about_location(self):
        return self.create_chapter(
            title="3. Informacje o lokalizacji",
            class_list=["grid", "grid-cols-2"],
            components=[
                self.create_component(component_type="text", label="Liczba mieszkańców",
                                      name="localizationInhabitants"),
                self.create_component(component_type="text", label="Liczba kin w miejscowości",
                                      name="localizationNumCinemas"),
                self.create_component(component_type="text", label="Liczba multipleksów w miejscowości",
                                      name="localizationMultiplexNum"),
                self.create_component(component_type="text", label="Liczba kin studyjnych/lokalnych w miejscowości",
                                      name="localizationArthouseCinemasNum"),
                self.create_component(component_type="text", label="Odległość od najbliższego kina",
                                      name="localizationDistanceToCinema", unit="km"),
                self.create_component(component_type="text", label="Odległość od najbliższego kina cyfrowego",
                                      name="localizationDistanceToDigitalCinema", unit="km")
            ]
        )

    def cinema_activities_information_12_months_period_from_submission(self):
        return self.create_chapter(
            class_list=["grid", "grid-cols-2"],
            components=[
                self.create_component(component_type="text", label="Liczba seansów", name="activitiesNumScreenings"),
                self.create_component(component_type="text", label="Liczba widzów", name="activitiesNumViewers"),
                self.create_component(component_type="text", label="Wpływy z biletów", name="activitiesTicketIncome",
                                      mask="fund"),
                self.create_component(component_type="text", label="Liczba filmów polskich",
                                      name="activitiesNumPolishMovies"),
                self.create_component(component_type="text", label="Liczba premierowych filmów polskich",
                                      name="activitiesNumPremierePolishMovies"),
                self.create_component(component_type="number", label="Procent seansów filmów polskich",
                                      name="activitiesSharePolishMovies", unit="%",
                                      validators=[self.validator.range_validator(min_value=0, max_value=100)]),
                self.create_component(component_type="text", label="Liczba filmów europejskich",
                                      name="activitiesNumEuropeanMovies"),
                self.create_component(component_type="number", label="Procent seansów filmów europejskich",
                                      name="activitiesShareEuropeanMovies", unit="%",
                                      validators=[self.validator.range_validator(min_value=0, max_value=100)]),
                self.create_component(component_type="text", label="Liczba seansów dla szkół",
                                      name="activitiesNumSchoolScreenings")
            ]
        )

    def cinema_additional_activities(self):
        return self.create_chapter(
            title="<normal>W kinie realizowane są: </normal>",
            components=[
                self.create_component(
                    component_type="checkbox",
                    label="festiwale",
                    name="organizesFestivals",
                ),
                self.create_component(
                    component_type="checkbox",
                    label="przeglądy",
                    name="organizesPreviews",
                ),
                self.create_component(
                    component_type="checkbox",
                    label="seanse dla najmłodszych dzieci",
                    name="organizesChildrenScreenings",
                ),
                self.create_component(
                    component_type="checkbox",
                    label="retrospektywy",
                    name="organizesRetrospectives",
                ),
                self.create_component(
                    component_type="checkbox",
                    label="DKF",
                    name="organizesDiscussions",
                )
            ]
        )

    def cinema_education_programs_info(self):
        return self.create_chapter(
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="radio",
                            label="Czy w kinie realizowany jest program edukacji filmowej dla szkół?",
                            name="organizesEducationalPrograms",
                            options=["Tak", "Nie"],
                            required=True
                        ),
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="organizesEducationalPrograms",
                            values=["Tak"])
                    ],
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Jak często odbywają się spotkania?",
                                    name="educationalProgramsFrequency"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Ile szkół bierze udział?",
                                    name="educationalProgramsNumSchools"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Ile uczniów uczestniczyło w edukacji filmowej?",
                                    name="educationalProgramsNumParticipants"
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def cinema_avg_ticket_price(self):
        return self.create_chapter(
            title="<normal>Średnia cena biletu w kinie </normal>",
            components=[
                self.create_component(
                    component_type="text",
                    name="avgTicketPrice",
                    mask="fund",
                    unit="PLN"
                )
            ]
        )

    def cinema_cooperation_with_other_cinemas(self):
        return self.create_chapter(
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Kino współpracuje z innymi kinami w Polsce",
                            name="cooperatesWithOtherPolishCinemas"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="cooperatesWithOtherPolishCinemas",
                            values=[True]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="W jakim zakresie?",
                            name="cooperationDetails",
                            validators=[
                                self.validator.length_validator(max_value=250)
                            ]
                        )
                    ]
                )
            ]
        )

    def cinema_webpage(self):
        return self.create_chapter(
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Kino posiada stronę internetową",
                            name="hasWebpage"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="hasWebpage",
                            values=[True]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Adres strony",
                            name="cinemaWebpageAddress",
                            validators=[
                                self.validator.length_validator(max_value=250)
                            ]
                        )
                    ]
                )
            ]
        )

    def cinema_online_ticketing(self):
        return self.create_chapter(
            components=[
                self.create_component(
                    component_type="checkbox",
                    label="W kinie prowadzona jest internetowa rezerwacja biletów",
                    name="hasInternetTicketBooking"
                ),
                self.create_component(
                    component_type="checkbox",
                    label="W kinie prowadzona jest internetowa sprzedaż biletów",
                    name="hasInternetTicketSales"
                )
            ]
        )

    def cinema_key_events_last_year(self):
        return self.create_chapter(
            title="<normal>Proszę wymienić pięć najważniejszych wydarzeń organizowanych w okresie 12 miesięcy do dnia złożenia wniosku (np. Festiwal Kina Japońskiego, Przegląd Filmów dla Młodzieży, Filmowe poranki dla dzieci itp.) </normal>",
            multiple_forms_rules={"minCount": 1, "maxCount": 10},
            components=[
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Nazwa wydarzenia",
                                    name="bestPastEvents"
                                )
                            ]
                        ),
                        self.create_chapter(
                            class_list=["dates", "grid", "grid-cols-2"],
                            components=[
                                self.create_component(
                                    component_type="date",
                                    label="Od",
                                    name="bestEventDateStart",
                                    validators=[
                                        self.validator.related_local_date_lte_validator(
                                            field_name="bestEventDateStart",
                                            message="Termin rozpoczęcia wydarzenia musi być wcześniejszy niż termin jego zakończenia"
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Do",
                                    name="bestEventDateEnd",
                                    validators=[
                                        self.validator.related_local_date_gte_validator(
                                            field_name="bestEventDateStart",
                                            message="Termin zakończenia wydarzenia musi być późniejszy niż termin jego rozpoczęcia"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def project_description(self):
        return self.create_chapter(
            title="5. Opis przedsięwzięcia (w tym: cel i zakres merytoryczny, zastosowane technologie, sposób realizacji)",
            components=[
                self.create_component(
                    component_type="textarea",
                    name="applicationTaskDescription",
                    validators=[
                        self.validator.length_validator(
                            max_value=1800
                        )
                    ]
                )
            ]
        )

    def cinema_project_relation_to_other_fundings(self):
        return self.create_chapter(
            title="6. Czy przedsięwzięcie, na które składany jest wniosek jest powiązane z innymi przedsięwzięciami, o dofinansowanie których ubiega się Wnioskodawca w bieżącym roku z innych programów operacyjnych PISF? Jeżeli tak, proszę podać nazwę przedsięwzięcia, program oraz wnioskowaną kwotę dofinansowania",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="wasSubmittedBefore",
                            options=["Tak", "Nie"],
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="wasSubmittedBefore",
                            values=["Tak"])
                    ],
                    multiple_forms_rules={"minCount": 1, "maxCount": 20},
                    components=[
                        self.create_chapter(
                            class_list=["grid", "grid-cols-3"],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Nazwa przedsięwzięcia",
                                    name="otherProjectName"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Program operacyjny",
                                    name="programmeName"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Wnioskowana kwota",
                                    name="otherProjectFundingAmount",
                                    unit="PLN",
                                    mask="fund"
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def project_detailed_description(self, chapters: dict):
        return self.create_chapter(
            title="3. Opis szczegółowy przedsięwzięcia",
            components=[
                *[self.create_chapter(
                    title=f"<normal>{chapter["section_title"]}</normal>",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name=chapter["name"],
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ) for chapter in chapters]
            ]
        )

    def expected_type_and_number_of_films_presented(self):
        expected_films_chapters = [
            {
                "name": "feature",
                "label": "Film fabularny"
            },
            {
                "name": "documentary",
                "label": "Film dokumentalny"
            },
            {
                "name": "animated",
                "label": "animowany"
            },
            {
                "name": "experimental",
                "label": "Film eksperymentalny"
            },
            {
                "name": "other",
                "label": "Inny (jakie?)",
                "isOther": True
            }
        ]

        return self.create_chapter(
            title="Rodzaj i przewidywana liczba prezentowanych filmów, przykładowe tytuły (jeśli są już znane)",
            components=[
                *[self.create_chapter(
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label=chapter["label"],
                                    name=f"{chapter["name"]}Film"
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name=f"{chapter["name"]}Film",
                                    values=[True]
                                )
                            ],
                            class_list=[
                                "grid",
                                "grid-cols-3"
                            ],
                            components=[
                                *(
                                    [
                                        self.create_component(
                                            component_type="text",
                                            label="Jakie?",
                                            name=f"{chapter['name']}FilmKind",
                                            validators=[
                                                self.validator.length_validator(max_value=100),
                                                self.validator.related_required_if_equal_validator(
                                                    field_name=f"{chapter['name']}Film",
                                                    value=True
                                                )
                                            ],
                                            class_list=["col-span-3"],
                                            required=True
                                        )
                                    ] if chapter.get("isOther", False) else []
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Liczba",
                                    name=f"{chapter["name"]}FilmCount",
                                    required=True,
                                    validators=[
                                        self.validator.related_required_if_equal_validator(
                                            field_name=f"{chapter["name"]}Film",
                                            value=True
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Tytuły",
                                    name=f"{chapter["name"]}FilmTitles",
                                    validators=[
                                        self.validator.length_validator(max_value=200)
                                    ],
                                    required=True,
                                    class_list=[
                                        "col-star-2",
                                        "col-end-4"
                                    ]
                                )
                            ]
                        )
                    ]
                ) for chapter in expected_films_chapters]
            ]
        )
