class HistoryAnalyzer:

    def analyze(self, events):

        if not events:
            return None

        valid_events = []

        for event in events:

            if (
                event.reaction is None
                or event.reaction.change_5d is None
            ):
                continue

            valid_events.append(event)

        if not valid_events:
            return None

        total = len(valid_events)

        win_1d = 0

        avg_1d = 0
        avg_3d = 0
        avg_5d = 0
        avg_10d = 0
        avg_30d = 0

        best = -999
        worst = 999

        for event in valid_events:

            reaction = event.reaction

            avg_1d += reaction.change_1d or 0
            avg_3d += reaction.change_3d or 0
            avg_5d += reaction.change_5d or 0
            avg_10d += reaction.change_10d or 0
            avg_30d += reaction.change_30d or 0

            if (reaction.change_5d or 0) > 0:
                win_1d += 1

            best = max(best, reaction.change_5d or 0)
            worst = min(worst, reaction.change_5d or 0)

        return {

            "count": total,

            "win_rate": round(
                win_1d / total * 100,
                1
            ),

            "avg_1d": round(avg_1d / total, 2),

            "avg_3d": round(avg_3d / total, 2),

            "avg_5d": round(avg_5d / total, 2),

            "avg_10d": round(avg_10d / total, 2),

            "avg_30d": round(avg_30d / total, 2),

            "best": round(best, 2),

            "worst": round(worst, 2)

        }