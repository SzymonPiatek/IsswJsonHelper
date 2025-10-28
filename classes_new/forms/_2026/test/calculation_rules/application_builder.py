from classes_new.form_builder.form_builder import ApplicationFormBuilder


class CalculationRulesApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/calculation_rules",
            custom_file_name="calculation_rules"
        )

        self.form_id = self.set_ids(
            local_id=16416,
            uat_id=None
        )

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
