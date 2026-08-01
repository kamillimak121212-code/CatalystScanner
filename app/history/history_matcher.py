from app.history.history_repository import (
    HistoryRepository
)


class HistoryMatcher:

    def __init__(self):

        self.repository = HistoryRepository()

    def find_similar(
        self,
        current_history
    ):

        matches = self.repository.find_similar(
            current_history
        )

        matches.sort(
            key=lambda x: x.similarity,
            reverse=True
        )

        return matches[:10]