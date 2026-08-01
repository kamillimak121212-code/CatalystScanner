from app.risk.risk import Risk

from app.risk.macro_risk import MacroRisk
from app.risk.price_risk import PriceRisk


class RiskEngine:

    def __init__(self):

        self.modules = [

            MacroRisk(),

            PriceRisk()

        ]

    def analyze(self, result):

        risk = Risk()

        for module in self.modules:

            module.apply(
                result,
                risk
            )

        if risk.score >= 70:

            risk.level = "HIGH"

        elif risk.score >= 40:

            risk.level = "MEDIUM"

        else:

            risk.level = "LOW"

        return risk