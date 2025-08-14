class Generator:
    def __init__(self, applications, reports):
        self.applications = applications
        self.reports = reports

    def generate_applications_and_reports(self):
        self.generate_applications()
        self.generate_report()

    def generate_applications(self):
        for application in self.applications:
            application.generate()

    def generate_report(self):
        for report in self.reports:
            report.generate()
