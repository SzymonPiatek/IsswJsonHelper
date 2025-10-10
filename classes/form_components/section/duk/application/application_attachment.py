from classes.form_components.component import Component
from classes.form_factory.form_factory import FormFactory


class ApplicationAttachment(FormFactory):
    def __init__(self):
        super().__init__()

        self.component = Component()

    def document_confirming_represent_applicant(self):
        return self.create_chapter(
            title="Dokumenty potwierdzające uprawnienie do reprezentacji Wnioskodawcy przy składaniu wniosku (np. KRS, RIK, statut, pełnomocnictwo)",
            components=[
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 10
                    },
                    components=[
                        self.create_chapter(
                            title="Dokument",
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="documentConfirmingRepresentApplicant",
                                    required=True
                                )
                            ]
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
                    title="Plik",
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
                    title="<small>Art. 43 ustawy z dnia 22 listopada 2018 r. o dokumentach publicznych. <br /><normal>1. Blankiety dokumentów publicznych przechowywane w miejscu ich personalizacji lub indywidualizacji oraz dokumenty publiczne przechowywane w miejscu ich wydawania zabezpiecza się przed dostępem osób nieuprawnionych, utratą, zniszczeniem lub uszkodzeniem. <br /> 2. Pomieszczenie, w którym są przechowywane dokumenty publiczne oraz blankiety tych dokumentów, jest zamykane, a dostęp do tego pomieszczenia mają wyłącznie osoby uprawnione. Jeżeli to pomieszczenie znajduje się na parterze, okna zewnętrzne są zabezpieczone: szybami odpornymi na przebicie lub rozbicie lub stalowymi żaluzjami albo siatkami stalowymi, lub okratowaniem. <br />3. Pomieszczenie, o którym mowa w ust.2, przeznaczone także do wydawania dokumentów publicznych posiada wydzieloną część, w której są przechowywane dokumenty publiczne, zabezpieczoną przed dostępem osób nieuprawnionych. <br />4. Dokumenty publiczne, o których mowa w art. 5 ust. 4, oraz blankiety tych dokumentów mogą być przechowywane w innym pomieszczeniu niż określone w ust. 2, jeżeli są przechowywane w szafie metalowej zamykanej lub w sejfie, do których dostęp mają wyłącznie osoby upoważnione. <br />5. Dostęp do pomieszczenia, o którym mowa w ust. 2, oraz do wydzielonej części pomieszczenia, o której mowa w ust. 3, a także do szafy metalowej zamykanej lub do sejfu, o którym mowa w ust. 4, jest rejestrowany. <br />6. Rejestrowanie dostępu, o którym mowa w ust. 5, może polegać na zamontowaniu systemu kontroli dostępu do pomieszczenia, o którym mowa w ust. 2, i wydzielonej części pomieszczenia, o której mowa w ust. 3, lub prowadzeniu rejestru wejść i wyjść do i z tego pomieszczenia oraz prowadzeniu rejestru wydawania i zwrotu kluczy do tego pomieszczenia i szafy metalowej zamykanej lub do sejfu, o których mowa w ust. 4.</small></normal><br /><small><br />Art. 44. <br /><normal>Dokumenty publiczne będące drukami ścisłego zarachowania oraz blankiety tych dokumentów są ewidencjonowane. Ewidencja dokumentów publicznych i blankietów tych dokumentów oraz dowody ich przekazania i odbioru zabezpiecza się przed dostępem osób nieuprawnionych w sposób przewidziany w art. 43 </small></normal>"
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
