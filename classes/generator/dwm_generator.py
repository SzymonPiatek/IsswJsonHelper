from classes.generator.generator import Generator
from classes.form_builder.dwm.promotion.application_builder import PromotionApplicationBuilder
from classes.form_builder.dwm.foreign_scholarship.application_builder import ForeignScholarshipApplicationBuilder


class DWMGenerator(Generator):
    def __init__(self):
        super().__init__(
            applications=[
                PromotionApplicationBuilder(),
                ForeignScholarshipApplicationBuilder(),
            ],
            reports=[]
        )
