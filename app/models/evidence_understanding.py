class EvidenceUnderstanding:

    def __init__(
        self,
        summary="",
        main_company="",
        event="",
        event_type="UNKNOWN",
        sentiment="NEUTRAL",
        reason="",
        related_companies=None,
        products=None,
        impact="Neutral",
        is_relevant=False,
        relevance_reason="",
        relevance_score=0,
        confidence=0
    ):

        # AI Summary
        self.summary = summary

        # Company
        self.main_company = main_company

        # Human readable event
        self.event = event

        # Structured event
        self.event_type = event_type

        # POSITIVE / NEGATIVE / NEUTRAL
        self.sentiment = sentiment

        # AI reasoning
        self.reason = reason

        # Mentioned companies
        self.related_companies = related_companies or []

        # Mentioned products
        self.products = products or []

        # Human impact description
        self.impact = impact

        # Relevance
        self.is_relevant = is_relevant

        self.relevance_reason = relevance_reason

        self.relevance_score = relevance_score

        # Confidence (0-100)
        self.confidence = confidence

    def __str__(self):

        companies = ", ".join(self.related_companies)
        if not companies:
            companies = "None"

        products = ", ".join(self.products)
        if not products:
            products = "None"

        return (
            f"Relevant         : {self.is_relevant}\n"
            f"Confidence       : {self.confidence}\n"
            f"Relevance Score  : {self.relevance_score}\n"
            f"Main Company     : {self.main_company}\n"
            f"Event Type       : {self.event_type}\n"
            f"Sentiment        : {self.sentiment}\n"
            f"Event            : {self.event}\n"
            f"Impact           : {self.impact}\n"
            f"Related Companies: {companies}\n"
            f"Products         : {products}\n"
            f"Summary          : {self.summary}\n"
            f"Reason           : {self.reason}\n"
            f"Relevance Reason : {self.relevance_reason}"
        )