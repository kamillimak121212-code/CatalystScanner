from app.services.importance_engine import (
    calculate_importance
)


class ImportanceStage:

    def process(self, result):

        result.importance = calculate_importance(
            result.understanding,
            result.evaluation
        )

        return result