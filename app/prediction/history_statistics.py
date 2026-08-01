class HistoryStatistics:

    def __init__(self):

        self.count = 0

        # Historical statistics

        self.win_rate = 0.0

        self.avg_1d = 0.0
        self.avg_3d = 0.0
        self.avg_5d = 0.0
        self.avg_10d = 0.0
        self.avg_30d = 0.0

        self.median_5d = 0.0

        self.best = 0.0
        self.worst = 0.0

        self.std_dev = 0.0

        # Prediction

        self.expected_value = 0.0

        # Direction probabilities

        self.probability_up = 0.0
        self.probability_down = 0.0
        self.neutral_probability = 0.0

        # Final confidence

        self.confidence = 0.0