from classes.form_factory.form_factory import FormFactory


class ApplicationCompletionDateData(FormFactory):
    def __init__(self):
        super().__init__()

    def shooting_days(self):
        return self.create_chapter(
            title="Dni zdjęciowe",
            class_list=[
                "grid",
                "grid-cols-2"
            ],
            components=[
                self.create_component(
                    component_type="number",
                    label="Łączna liczba dni zdjęciowych",
                    name="scheduleShootingDaysAll",
                    required=True
                ),
                self.create_component(
                    component_type="number",
                    label="Liczba dni zdjęciowych na terenie Polski",
                    name="scheduleShootingDaysPoland",
                    required=True
                )
            ]
        )

    def planned_date_of_master_copy(self):
        return self.create_chapter(
            title="Planowany termin wykonania kopii wzorcowej",
            class_list=[
                "grid",
                "grid-cols-2"
            ],
            components=[
                self.create_component(
                    component_type="date",
                    name="scheduleFinalCopyDate",
                    validators=[
                        self.validator.related_date_gte_validator(
                            field_name="scheduleFinalWorksPeriodStart",
                            message="Wykonanie kopii wzorcowej nie może odbyć się wcześniej niż data początku prac końcowych."
                        ),
                        self.validator.related_date_lte_validator(
                            field_name="scheduleFinalWorksPeriodEnd",
                            message="Wykonanie kopii wzorcowej nie może odbyć się później niż data zakończenia prac końcowych."
                        )
                    ],
                    required=True
                )
            ]
        )

    def planned_date_of_film_release(self):
        return self.create_chapter(
            title="Planowany termin wprowadzenia filmu do obrotu (premiera/eksploatacja)",
            class_list=[
                "grid",
                "grid-cols-2"
            ],
            components=[
                self.create_component(
                    component_type="date",
                    name="schedulePremiereDate",
                    validators=[
                        self.validator.related_date_gte_validator(
                            field_name="scheduleFinalCopyDate",
                            message="Planowany termin wprowadzenia filmu do obrotu musi nastąpić po planowanym terminie wykonania kopii wzorcowej."
                        )
                    ],
                    required=True
                )
            ]
        )

    def operational_reports(self):
        return self.create_chapter(
            title="Raporty z eksploatacji",
            components=[
                self.create_chapter(
                    title=chapter["title"],
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name=chapter["component"]["name"],
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field=chapter["component"]["field"],
                                    parameter=chapter["component"]["parameter"]
                                )
                            ]
                        )
                    ]
                ) for chapter in [
                    {
                        "title": "I Raport",
                        "component": {
                            "name": "scheduleFirstReportDate",
                            "field": "schedulePremiereDate",
                            "parameter": 182
                        }
                    },
                    {
                        "title": "II Raport",
                        "component": {
                            "name": "scheduleSecondReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 182
                        }
                    },
                    {
                        "title": "III Raport",
                        "component": {
                            "name": "scheduleThirdReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 364
                        }
                    },
                    {
                        "title": "IV Raport",
                        "component": {
                            "name": "scheduleFourthReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 546
                        }
                    },
                    {
                        "title": "V Raport",
                        "component": {
                            "name": "scheduleFifthReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 728
                        }
                    },
                    {
                        "title": "VI Raport",
                        "component": {
                            "name": "scheduleSixthReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 910
                        }
                    },
                    {
                        "title": "VII Raport",
                        "component": {
                            "name": "scheduleSeventhReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 1092
                        }
                    },
                    {
                        "title": "VIII Raport",
                        "component": {
                            "name": "scheduleEighthReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 1274
                        }
                    },
                    {
                        "title": "IX Raport",
                        "component": {
                            "name": "scheduleNinthReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 1456
                        }
                    },
                    {
                        "title": "X Raport",
                        "component": {
                            "name": "scheduleTenthReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 1638
                        }
                    },
                    {
                        "title": "XI Raport",
                        "component": {
                            "name": "scheduleEleventhReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 1820
                        }
                    },
                    {
                        "title": "XII Raport",
                        "component": {
                            "name": "scheduleTwelfthReportDate",
                            "field": "scheduleFirstReportDate",
                            "parameter": 2002
                        }
                    }
                ]
            ]
        )

    def mandatory_activities(self):
        return self.create_chapter(
            title="OBLIGATORYJNE CZYNNOŚCI W PRZYPADKU ZAWARCIA UMOWY O DOFINANSOWANIE",
            components=[
                self.create_chapter(
                    title="Termin doręczenia audytu (po okresie zdjęciowym) (jeśli dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja)",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="scheduleAuditDate",
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="scheduleAnimationPeriodEnd",
                                    parameter=30
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Termin doręczenia materiałów promocyjnych",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="schedulePromoMaterialsDate",
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="scheduleAnimationPeriodEnd",
                                    parameter=30
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Termin, do którego należy zorganizować pierwszą kolaudację",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="scheduleFirstPreReleaseReviewDate",
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="schedulePostProdPeriodEnd",
                                    parameter=0
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Termin, do którego należy zorganizować drugą kolaudację",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Termin do",
                            name="scheduleSecondPreReleaseReviewDate",
                            required=True,
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Akceptacja zastosowania logo PISF oraz napisów",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="scheduleLogoDate",
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="scheduleFinalCopyDate",
                                    parameter=-15
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Termin doręczenia drugiego audytu (po okresie prac końcowych)",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="scheduleSecondAutitDate",
                            help_text="Dotyczy filmów pełnometrażowych oraz serii animowanych.",
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="scheduleFinalWorksPeriodEnd",
                                    parameter=30
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Termin doręczenia raportu końcowego",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="scheduleFinalReportDate",
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="scheduleFinalWorksPeriodEnd",
                                    parameter=30
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Akceptacja materiałów promocyjno-dystrybucyjnych z wykorzystaniem logo PISF",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="schedulePromoMaterialsAcceptanceDate",
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="schedulePremiereDate",
                                    parameter=-15
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Doręczenie do PISF umowy z dystrybutorem oraz kosztorysu P&A",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="scheduleDistributorContractDate",
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="schedulePremiereDate",
                                    parameter=-14
                                )
                            ]
                        )
                    ]
                ),
            ]
        )
