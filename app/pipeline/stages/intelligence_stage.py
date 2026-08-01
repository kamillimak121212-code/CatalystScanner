from app.services.intelligence_service import IntelligenceService


class IntelligenceStage:

    def __init__(self):

        self.service = IntelligenceService()

    def process(self, result):

        understanding = result.understanding

        if (
            understanding is not None
            and understanding.relevance_score == 0
        ):
            from app.intelligence.models.evaluation import CompanyEvaluation
            result.evaluation = CompanyEvaluation()
            return result

        result.evaluation = self.service.evaluate(
            result.profile,
            result.evidence,
            understanding
        )

        return result