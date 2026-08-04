from app.scoring.priority_scorer import (
    PriorityScorer
)

from app.logger.logger import logger


class PriorityStage:

    def __init__(self):

        self.scorer = PriorityScorer()

    def process(
        self,
        result
    ):

        score = self.scorer.score(
            result.evidence
        )

        result.priority_score = score

        logger.info(
            f"Priority -> "
            f"{result.evidence.company.ticker} "
            f"{score}"
        )

        return result