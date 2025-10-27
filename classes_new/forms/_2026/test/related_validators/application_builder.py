from classes_new.form_builder.form_builder import ApplicationFormBuilder


class RelatedValidatorsApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/related_validators",
            custom_file_name="related_validators"
        )

        self.parts = []

        """
        Related validators:
        
        [x] RelatedEqualityValidator
        [x] RelatedLocalEqualityValidator
        [x] RelatedNumericEqualityValidator
        [x] RelatedRequiredIfEqualValidator
        [x] RelatedDateLTEValidator
        [x] RelatedLocalDateLTEValidator
        [x] RelatedDateGTEValidator
        [x] RelatedLocalDateGTEValidator
        [x] RelatedDateOffsetValidator
        [x] RelatedDateIncrementValidator
        [x] RelatedSumValidator
        [x] RelatedMultiplicationValidator
        [ ] RelatedLocalMultiplicationValidator
        [x] RelatedShareValidator
        [x] RelatedLocalDivisionValidator
        [x] RelatedMapValidator
        [x] RelatedBooleanSumValidator
        [x] RelatedSumOfWeightsValidator
        [x] RelatedEqualIfInRangeValidator
        [x] RelatedEmptyIfValidator
        [x] RelatedFractionValidator
        [x] RelatedFractionGTEValidator
        [x] RelatedFractionLTEValidator
        [x] RelatedLocalSumValidator
        [x] RelatedAnyOfValidator
        [x] RelatedMappedLimitValidator
        [x] RelatedAllowedOptionsValidator
        [x] RelatedUniqueValueValidator
        [ ] RelatedConditionRatioValidator
        [ ] RelatedConditionRangeValidator
        [x] RelatedLastDateValidator
        """
