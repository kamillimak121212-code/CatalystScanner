class IntelligenceService:

    def evaluate(
        self,
        profile,
        evidence,
        understanding
    ):

        if profile is None:
            return None

        return profile.evaluate(
            evidence,
            understanding
        )