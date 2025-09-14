from classes.form_builder.components.component.dpf_component import DPFComponent
from classes.form_builder.form_builder_base import FormBuilderBase


class ApplicationStatements(FormBuilderBase):
    def __init__(self):
        super().__init__()

        self.component = DPFComponent()

    def script_meet_bechdel_test_criteria(self):
        return self.create_chapter(
            title="Badanie prowadzone jest dla celów naukowych i nie ma wpływu na ocenę wniosku",
            components=[
                self.create_component(
                    component_type="radio",
                    label="Czy scenariusz spełnia kryterium testu Bechdel",
                    name="scriptMeetBechdelTestCriteria",
                    options=[
                        "Tak", "Nie"
                    ],
                    required=True
                )
            ]
        )

    def storage_of_blank_public_documents(self):
        return self.create_chapter(
            title="Przechowywanie blankietów dokumentów publicznych oraz dokumentów publicznych",
            components=[
                self.create_chapter(
                    title="<small>Art. 43 ustawy z dnia 22 listopada 2018 r. o dokumentach publicznych. <br /><normal>1. Blankiety dokumentów publicznych przechowywane w miejscu ich personalizacji lub indywidualizacji oraz dokumenty publiczne przechowywane w miejscu ich wydawania zabezpiecza się przed dostępem osób nieuprawnionych, utratą, zniszczeniem lub uszkodzeniem. <br /> 2. Pomieszczenie, w którym są przechowywane dokumenty publiczne oraz blankiety tych dokumentów, jest zamykane, a dostęp do tego pomieszczenia mają wyłącznie osoby uprawnione. Jeżeli to pomieszczenie znajduje się na parterze, okna zewnętrzne są zabezpieczone: szybami odpornymi na przebicie lub rozbicie lub stalowymi żaluzjami albo siatkami stalowymi, lub okratowaniem. <br />3. Pomieszczenie, o którym mowa w ust.2, przeznaczone także do wydawania dokumentów publicznych posiada wydzieloną część, w której są przechowywane dokumenty publiczne, zabezpieczoną przed dostępem osób nieuprawnionych. <br />4. Dokumenty publiczne, o których mowa w art. 5 ust. 4, oraz blankiety tych dokumentów mogą być przechowywane w innym pomieszczeniu niż określone w ust. 2, jeżeli są przechowywane w szafie metalowej zamykanej lub w sejfie, do których dostęp mają wyłącznie osoby upoważnione. <br />5. Dostęp do pomieszczenia, o którym mowa w ust. 2, oraz do wydzielonej części pomieszczenia, o której mowa w ust. 3, a także do szafy metalowej zamykanej lub do sejfu, o którym mowa w ust. 4, jest rejestrowany. <br />6. Rejestrowanie dostępu, o którym mowa w ust. 5, może polegać na zamontowaniu systemu kontroli dostępu do pomieszczenia, o którym mowa w ust. 2, i wydzielonej części pomieszczenia, o której mowa w ust. 3, lub prowadzeniu rejestru wejść i wyjść do i z tego pomieszczenia oraz prowadzeniu rejestru wydawania i zwrotu kluczy do tego pomieszczenia i szafy metalowej zamykanej lub do sejfu, o których mowa w ust. 4.</small></normal><br /><small>Art. 44. <br /><normal>Dokumenty publiczne będące drukami ścisłego zarachowania oraz blankiety tych dokumentów są ewidencjonowane. Ewidencja dokumentów publicznych i blankietów tych dokumentów oraz dowody ich przekazania i odbioru zabezpiecza się przed dostępem osób nieuprawnionych w sposób przewidziany w art. 43 </small></normal>"
                )
            ]
        )

    def applicant_statements(self):
        return self.create_chapter(
            title="Oświadczenia wnioskodawcy",
            components=[
                self.component.application_statements.statement_act_on_cinematography(),
                self.component.application_statements.statement_necessary_resources(),
                self.component.application_statements.statement_article_twenty_two(),
                self.component.application_statements.statement_not_in_arrears(),
                self.component.application_statements.statement_pay_social_security(),
                self.component.application_statements.applicants_statement_of_no_ties()
            ]
        )

    def producer_statements(self):
        return self.create_chapter(
            title="Oświadczenia producenta",
            components=[
                self.create_chapter(
                    title="Jako producent oświadczam, że zapewnię, że dystrybucja filmu będzie odbywała się na zasadach zapewniających jak najszerszy, powszechny dostęp do filmu dofinansowanego przez PISF w szczególności z uwzględnieniem następujących zasad:",
                    components=[
                        self.component.application_statements.producer_statement_screening_to_all_cinemas(),
                        self.component.application_statements.screening_requirement_no_more_than_two(),
                        self.component.application_statements.film_had_no_public_screening()
                    ]
                )
            ]
        )

    def script_statements(self):
        return self.create_chapter(
            title="Oświadczenie dot. scenariusza",
            components=[
                self.script_meet_bechdel_test_criteria()
            ]
        )
