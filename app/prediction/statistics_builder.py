from statistics import mean, median, pstdev

from app.prediction.history_statistics import (
    HistoryStatistics
)


class StatisticsBuilder:

    def build(self, history_events):

        stats = HistoryStatistics()

        if not history_events:
            return stats

        returns_1d = []
        returns_3d = []
        returns_5d = []
        returns_10d = []
        returns_30d = []

        for event in history_events:

            if event.reaction is None:
                continue

            if event.reaction.change_1d is not None:
                returns_1d.append(
                    event.reaction.change_1d
                )

            if event.reaction.change_3d is not None:
                returns_3d.append(
                    event.reaction.change_3d
                )

            if event.reaction.change_5d is not None:
                returns_5d.append(
                    event.reaction.change_5d
                )

            if event.reaction.change_10d is not None:
                returns_10d.append(
                    event.reaction.change_10d
                )

            if event.reaction.change_30d is not None:
                returns_30d.append(
                    event.reaction.change_30d
                )

        if not returns_5d:
            return stats

        stats.count = len(returns_5d)

        stats.avg_1d = round(
            mean(returns_1d),
            2
        ) if returns_1d else 0

        stats.avg_3d = round(
            mean(returns_3d),
            2
        ) if returns_3d else 0

        stats.avg_5d = round(
            mean(returns_5d),
            2
        )

        stats.avg_10d = round(
            mean(returns_10d),
            2
        ) if returns_10d else 0

        stats.avg_30d = round(
            mean(returns_30d),
            2
        ) if returns_30d else 0

        stats.median_5d = round(
            median(returns_5d),
            2
        )

        stats.best = round(
            max(returns_5d),
            2
        )

        stats.worst = round(
            min(returns_5d),
            2
        )

        stats.std_dev = round(
            pstdev(returns_5d),
            2
        )

        # --------------------------------------------------
        # Bull / Bear statistics
        # --------------------------------------------------

        bullish = len([
            r for r in returns_5d
            if r > 0
        ])

        bearish = len([
            r for r in returns_5d
            if r < 0
        ])

        neutral = len([
            r for r in returns_5d
            if r == 0
        ])

        total = len(returns_5d)

        stats.win_rate = round(
            bullish / total * 100,
            2
        )

        stats.probability_up = round(
            bullish / total * 100,
            2
        )

        stats.probability_down = round(
            bearish / total * 100,
            2
        )

        stats.neutral_probability = round(
            neutral / total * 100,
            2
        )

        stats.expected_value = round(
            mean(returns_5d),
            2
        )

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        confidence = min(
            stats.count * 4,
            40
        )

        if abs(stats.expected_value) >= 3:
            confidence += 15

        if abs(stats.expected_value) >= 6:
            confidence += 10

        if stats.std_dev <= 3:
            confidence += 20

        elif stats.std_dev <= 6:
            confidence += 10

        if stats.win_rate >= 70:
            confidence += 15

        elif stats.win_rate >= 60:
            confidence += 10

        stats.confidence = min(
            100,
            confidence
        )

        return stats