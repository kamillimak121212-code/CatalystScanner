from app.intelligence.asset_profile import (
    AssetProfile
)


class GoldProfile(AssetProfile):

    def __init__(self):

        super().__init__()

        self.symbol = "XAUUSD"
        self.name = "Gold"

        self.asset_type = "COMMODITY"

        self.sector = "Precious Metals"

        self.keywords = [

            "gold",
            "xau",
            "bullion",
            "precious metals",

            "fed",
            "fomc",
            "powell",

            "cpi",
            "ppi",
            "inflation",

            "interest rates",
            "rate cut",
            "rate hike",

            "treasury",
            "bond yield",
            "real yields",

            "dollar",
            "usd",

            "safe haven",

            "central bank",

            "geopolitics",
            "war"

        ]

        self.catalysts = [

            "FED",
            "CPI",
            "PPI",
            "NFP",
            "Inflation",
            "Rate Cut",
            "Rate Hike",
            "Treasury Yield",
            "Dollar Strength",
            "Safe Haven",
            "Geopolitical Risk"

        ]

    def evaluate(
        self,
        evidence,
        understanding=None
    ):

        text = (
            f"{evidence.title} "
            f"{evidence.description}"
        ).lower()

        score = 0
        matches = []

        for keyword in self.keywords:

            if keyword.lower() in text:

                score += 5
                matches.append(keyword)

        return {

            "score": min(score, 100),

            "matches": matches

        }