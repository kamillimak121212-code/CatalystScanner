from datetime import datetime


class Narrative:

    def __init__(self):

        self.title = ""

        self.summary = ""

        self.drivers = []

        self.companies = []

        self.confidence = 0

        # Wszystkie Evidence należące
        # do tej narracji
        self.evidence = []

        # Historia zmian
        self.history = []

        # Kiedy powstała
        self.created_at = datetime.now()

        # Ostatnia aktualizacja
        self.last_updated = datetime.now()

    def add_evidence(self, evidence):

        self.evidence.append(evidence)

        self.last_updated = datetime.now()

    def add_history(self, text):

        self.history.append(
            {
                "time": datetime.now(),
                "text": text
            }
        )

        self.last_updated = datetime.now()

    def __str__(self):

        return (
            f"Title        : {self.title}\n"
            f"Summary      : {self.summary}\n"
            f"Companies    : {', '.join(self.companies)}\n"
            f"Confidence   : {self.confidence}%\n"
            f"Evidence     : {len(self.evidence)}\n"
            f"History      : {len(self.history)}\n"
            f"Last Update  : {self.last_updated}"
        )