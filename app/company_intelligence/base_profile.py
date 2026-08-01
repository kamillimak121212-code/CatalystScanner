from app.company_intelligence.results.evaluation_result import (
    EvaluationResult
)


class CompanyProfile:

    def __init__(self):

        self.people = []
        self.products = []
        self.customers = []
        self.suppliers = []
        self.partners = []
        self.competitors = []
        self.technologies = []
        self.macro_factors = []
        self.catalysts = []

        self.knowledge = []

    def build_knowledge(self):

        self.knowledge = (
            self.people
            + self.products
            + self.customers
            + self.suppliers
            + self.partners
            + self.competitors
            + self.technologies
            + self.catalysts
        )

    def evaluate(self, obj):

        self.build_knowledge()

        title = getattr(obj, "title", "")
        text_body = getattr(obj, "summary", None)

        if text_body is None:
            text_body = getattr(obj, "description", "")

        text = f"{title} {text_body}".lower()

        result = EvaluationResult()

        for item in self.knowledge:

            if self._matches_item(text, item):

                result.add_match(
                    item.category,
                    item
                )

        return result

    def _matches_item(self, text, item):

        # Match by official name

        if item.name.lower() in text:
            return True

        # Match by aliases

        for alias in item.aliases:

            if alias.lower() in text:
                return True

        return False

    def to_prompt(self):

        def names(items):
            return ", ".join(
                item.name
                for item in items
            )

        return f"""
COMPANY PROFILE

People:
{names(self.people)}

Products:
{names(self.products)}

Customers:
{names(self.customers)}

Suppliers:
{names(self.suppliers)}

Partners:
{names(self.partners)}

Competitors:
{names(self.competitors)}

Technologies:
{names(self.technologies)}

Catalysts:
{names(self.catalysts)}
"""