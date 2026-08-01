from app.history.history_reaction import HistoryReaction
from app.history.price_history_repository import (
    PriceHistoryRepository
)


class HistoryReactionBuilder:

    def __init__(self):

        self.repository = PriceHistoryRepository()

    def build(
        self,
        ticker,
        trading_day
    ):

        prices = self.repository.get_next_prices(
            ticker,
            trading_day
        )

        if len(prices) < 2:
            return None

        reaction = HistoryReaction()

        reaction.price_before = float(prices[0][1])

        self._fill(
            reaction,
            prices
        )

        return reaction

    def _fill(
        self,
        reaction,
        prices
    ):

        base = reaction.price_before

        mapping = {
            1: "1d",
            3: "3d",
            5: "5d",
            10: "10d",
            30: "30d"
        }

        for index, suffix in mapping.items():

            if index >= len(prices):
                continue

            close = float(prices[index][1])

            setattr(
                reaction,
                f"price_{suffix}",
                close
            )

            change = (
                (close - base)
                / base
            ) * 100

            setattr(
                reaction,
                f"change_{suffix}",
                round(change, 2)
            )