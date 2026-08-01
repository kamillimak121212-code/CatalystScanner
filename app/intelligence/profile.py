from app.intelligence.asset_profile import (
    AssetProfile
)

from app.intelligence.models.evaluation import (
    CompanyEvaluation
)


class CompanyProfile(AssetProfile):

    def __init__(self):

        super().__init__()

        # Basic
        self.ticker = ""
        self.name = ""
        self.sector = ""
        self.industry = ""
        self.description = ""

        # Business
        self.products = []
        self.customers = []
        self.suppliers = []
        self.competitors = []

        # Technology
        self.technologies = []

        # Management
        self.people = []

        # Investment
        self.catalysts = []
        self.risks = []

        # AI
        self.keywords = []

    def evaluate(
        self,
        evidence,
        understanding=None
    ):

        text = (
            f"{evidence.title} "
            f"{evidence.description}"
        ).lower()

        evaluation = CompanyEvaluation()

        # --------------------------------------------------
        # AI Main Company
        # --------------------------------------------------

        self._score_main_company(
            evaluation,
            understanding
        )

        # --------------------------------------------------
        # Keyword matching
        # --------------------------------------------------

        self._score_keywords(
            text,
            evaluation
        )

        # --------------------------------------------------
        # Technology matching
        # --------------------------------------------------

        self._score_objects(
            self.technologies,
            evaluation,
            text,
            "technology",
            "name",
            1.6
        )

        # --------------------------------------------------
        # People matching
        # --------------------------------------------------

        self._score_objects(
            self.people,
            evaluation,
            text,
            "person",
            "name",
            2.0
        )

        # --------------------------------------------------
        # AI Understanding
        # --------------------------------------------------

        if understanding is not None:

            self._score_products(
                evaluation,
                understanding.products
            )

            self._score_relations(
                self.customers,
                evaluation,
                understanding.related_companies,
                "customer",
                1.5
            )

            self._score_relations(
                self.suppliers,
                evaluation,
                understanding.related_companies,
                "supplier",
                1.5
            )

            self._score_relations(
                self.competitors,
                evaluation,
                understanding.related_companies,
                "competitor",
                1.2
            )

        evaluation.finalize()

        return evaluation

    def _score_main_company(
        self,
        evaluation,
        understanding
    ):

        if understanding is None:
            return

        if not understanding.main_company:
            return

        if (
            understanding.main_company.lower()
            == self.name.lower()
        ):

            evaluation.add(
                "company",
                self.name,
                100,
                1.0
            )

    def _score_keywords(
        self,
        text,
        evaluation
    ):

        for keyword in self.keywords:

            if keyword.value.lower() in text:

                evaluation.add(
                    "keyword",
                    keyword.value,
                    keyword.importance,
                    1.0
                )

    def _score_objects(
        self,
        objects,
        evaluation,
        text,
        category,
        attribute,
        weight
    ):

        for obj in objects:

            if obj.matches(text):

                evaluation.add(
                    category,
                    getattr(obj, attribute),
                    obj.importance,
                    weight
                )

    def _score_products(
        self,
        evaluation,
        detected_products
    ):

        for product in self.products:

            for detected in detected_products:

                detected = detected.lower()

                for name in product.all_names():

                    if (
                        detected in name.lower()
                        or
                        name.lower() in detected
                    ):

                        evaluation.add(
                            "product",
                            product.name,
                            product.importance,
                            1.8
                        )

                        break

    def _score_relations(
        self,
        relations,
        evaluation,
        detected_companies,
        category,
        weight
    ):

        for relation in relations:

            for detected in detected_companies:

                detected = detected.lower()

                for name in relation.all_names():

                    if (
                        detected in name.lower()
                        or
                        name.lower() in detected
                    ):

                        evaluation.add(
                            category,
                            relation.company,
                            relation.importance,
                            weight
                        )

                        break

    def to_prompt(self):

        return f"""
Company: {self.name}
Sector: {self.sector}
Industry: {self.industry}
Description: {self.description}
"""