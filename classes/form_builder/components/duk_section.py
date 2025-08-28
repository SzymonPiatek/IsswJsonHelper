from classes.form_builder.components.section import Section
from classes.form_builder.form_builder_base import FormBuilderBase
from classes.form_builder.components.component import Component


class DUKSection(Section):
    def __init__(self):
        super().__init__()

        self.application_attachment = ApplicationAttachmentSection()
        self.application_scope_of_project = ApplicationScopeOfProject()


class ApplicationAttachmentSection(FormBuilderBase):
    def __init__(self):
        super().__init__()

        self.component = Component()

    def document_confirming_represent_applicant(self):
        return self.create_chapter(
            multiple_forms_rules={
                "minCount": 1,
                "maxCount": 10
            },
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="file",
                            label="Dokumenty potwierdzające uprawnienie do reprezentacji Wnioskodawcy przy składaniu wniosku (np. KRS, RIK, statut, pełnomocnictwo)",
                            name="documentConfirmingRepresentApplicant",
                            required=True
                        )
                    ]
                )
            ]
        )

    def other_attachments(self):
        return self.create_chapter(
            title="Inne załączniki",
            components=[
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 50
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="otherAttachments",
                                    help_text="Maksymalny rozmiar pliku to 50 MB"
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def schedule_information(self):
        return self.create_chapter(
            title="<small>Harmonogram i kosztorys stanowią integralną część wniosku. </small><br /><br /><normal><small>Załączanym plikom należy nadać nazwy umożliwiające określenie ich zawartości. <br /><br />Wniosek i wszystkie załączniki należy wypełniać w języku polskim. Jeśli załączane dokumenty oryginalne (w szczególności dokumenty urzędowe, np. wypisy z rejestrów i umowy) sporządzone są w języku innym niż polski, należy załączyć do nich również ich tłumaczenie przysięgłe na język polski. </small></normal>"
        )

    def storage_of_blanks(self):
        return self.create_chapter(
            title="Przechowywanie blankietów dokumentów publicznych oraz dokumentów publicznych",
            components=[
                self.create_chapter(
                    title="<small>Art. 43 ustawy z dnia 22 listopada 2018 r. o dokumentach publicznych. <br /><normal>1. Blankiety dokumentów publicznych przechowywane w miejscu ich personalizacji lub indywidualizacji oraz dokumenty publiczne przechowywane w miejscu ich wydawania zabezpiecza się przed dostępem osób nieuprawnionych, utratą, zniszczeniem lub uszkodzeniem. <br /> 2. Pomieszczenie, w którym są przechowywane dokumenty publiczne oraz blankiety tych dokumentów, jest zamykane, a dostęp do tego pomieszczenia mają wyłącznie osoby uprawnione. Jeżeli to pomieszczenie znajduje się na parterze, okna zewnętrzne są zabezpieczone: szybami odpornymi na przebicie lub rozbicie lub stalowymi żaluzjami albo siatkami stalowymi, lub okratowaniem. <br />3. Pomieszczenie, o którym mowa w ust.2, przeznaczone także do wydawania dokumentów publicznych posiada wydzieloną część, w której są przechowywane dokumenty publiczne, zabezpieczoną przed dostępem osób nieuprawnionych. <br />4. Dokumenty publiczne, o których mowa w art. 5 ust. 4, oraz blankiety tych dokumentów mogą być przechowywane w innym pomieszczeniu niż określone w ust. 2, jeżeli są przechowywane w szafie metalowej zamykanej lub w sejfie, do których dostęp mają wyłącznie osoby upoważnione. <br />5. Dostęp do pomieszczenia, o którym mowa w ust. 2, oraz do wydzielonej części pomieszczenia, o której mowa w ust. 3, a także do szafy metalowej zamykanej lub do sejfu, o którym mowa w ust. 4, jest rejestrowany. <br />6. Rejestrowanie dostępu, o którym mowa w ust. 5, może polegać na zamontowaniu systemu kontroli dostępu do pomieszczenia, o którym mowa w ust. 2, i wydzielonej części pomieszczenia, o której mowa w ust. 3, lub prowadzeniu rejestru wejść i wyjść do i z tego pomieszczenia oraz prowadzeniu rejestru wydawania i zwrotu kluczy do tego pomieszczenia i szafy metalowej zamykanej lub do sejfu, o których mowa w ust. 4.</small></normal><br /><small>Art. 44. <br /><normal>Dokumenty publiczne będące drukami ścisłego zarachowania oraz blankiety tych dokumentów są ewidencjonowane. Ewidencja dokumentów publicznych i blankietów tych dokumentów oraz dowody ich przekazania i odbioru zabezpiecza się przed dostępem osób nieuprawnionych w sposób przewidziany w art. 43 </small></normal>"
                )
            ]
        )

    def right_to_property(self):
        return self.create_chapter(
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Dokument potwierdzający posiadanie przez Wnioskodawcę tytułu prawnego do nieruchomości przez okres co najmniej 3 lat, liczonych od rozpoczęcia sesji naboru wniosków",
                            name="isRightToProperty",
                            read_only=True,
                            required=True,
                            value=True
                        )
                    ]
                ),
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 5
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="attachmentRightToProperty",
                                    help_text="Plik PDF (należy podpisać elektronicznie). Maksymalny rozmiar pliku to 50 MB",
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def room_pics(self):
        return self.create_chapter(
            title="<normal>Zdjęcia sal kinowych i kabiny projekcyjnej (max 5 szt.)</normal>",
            multiple_forms_rules={
                "minCount": 1,
                "maxCount": 5
            },
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="file",
                            name="attachmentRoomPics",
                            required=True
                        )
                    ]
                )
            ]
        )

    def building_permit(self):
        return self.create_chapter(
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Pozwolenie na budowę (dot. budowy, modernizacji i adaptacji obiektów)",
                            name="isBuildingPermit"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="isBuildingPermit",
                            values=[
                                True
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="file",
                            name="attachmentBuildingPermit",
                            help_text="Plik PDF (należy podpisać elektronicznie). Maksymalny rozmiar pliku to 50 MB",
                            required=True
                        )
                    ]
                )
            ]
        )

    def investment_cost_estimate(self):
        return self.create_chapter(
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Kosztorys prac inwestycyjnych, z uwzględnieniem kosztów zakupu materiałów (dot. budowy, modernizacji i adaptacji obiektów)",
                            name="isInvestmentCostEstimate"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="isInvestmentCostEstimate",
                            values=[
                                True
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="file",
                            name="attachmentInvestmentCostEstimate",
                            help_text="Plik PDF (należy podpisać elektronicznie). Maksymalny rozmiar pliku to 50 MB",
                            required=True
                        )
                    ]
                )
            ]
        )

    def financial_contribution_confirmation(self):
        return self.create_chapter(
            title="",
            components=[
                self.create_component(
                    component_type="file",
                    label="Poświadczenie posiadania finansowego wkładu własnego (np. opinia bankowa o rachunku firmy, wyciąg z konta, umowa z podmiotem współfinansującym)",
                    name="attachmentBankOpinion",
                    required=True
                )
            ]
        )

    def deminimis_statement(self):
        return self.create_chapter(
            title="<normal>Oświadczenie dotyczące pomocy de minimis </normal>",
            components=[
                self.create_component(
                    component_type="file",
                    name="attachmentDeminimisStatement",
                    help_text="Plik PDF (należy podpisać elektronicznie). Maksymalny rozmiar pliku to 50 MB",
                    required=True
                )
            ]
        )


class ApplicationScopeOfProject(FormBuilderBase):
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
                self.create_component(component_type="text", label="Wpływy z biletów", name="activitiesTicketIncome", mask="fund"),
                self.create_component(component_type="text", label="Liczba filmów polskich", name="activitiesNumPolishMovies"),
                self.create_component(component_type="text", label="Liczba premierowych filmów polskich", name="activitiesNumPremierePolishMovies"),
                self.create_component(component_type="number", label="Procent seansów filmów polskich", name="activitiesSharePolishMovies", unit="%", validators=[self.validator.range_validator(min_value=0, max_value=100)]),
                self.create_component(component_type="text", label="Liczba filmów europejskich", name="activitiesNumEuropeanMovies"),
                self.create_component(component_type="number", label="Procent seansów filmów europejskich", name="activitiesShareEuropeanMovies", unit="%", validators=[self.validator.range_validator(min_value=0, max_value=100)]),
                self.create_component(component_type="text", label="Liczba seansów dla szkół", name="activitiesNumSchoolScreenings")
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
