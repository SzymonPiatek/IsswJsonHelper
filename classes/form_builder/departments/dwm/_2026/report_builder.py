from classes.form_builder.departments.dwm.report_builder import DWMReportBuilder


class DWMReportBuilder2026(DWMReportBuilder):
    YEAR = 2026

    def __init__(self):
        super().__init__()

    def create_report_additional_information(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dodatkowe informacje",
            chapters=[
                self.create_chapter(
                    class_list=[
                        "grid",
                        "grid-cols-4",
                    ],
                    components=[
                        self.create_component(
                            component_type="header",
                            value="Dodatkowe informacje",
                            name="additionalGeneralComments",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Dodatkowe informacje",
                            name="additionalGeneralComments",
                            validators=[
                                self.validator.length_validator(max_value=10000)
                            ],
                            class_list=[
                                "no-label",
                                "col-span-3",
                                "text-left"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="header",
                                    value="Do raportu należy załączyć ewentualny raport medialny, ulotki, plakaty oraz inne materiały promocyjne i informacyjne.",
                                    name="attachmentsDesc"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Informacja o załącznikach",
                            class_list=[
                                "grid",
                                "grid-cols-4",
                                "no-title"
                            ],
                            components=[
                                self.create_component(
                                    component_type="header",
                                    value="Informacja o załącznikach",
                                    name="attachmentsInfo",
                                    class_list=[
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    name="attachmentsInfo",
                                    validators=[
                                        self.validator.length_validator(max_value=20000)
                                    ],
                                    class_list=[
                                        "col-span-3",
                                        "text-left"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Lista załączników",
                            components=[
                                self.create_chapter(
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 20
                                    },
                                    class_list={
                                        "main": [
                                            "swappable-bg",
                                        ]
                                    },
                                    components=[
                                        self.create_chapter(
                                            title="Załącznik",
                                            class_list=[
                                                "no-title",
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="file",
                                                    name="reportAttachment"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Oświadczenia",
                    class_list=[
                        "no-title",
                        "grid",
                        "grid-cols-10"
                    ],
                    components=[
                        *[comp
                          for checkbox in [
                              {
                                  "label": "Od daty zawarcia umowy nie zmienił się status prawny Beneficjenta.",
                                  "name": "statementLegalStatusUnchanged"
                              },
                              {
                                  "label": "Wszystkie podane w niniejszym raporcie informacje są zgodne z aktualnym stanem prawnym i faktycznym.",
                                  "name": "statementDeclaredInformationUptodate"
                              },
                              {
                                  "label": "Przedstawiciele Instytutu dokonujący weryfikacji mogą dokonać poprawy oczywistych omyłek pisarskich i rachunkowych w raporcie końcowym, zawiadamiając o tym Beneficjenta.",
                                  "name": "statementInstituteMayCorrectObviousErrors"
                              },
                              {
                                  "label": "Oświadczam, że zestawienie faktur (rachunków) obejmuje wyłącznie koszty ujęte w ewidencji księgowej podmiotu realizującego przedsięwzięcie.",
                                  "name": "statementInvoicesIncludeOnlyRecordedCosts"
                              },
                              {
                                  "label": "Oświadczam, że wszystkie kwoty wymienione w zestawieniu faktur (rachunków) zostały faktycznie poniesione.",
                                  "name": "statementAllInvoiceAmountsActuallyIncurred"
                              },
                              {
                                  "label": "Oświadczam, że wszystkie płatności, w tym podatki i świadczenia od wynagrodzeń zostały uregulowane do dnia zakończenia zadania, o którym mowa w § ………… zawartej umowy z PISF.",
                                  "name": "statementAllPaymentsSettledByProjectEnd"
                              },
                              {
                                  "label": "Oświadczam, że w całkowitym koszcie przedsięwzięcia nie został uwzględniony podatek od towarów i usług (VAT) podlegający odzyskaniu lub rozliczeniu w deklaracjach składanych do Urzędu Skarbowego.",
                                  "name": "statementNoRecoverableVATIncluded"
                              },
                              {
                                  "label": "Oświadczam, że nie toczą się przeciwko mnie żadne postępowania sądowe oraz nie posiadam żadnych tytułów egzekucyjnych wydanych przez komornika.",
                                  "name": "statementNoLegalProceedingsOrEnforcements"
                              }
                          ]
                          for comp in [
                              self.create_component(
                                  component_type="checkbox",
                                  label=checkbox["label"],
                                  name=checkbox["name"],
                                  required=True,
                                  class_list=[
                                      "no-label",
                                      "text-center"
                                  ]
                              ),
                              self.create_component(
                                  component_type="header",
                                  name=checkbox["name"],
                                  class_list=[
                                      "col-span-9",
                                      "text-left",
                                      "displayNoneFrontend"
                                  ]
                              )
                          ]],
                        self.create_component(
                            component_type="text",
                            label="PODPIS BENEFICJENTA:",
                            name="reportSignature",
                            class_list=[
                                "col-start-7",
                                "col-span-4",
                                "text-center",
                                "report-signature",
                                "displayNoneFrontend"
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)
