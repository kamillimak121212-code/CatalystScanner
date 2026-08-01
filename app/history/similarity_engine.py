class SimilarityEngine:

    def calculate(
        self,
        current,
        historical
    ):

        score = 0
        reasons = []

        score += self._event_score(
            current,
            historical,
            reasons
        )

        score += self._company_score(
            current,
            historical,
            reasons
        )

        score += self._product_score(
            current,
            historical,
            reasons
        )

        score += self._relation_score(
            current,
            historical,
            reasons
        )

        score += self._intelligence_score(
            current,
            historical,
            reasons
        )

        score += self._catalyst_score(
            current,
            historical,
            reasons
        )

        score += self._sentiment_score(
            current,
            historical,
            reasons
        )

        score += self._confidence_score(
            current,
            historical,
            reasons
        )

        historical.similarity = min(score, 100)
        historical.similarity_reasons = reasons

        if historical.similarity >= 70:
            historical.match_level = "HIGH"

        elif historical.similarity >= 40:
            historical.match_level = "MEDIUM"

        else:
            historical.match_level = "LOW"

        return historical.similarity

    # --------------------------------------------------

    def _event_score(
        self,
        current,
        historical,
        reasons
    ):

        if not current.event:
            return 0

        event_type = current.event.get("event_type")

        if (
            event_type
            and event_type.value == historical.event_type
        ):

            reasons.append("+25 Same event type")

            return 25

        return 0

    # --------------------------------------------------

    def _company_score(
        self,
        current,
        historical,
        reasons
    ):

        if (
            current.understanding
            and current.understanding.main_company
            and historical.main_company
        ):

            if (
                current.understanding.main_company.lower()
                ==
                historical.main_company.lower()
            ):

                reasons.append("+20 Same company")

                return 20

        return 0

    # --------------------------------------------------

    def _product_score(
        self,
        current,
        historical,
        reasons
    ):

        if not current.understanding:
            return 0

        current_products = {
            p.lower()
            for p in current.understanding.products
        }

        historical_products = {
            p.lower()
            for p in historical.products
        }

        common = (
            current_products &
            historical_products
        )

        points = min(
            len(common) * 5,
            15
        )

        if points:

            reasons.append(
                f"+{points} Shared products"
            )

        return points

    # --------------------------------------------------

    def _relation_score(
        self,
        current,
        historical,
        reasons
    ):

        if not current.understanding:
            return 0

        current_companies = {
            c.lower()
            for c in current.understanding.related_companies
        }

        historical_companies = {
            c.lower()
            for c in historical.related_companies
        }

        common = (
            current_companies &
            historical_companies
        )

        points = min(
            len(common) * 5,
            5
        )

        if points:

            reasons.append(
                f"+{points} Related companies"
            )

        return points

    # --------------------------------------------------

    def _intelligence_score(
        self,
        current,
        historical,
        reasons
    ):

        if current.evaluation is None:
            return 0

        current_matches = {

            match["name"].lower()

            for match in current.evaluation.matches

        }

        historical_matches = {

            match.lower()

            for match in historical.matches

        }

        common = (
            current_matches &
            historical_matches
        )

        points = min(
            len(common) * 5,
            20
        )

        if points:

            reasons.append(
                f"+{points} Company intelligence"
            )

        return points

    # --------------------------------------------------

    def _catalyst_score(
        self,
        current,
        historical,
        reasons
    ):

        difference = abs(
            current.catalyst_score -
            historical.catalyst_score
        )

        if difference <= 5:

            reasons.append("+3 Similar catalyst")

            return 3

        return 0

    # --------------------------------------------------

    def _sentiment_score(
        self,
        current,
        historical,
        reasons
    ):

        if (
            current.sentiment
            and historical.sentiment
            and current.sentiment.name
            == historical.sentiment
        ):

            reasons.append("+10 Same sentiment")

            return 10

        return 0

    # --------------------------------------------------

    def _confidence_score(
        self,
        current,
        historical,
        reasons
    ):

        if not current.understanding:
            return 0

        difference = abs(
            current.understanding.confidence -
            historical.confidence
        )

        if difference <= 10:

            reasons.append("+2 Similar confidence")

            return 2

        return 0