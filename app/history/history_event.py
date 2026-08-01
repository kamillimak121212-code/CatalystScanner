from app.history.history_reaction import (
    HistoryReaction
)

from app.history.similarity_result import (
    SimilarityResult
)


class HistoryEvent:

    def __init__(self):

        # Company
        self.company = None

        # Original evidence
        self.evidence = None

        # Event
        self.event_type = ""
        self.category = ""

        # AI Understanding
        self.main_company = ""
        self.products = []
        self.related_companies = []

        self.importance = ""
        self.sentiment = ""

        self.relevance_score = 0
        self.confidence = 0

        # Company Profile
        self.sector = ""
        self.industry = ""

        # Decision
        self.decision = ""
        self.decision_score = 0

        # Date
        self.date = None

        # Company Intelligence
        self.matches = []

        # Catalyst
        self.catalyst_score = 0

        # Market reaction
        self.reaction = HistoryReaction()

        # Similarity
        self.similarity = 0
        self.match_level = "LOW"
        self.similarity_reasons = []

        self.score = 0

    def compare(
        self,
        other
    ):

        result = SimilarityResult()

        # --------------------------------------------------
        # Event Type
        # --------------------------------------------------

        if (
            self.event_type
            and self.event_type == other.event_type
        ):

            result.score += 25
            result.reasons.append("+25 Same event type")

        # --------------------------------------------------
        # Main Company
        # --------------------------------------------------

        if (
            self.main_company
            and other.main_company
            and self.main_company.lower()
            == other.main_company.lower()
        ):

            result.score += 20
            result.reasons.append("+20 Same company")

        # --------------------------------------------------
        # Sentiment
        # --------------------------------------------------

        if (
            self.sentiment
            and other.sentiment
            and self.sentiment == other.sentiment
        ):

            result.score += 10
            result.reasons.append("+10 Same sentiment")

        # --------------------------------------------------
        # Products
        # --------------------------------------------------

        common_products = {
            product.lower()
            for product in self.products
        } & {
            product.lower()
            for product in other.products
        }

        if common_products:

            points = min(
                len(common_products) * 5,
                15
            )

            result.score += points

            result.reasons.append(
                f"+{points} Shared products"
            )

        # --------------------------------------------------
        # Related Companies
        # --------------------------------------------------

        common_companies = {
            company.lower()
            for company in self.related_companies
        } & {
            company.lower()
            for company in other.related_companies
        }

        if common_companies:

            points = min(
                len(common_companies) * 5,
                5
            )

            result.score += points

            result.reasons.append(
                f"+{points} Shared related companies"
            )

        # --------------------------------------------------
        # Company Intelligence
        # --------------------------------------------------

        common_matches = {
            match.lower()
            for match in self.matches
        } & {
            match.lower()
            for match in other.matches
        }

        if common_matches:

            points = min(
                len(common_matches) * 5,
                20
            )

            result.score += points

            result.reasons.append(
                f"+{points} Company intelligence"
            )

        # --------------------------------------------------
        # Catalyst
        # --------------------------------------------------

        difference = abs(
            self.catalyst_score -
            other.catalyst_score
        )

        if difference <= 5:

            result.score += 3
            result.reasons.append("+3 Similar catalyst")

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        difference = abs(
            self.confidence -
            other.confidence
        )

        if difference <= 10:

            result.score += 2
            result.reasons.append("+2 Similar confidence")

        # --------------------------------------------------
        # Match Level
        # --------------------------------------------------

        if result.score >= 70:

            result.level = "HIGH"

        elif result.score >= 40:

            result.level = "MEDIUM"

        else:

            result.level = "LOW"

        return result