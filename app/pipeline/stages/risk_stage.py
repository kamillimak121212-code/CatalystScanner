from app.risk.risk_engine import RiskEngine


class RiskStage:

    def __init__(self):

        self.engine = RiskEngine()

    def process(self, result):

        result.risk = self.engine.analyze(
            result
        )

        return result