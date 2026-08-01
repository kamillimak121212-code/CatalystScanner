from app.prediction.prediction_engine import (
    PredictionEngine
)


class PredictionStage:

    def __init__(self):

        self.engine = PredictionEngine()

    def process(self, result):

        result.prediction = self.engine.predict(
            result.history_events
        )

        return result