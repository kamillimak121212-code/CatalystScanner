from app.decision.decision_engine import (
    DecisionEngine
)


class DecisionStage:

    def __init__(self):

        self.engine = DecisionEngine()

    def process(self, result):

        result.decision = self.engine.decide(
            result
        )

        return result