from app.intelligence.models.evaluation import (
    CompanyEvaluation
)


class AssetIntelligenceEngine:

    def evaluate(
        self,
        profile,
        evidence,
        understanding=None
    ):

        text = (
            f"{evidence.title} "
            f"{evidence.description}"
        ).lower()

        evaluation = CompanyEvaluation()

        # --------------------------------------------------
        # Main Company
        # --------------------------------------------------

        if (
            understanding is not None
            and understanding.main_company
            and profile.name
        ):

            detected = understanding.main_company.lower()

            company_names = [

                profile.name.lower(),

                f"{profile.name.lower()} inc",

                f"{profile.name.lower()} inc.",

                f"{profile.name.lower()} ({profile.ticker.lower()})",

                profile.ticker.lower()

            ]

            if any(name in detected for name in company_names):

                evaluation.add(
                    "company",
                    profile.name,
                    100,
                    1.0
                )

        # --------------------------------------------------
        # Products
        # --------------------------------------------------

        if (
            understanding is not None
            and hasattr(profile, "products")
        ):

            counted_products = set()

            for product in profile.products:

                product_name = getattr(
                    product,
                    "name",
                    ""
                ).lower()

                if product_name in counted_products:
                    continue

                names = (
                    product.all_names()
                    if hasattr(product, "all_names")
                    else [product]
                )

                matched = False

                for detected in understanding.products:

                    detected = detected.lower()

                    for name in names:

                        if (
                            detected in name.lower()
                            or name.lower() in detected
                        ):

                            evaluation.add(
                                "product",
                                getattr(product, "name", name),
                                getattr(product, "importance", 5),
                                1.8
                            )

                            counted_products.add(
                                product_name
                            )

                            matched = True
                            break

                    if matched:
                        break

        # --------------------------------------------------
        # Technologies
        # --------------------------------------------------

        if hasattr(profile, "technologies"):

            for technology in profile.technologies:

                if technology.matches(text):

                    evaluation.add(
                        "technology",
                        technology.name,
                        technology.importance,
                        1.6
                    )

        # --------------------------------------------------
        # People
        # --------------------------------------------------

        if hasattr(profile, "people"):

            for person in profile.people:

                if person.matches(text):

                    evaluation.add(
                        "person",
                        person.name,
                        person.importance,
                        2.0
                    )

        # --------------------------------------------------
        # Customers
        # --------------------------------------------------

        self._score_relations(
            profile,
            evaluation,
            understanding,
            profile.customers,
            "customer",
            1.5
        )

        # --------------------------------------------------
        # Suppliers
        # --------------------------------------------------

        self._score_relations(
            profile,
            evaluation,
            understanding,
            profile.suppliers,
            "supplier",
            1.5
        )

        # --------------------------------------------------
        # Competitors
        # --------------------------------------------------

        self._score_relations(
            profile,
            evaluation,
            understanding,
            profile.competitors,
            "competitor",
            1.2
        )

        # --------------------------------------------------
        # Keywords
        # --------------------------------------------------

        for keyword in profile.keywords:

            value = (
                keyword.value
                if hasattr(keyword, "value")
                else keyword
            )

            importance = (
                keyword.importance
                if hasattr(keyword, "importance")
                else 5
            )

            if value.lower() in text:

                evaluation.add(
                    "keyword",
                    value,
                    importance,
                    1.0
                )

        evaluation.finalize()

        return evaluation

    def _score_relations(
        self,
        profile,
        evaluation,
        understanding,
        relations,
        category,
        weight
    ):

        if (
            understanding is None
            or relations is None
        ):
            return

        counted_relations = set()

        for relation in relations:

            relation_name = getattr(
                relation,
                "company",
                ""
            ).lower()

            if relation_name in counted_relations:
                continue

            names = (
                relation.all_names()
                if hasattr(relation, "all_names")
                else [relation]
            )

            matched = False

            for detected in understanding.related_companies:

                detected = detected.lower()

                for name in names:

                    if (
                        detected in name.lower()
                        or name.lower() in detected
                    ):

                        evaluation.add(
                            category,
                            getattr(
                                relation,
                                "company",
                                name
                            ),
                            getattr(
                                relation,
                                "importance",
                                5
                            ),
                            weight
                        )

                        counted_relations.add(
                            relation_name
                        )

                        matched = True
                        break

                if matched:
                    break