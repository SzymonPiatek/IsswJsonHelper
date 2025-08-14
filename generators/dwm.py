from classes.form_builder.dwm.promotion.application_builder import PromotionApplicationBuilder
from classes.form_builder.dwm.foreign_scholarship.application_builder import ForeignScholarshipApplicationBuilder


def generate_applications():
    applications = [
        PromotionApplicationBuilder(),
        ForeignScholarshipApplicationBuilder(),
    ]

    for application in applications:
        application.generate()


def generate_reports():
    pass
