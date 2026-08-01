from app.decision.decision import Decision
from app.decision.decision_rules import (
    EVENT_SCORES,
    IMPORTANCE_SCORES
)


class DecisionEngine:

    def decide(self, result):

        decision = Decision()

        # --------------------------------------------------
        # Ignore non-relevant news
        # --------------------------------------------------

        if (
            result.understanding
            and not result.understanding.is_relevant
        ):

            decision.score = 0
            decision.recommendation = "IGNORE"
            decision.reason = (
                "AI marked article as not relevant"
            )

            return decision

        score = 0
        reasons = []

        # --------------------------------------------------
        # AI Relevance
        # --------------------------------------------------

        if (
            result.understanding
            and result.understanding.is_relevant
        ):

            score += 10

            reasons.append("+10 Relevant")

        # --------------------------------------------------
        # AI Confidence
        # --------------------------------------------------

        if result.understanding:

            confidence = result.understanding.confidence

            if confidence <= 1:
                confidence *= 100

            ai_score = min(
                int(confidence / 20),
                5
            )

            score += ai_score

            reasons.append(
                f"+{ai_score} AI"
            )

        # --------------------------------------------------
        # Event Type
        # --------------------------------------------------

        if result.event:

            event_type = result.event.get(
                "event_type"
            )

            event_score = EVENT_SCORES.get(
                event_type,
                0
            )

            score += event_score

            reasons.append(
                f"{event_score:+} Event"
            )

        # --------------------------------------------------
        # Sentiment
        # --------------------------------------------------

        if result.understanding:

            sentiment = (
                result.understanding.sentiment
            )

            if sentiment == "POSITIVE":

                score += 10
                reasons.append("+10 Sentiment")

            elif sentiment == "NEGATIVE":

                score -= 20
                reasons.append("-20 Sentiment")

        # --------------------------------------------------
        # Importance
        # --------------------------------------------------

        if result.importance:

            importance_score = IMPORTANCE_SCORES.get(
                result.importance,
                0
            )

            score += importance_score

            reasons.append(
                f"+{importance_score} Importance"
            )

        # --------------------------------------------------
        # Company Intelligence
        # --------------------------------------------------

        if result.evaluation:

            evaluation_score = min(
                result.evaluation.score,
                100
            )

            evaluation_points = int(
                evaluation_score * 0.15
            )

            score += evaluation_points

            reasons.append(
                f"+{evaluation_points} Intelligence"
            )

        # --------------------------------------------------
        # Catalyst
        # --------------------------------------------------

        catalyst_points = int(
            result.catalyst_score * 0.20
        )

        score += catalyst_points

        reasons.append(
            f"+{catalyst_points} Catalyst"
        )

        # --------------------------------------------------
        # Prediction
        # --------------------------------------------------

        if result.prediction:

            prediction_points = int(
                result.prediction.confidence * 0.20
            )

            score += prediction_points

            reasons.append(
                f"+{prediction_points} Prediction"
            )

        # --------------------------------------------------
        # Risk
        # --------------------------------------------------

        if result.risk:

            score -= result.risk.score

            reasons.append(
                f"-{result.risk.score} Risk"
            )

        # --------------------------------------------------

        score = max(
            0,
            min(score, 100)
        )

        decision.score = score

        if score >= 85:

            decision.recommendation = (
                "STRONG BUY"
            )

        elif score >= 70:

            decision.recommendation = (
                "BUY"
            )

        elif score >= 50:

            decision.recommendation = (
                "WATCH"
            )

        else:

            decision.recommendation = (
                "IGNORE"
            )

        decision.reason = " | ".join(
            reasons
        )

        return decision