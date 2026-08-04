class PriorityScorer:

    def score(
        self,
        evidence
    ):

        score = 0

        # ----------------------------------
        # Source
        # ----------------------------------

        if evidence.source.name == "SEC":
            score += 40

        elif evidence.source.name == "RSS":
            score += 20

        # ----------------------------------
        # SEC Forms
        # ----------------------------------

        if "8-K" in evidence.title:
            score += 30

        elif "10-Q" in evidence.title:
            score += 25

        elif "10-K" in evidence.title:
            score += 25

        # ----------------------------------
        # Keywords
        # ----------------------------------

        text = (
            f"{evidence.title} "
            f"{evidence.description}"
        ).lower()

        keywords = {

            "earnings": 25,
            "guidance": 20,
            "contract": 20,
            "partnership": 20,
            "acquisition": 30,
            "merger": 30,
            "buyback": 20,
            "dividend": 15,
            "ceo": 15,
            "lawsuit": 20,
            "fda": 25

        }

        for word, points in keywords.items():

            if word in text:

                score += points

        return score