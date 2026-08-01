from app.intelligence.asset_profile import (
    AssetProfile
)


class WTIProfile(AssetProfile):

    def __init__(self):

        super().__init__()

        self.symbol = "WTI"
        self.name = "WTI Crude Oil"

        self.asset_type = "COMMODITY"

        self.sector = "Energy"

        self.keywords = [

            "wti",
            "crude oil",
            "oil",
            "brent",

            "opec",
            "opec+",

            "eia",
            "inventory",
            "inventories",

            "production",
            "output",

            "saudi arabia",
            "russia",
            "iran",
            "iraq",

            "pipeline",
            "refinery",

            "hurricane",

            "sanctions",

            "spr",

            "demand",
            "supply"

        ]

        self.catalysts = [

            "OPEC Meeting",
            "Production Cut",
            "Production Increase",
            "EIA Inventory",
            "SPR Release",
            "Sanctions",
            "War",
            "Pipeline Outage",
            "Hurricane",
            "Demand Forecast"

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

            if keyword in text:

                score += 5
                matches.append(keyword)

        return {

            "score": min(score, 100),

            "matches": matches

        }