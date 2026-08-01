from app.history.history_builder import (
    HistoryBuilder
)

from app.history.history_matcher import (
    HistoryMatcher
)


class HistoryStage:

    def __init__(self):

        self.builder = HistoryBuilder()

        self.matcher = HistoryMatcher()

    def process(self, result):

        current_history = self.builder.build(
            result
        )

        result.history_events = self.matcher.find_similar(
            current_history
        )

        return result