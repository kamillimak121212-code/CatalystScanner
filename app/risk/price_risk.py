from app.history.price_history_repository import (
    PriceHistoryRepository
)

from app.risk.base_risk import BaseRisk


class PriceRisk(BaseRisk):

    def __init__(self):

        self.repository = PriceHistoryRepository()

    def apply(
        self,
        result,
        risk
    ):

        history = self.repository.get_history(
            result.evidence.company.ticker,
            20
        )

        if len(history) < 20:
            return

        # Brak danych o cenach
        if (
            history[0][4] is None
            or history[-6][4] is None
            or history[-1][4] is None
        ):
            return

        latest_close = float(history[-1][4])

        close_5d = float(history[-6][4])

        close_20d = float(history[0][4])

        change_5d = (
            (latest_close - close_5d)
            / close_5d
            * 100
        )

        change_20d = (
            (latest_close - close_20d)
            / close_20d
            * 100
        )

        if change_5d >= 10:

            risk.add(
                15,
                f"Price +{change_5d:.1f}% in last 5 days"
            )

        elif change_5d >= 5:

            risk.add(
                8,
                f"Price +{change_5d:.1f}% in last 5 days"
            )

        if change_20d >= 25:

            risk.add(
                20,
                f"Price +{change_20d:.1f}% in last 20 days"
            )

        elif change_20d >= 15:

            risk.add(
                10,
                f"Price +{change_20d:.1f}% in last 20 days"
            )