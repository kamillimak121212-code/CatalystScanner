from app.history.history_builder import HistoryBuilder
from app.history.history_repository import HistoryRepository


class HistorySaveStage:

    def __init__(self):

        self.builder = HistoryBuilder()
        self.repository = HistoryRepository()

    def process(self, result):

        history = self.builder.build(result)

        self.repository.add(history)

        return result