class Prediction:

    def __init__(self):

        # Statistics

        self.similar_events = 0

        self.win_rate = 0.0

        self.avg_return_1d = 0.0
        self.avg_return_3d = 0.0
        self.avg_return_5d = 0.0
        self.avg_return_10d = 0.0
        self.avg_return_30d = 0.0

        self.median_return_5d = 0.0

        self.best_return = 0.0
        self.worst_return = 0.0

        self.std_dev = 0.0

        # Prediction

        self.expected_return = 0.0

        self.direction = "NEUTRAL"

        self.probability_bull = 0.0
        self.probability_bear = 0.0

        self.confidence = 0.0

        # Final Recommendation

        self.recommendation = "WATCH"

        self.reason = ""

    def __str__(self):

        return (
            f"Recommendation : {self.recommendation}\n"
            f"Direction      : {self.direction}\n"
            f"Confidence     : {self.confidence:.1f}%\n"
            f"Bull Probability: {self.probability_bull:.2f}%\n"
            f"Bear Probability: {self.probability_bear:.2f}%\n"
            f"Expected Return: {self.expected_return:.2f}%\n"
            f"Win Rate       : {self.win_rate:.2f}%\n"
            f"Similar Events : {self.similar_events}\n"
            f"Avg 1D Return  : {self.avg_return_1d:.2f}%\n"
            f"Avg 3D Return  : {self.avg_return_3d:.2f}%\n"
            f"Avg 5D Return  : {self.avg_return_5d:.2f}%\n"
            f"Avg 10D Return : {self.avg_return_10d:.2f}%\n"
            f"Avg 30D Return : {self.avg_return_30d:.2f}%\n"
            f"Median 5D      : {self.median_return_5d:.2f}%\n"
            f"Best Return    : {self.best_return:.2f}%\n"
            f"Worst Return   : {self.worst_return:.2f}%\n"
            f"Std Dev        : {self.std_dev:.2f}\n"
            f"Reason         : {self.reason}"
        )