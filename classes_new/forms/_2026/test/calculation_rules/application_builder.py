from classes_new.form_builder.form_builder import ApplicationFormBuilder


class CalculationRulesApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parts = []

        """
        Calculation rules:
        
        [ ] sumInputs
        [ ] multiplyInputs
        [ ] copyValue
        [ ] copyLocalValue
        [ ] copyTitle
        [ ] sumsShareCalculator
        [ ] shareCalculator
        [ ] localShareCalculator
        [ ] singlePositionShareCalculator
        [ ] assignValue
        [ ] lastDate
        [ ] firstDate
        [ ] relateToDate
        [ ] relateToLastDate
        [ ] halfwayDate
        [ ] dynamicSumInputs
        [ ] multiplyValues
        [ ] localSum
        [ ] getNBPCurrency
        [ ] conditionalCopyValue
        [ ] copyCompanyData
        [ ] sumInvoiceCosts
        """
