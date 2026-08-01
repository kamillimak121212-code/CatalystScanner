from app.intelligence.models.evaluation import (
    CompanyEvaluation
)


class CompanyProfile:

    def __init__(self):

        self.ticker = ""
        self.name = ""
        self.sector = ""
        self.industry = ""
        self.description = ""

        self.products = []
        self.customers = []
        self.suppliers = []
        self.competitors = []

        self.technologies = []

        self.people = []

        self.catalysts = []
        self.risks = []

        self.keywords = []

    def evaluate(self, evidence):

        evaluation = CompanyEvaluation()

        text = (
            evidence.title + " " +
            evidence.description
        ).lower()

        for keyword in self.keywords:

            if keyword.value.lower() in text:

                evaluation.score += keyword.importance

                evaluation.matches.append(
                    keyword.value
                )

        evaluation.reason = ", ".join(
            evaluation.matches
        )

        return evaluation

    def to_prompt(self):

        return f"""
Company: {self.name}

Sector: {self.sector}

Industry: {self.industry}

Description:
{self.description}
"""