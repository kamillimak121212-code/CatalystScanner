from app.models.evidence import EvidenceImportance


class CatalystStage:

    def process(self, result):

        score = 0

        if result.understanding is None:
            result.catalyst_score = 0
            return result

        if not result.understanding.is_relevant:
            result.catalyst_score = 0
            return result

        # --------------------------------------------------
        # AI relevance
        # --------------------------------------------------

        score += (
            result.understanding.relevance_score * 0.35
        )

        # --------------------------------------------------
        # Company Intelligence
        # --------------------------------------------------

        if result.evaluation:

            score += (
                result.evaluation.score * 0.35
            )

        # --------------------------------------------------
        # Importance
        # --------------------------------------------------

        if result.importance == EvidenceImportance.CRITICAL:

            score += 30

        elif result.importance == EvidenceImportance.HIGH:

            score += 20

        elif result.importance == EvidenceImportance.MEDIUM:

            score += 10

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        score += (
            result.understanding.confidence * 0.10
        )

        # --------------------------------------------------
        # Sentiment adjustment
        # --------------------------------------------------

        sentiment = (
            result.understanding.sentiment
        )

        if sentiment == "POSITIVE":

            score += 10

        elif sentiment == "NEGATIVE":

            score -= 15

        # --------------------------------------------------

        result.catalyst_score = max(
            0,
            min(
                round(score),
                100
            )
        )

        return result