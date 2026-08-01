from app.prediction.prediction import Prediction
from app.prediction.statistics_builder import (
    StatisticsBuilder
)


class PredictionEngine:

    def __init__(self):

        self.statistics = StatisticsBuilder()

    def predict(self, history_events):

        prediction = Prediction()

        if not history_events:

            prediction.reason = "No similar events"

            return prediction

        stats = self.statistics.build(
            history_events
        )

        if stats.count == 0:

            prediction.reason = "No statistics"

            return prediction

        prediction.similar_events = stats.count

        prediction.win_rate = stats.win_rate

        prediction.avg_return_1d = stats.avg_1d
        prediction.avg_return_3d = stats.avg_3d
        prediction.avg_return_5d = stats.avg_5d
        prediction.avg_return_10d = stats.avg_10d
        prediction.avg_return_30d = stats.avg_30d

        prediction.median_return_5d = (
            stats.median_5d
        )

        prediction.best_return = stats.best
        prediction.worst_return = stats.worst

        prediction.std_dev = stats.std_dev

        prediction.expected_return = (
            stats.expected_value
        )

        prediction.probability_bull = (
            stats.probability_up
        )

        prediction.probability_bear = (
            100 - stats.probability_up
        )

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        base_confidence = stats.confidence

        sample_bonus = min(
            stats.count * 2,
            20
        )

        prediction.confidence = min(
            base_confidence + sample_bonus,
            100
        )

        # --------------------------------------------------
        # Direction
        # --------------------------------------------------

        if prediction.expected_return >= 0:

            prediction.direction = "BULLISH"

        else:

            prediction.direction = "BEARISH"

        # --------------------------------------------------
        # Recommendation
        # --------------------------------------------------

        if (
            prediction.direction == "BULLISH"
            and prediction.expected_return >= 5
            and prediction.confidence >= 70
        ):

            prediction.recommendation = "BUY"

        elif (
            prediction.direction == "BEARISH"
            and prediction.expected_return <= -5
            and prediction.confidence >= 70
        ):

            prediction.recommendation = "SELL"

        else:

            prediction.recommendation = "WATCH"

        prediction.reason = (
            f"{prediction.similar_events} similar events"
        )

        return prediction