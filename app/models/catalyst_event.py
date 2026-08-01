class CatalystEvent:

    def __init__(
        self,
        company,
        title,
        category,
        theme="UNKNOWN"
    ):

        self.company = company

        self.name = theme          # nazwa wydarzenia

        self.title = title         # pierwszy artykuł

        self.category = category

        self.theme = theme

        self.evidence = []

        self.analysis = None

    def add_evidence(self, evidence):

        self.evidence.append(evidence)

        # zawsze aktualizujemy tytuł na najnowszy artykuł
        self.title = evidence.title

    def evidence_count(self):

        return len(self.evidence)

    def __str__(self):

        return (
            f"Company : {self.company.ticker}\n"
            f"Event   : {self.name}\n"
            f"Title   : {self.title}\n"
            f"Category: {self.category}\n"
            f"Evidence: {self.evidence_count()}"
        )