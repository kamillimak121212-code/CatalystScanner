from app.risk.base_risk import BaseRisk


class MacroRisk(BaseRisk):

    def apply(
        self,
        result,
        risk
    ):

        return