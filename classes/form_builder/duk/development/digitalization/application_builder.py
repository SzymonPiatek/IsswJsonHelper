from classes.form_builder.duk.development.application_builder import DevelopmentApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.development.digitalization.estimate_data import estimate_sections


class DigitalizationApplicationBuilder(DevelopmentApplicationBuilder):
    PRIORITY_NAME = 'II. Cyfryzacja kin'
    PRIORITY_NUM = 2
    FORM_ID = 9191

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'digitalization'
        self.estimate_sections = estimate_sections

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Współfinansowanie zakupu sprzętu do projekcji cyfrowych o minimalnej rozdzielczości 2K w standardzie DCI"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_attachments(self):
        part = self.create_part(
            title="VI. Załączniki",
            short_name="VI. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information(),
                        self.section.application_attachment.financial_contribution_confirmation(),
                        self.section.application_attachment.room_pics(),
                        self.section.application_attachment.right_to_property(),
                        self.section.application_attachment.deminimis_statement(),
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )
        self.save_part(part)

    def create_application_scope_of_project(self):
        part = self.create_part(
            title="III. Zakres przedsięwzięcia",
            short_name="III. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="1. Miejsce realizacji przedsięwzięcia",
                    class_list=["grid", "grid-cols-2"],
                    components=[
                        self.create_component(component_type="text", label="Nazwa kina", name="cinemaName", required=True, validators=[self.validator.length_validator(max_value=100)]),
                        self.create_component(component_type="text", label="Ulica, nr domu, nr lokalu", name="cinemaStreet", required=True, validators=[self.validator.length_validator(max_value=100)]),
                        self.create_component(component_type="text", label="Kod pocztowy", name="cinemaZipcode", mask="polishPostalCode", required=True),
                        self.create_component(component_type="text", label="Miejscowość", name="cinemaLocation", required=True, validators=[self.validator.length_validator(max_value=100)])
                    ]
                ),
                self.create_chapter(
                    title="2. Informacje szczegółowe o kinie",
                    components=[
                        self.create_chapter(
                            class_list=["grid", "grid-cols-2"],
                            components=[
                                self.create_component(component_type="text", label="Od ilu lat prowadzone jest kino", name="yearsFunctioning", required=True),
                                self.create_component(component_type="radio", label="Kino działa", name="weekdaysActive", required=True, options=["przez cały tydzień", "weekendowo", "w inny sposób"]),
                                self.create_component(component_type="radio", label="Czy kino działa w okresie wakacyjnym?", name="summertimeActive", required=True, options=["tak", "nie"])
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Liczba sal kinowych </normal>",
                            multiple_forms_rules={"minCount": 1, "maxCount": 20},
                            components=[
                                self.create_chapter(
                                    class_list=["grid", "grid-cols-2"],
                                    components=[
                                        self.create_component(component_type="text", label="Liczba miejsc", name="seatsCapacity", required=True),
                                        self.create_component(component_type="text", label="Powierzchnia w metrach kwadratowych", name="roomArea", required=True),
                                        self.create_component(component_type="text", label="Wymiar ekranu (szerokość w metrach)", name="screenWidth", required=True),
                                        self.create_component(component_type="text", label="Wymiar ekranu (wysokość w metrach)", name="screenHeight", required=True),
                                        self.create_component(component_type="text", label="System dźwięku", name="soundSystem", required=True)
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Liczba miejsc na sali przeznaczonej do cyfryzacji </normal>",
                            components=[
                                self.create_component(component_type="number", label="Liczba miejsc", name="seatsDigitizationRoom", required=True)
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Informacja o projektorach znajdujących się w kinie </normal>",
                            class_list=["grid", "grid-cols-2"],
                            components=[
                                self.create_component(component_type="number", label="35 mm", name="numProjectors35", unit="szt."),
                                self.create_component(component_type="number", label="16 mm", name="numProjectors16", unit="szt."),
                                self.create_component(component_type="number", label="cyfrowy HD", name="numProjectorsDigitalHd", unit="szt."),
                                self.create_component(component_type="number", label="cyfrowy 2K", name="numProjectorsDigital2k", unit="szt."),
                                self.create_component(component_type="number", label="cyfrowy 4K", name="numProjectorsDigital4k", unit="szt.")
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Informacja o dźwięku w sali przeznaczonej do cyfryzacji </normal>",
                            class_list=["grid", "grid-cols-2"],
                            components=[
                                self.create_component(component_type="text", label="System dźwięku", name="soundSystemDigitizationRoom", required=True),
                                self.create_component(component_type="text", label="Nazwa procesora", name="cpuNameDigitizationRoom", required=True),
                                self.create_component(component_type="text", label="Powierzchnia kabiny projekcyjnej", name="projectionCabinAreaDigitizationRoom", required=True)
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)
