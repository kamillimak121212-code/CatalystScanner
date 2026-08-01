from datetime import datetime

from app.history.history_event import HistoryEvent
from app.history.history_reaction_builder import (
    HistoryReactionBuilder
)


class HistoryBuilder:

    def __init__(self):

        self.reaction_builder = HistoryReactionBuilder()

    def build(self, result):

        history = HistoryEvent()

        # --------------------------------------------------
        # Basic
        # --------------------------------------------------

        history.company = result.evidence.company
        history.evidence = result.evidence
        history.date = datetime.now()

        history.title = result.evidence.title
        history.url = result.evidence.url

        # --------------------------------------------------
        # Event
        # --------------------------------------------------

        if result.event:

            event_type = result.event.get(
                "event_type"
            )

            if event_type:

                history.event_type = event_type.value

            history.category = result.event.get(
                "category",
                ""
            )

        # --------------------------------------------------
        # AI Understanding
        # --------------------------------------------------

        if result.understanding:

            history.sentiment = (
                result.understanding.sentiment
            )

            history.main_company = (
                result.understanding.main_company
            )

            history.products = (
                result.understanding.products
            )

            history.related_companies = (
                result.understanding.related_companies
            )

            history.relevance_score = (
                result.understanding.relevance_score
            )

            history.confidence = (
                result.understanding.confidence
            )

            history.summary = (
                result.understanding.summary
            )

        # --------------------------------------------------
        # Importance
        # --------------------------------------------------

        if result.importance:

            history.importance = (
                result.importance.name
            )

        # --------------------------------------------------
        # Decision
        # --------------------------------------------------

        if result.decision:

            history.decision = (
                result.decision.recommendation
            )

            history.decision_score = (
                result.decision.score
            )

        # --------------------------------------------------
        # Company Intelligence
        # --------------------------------------------------

        if result.evaluation:

            history.matches = [

                match["name"]

                for match in result.evaluation.matches

            ]

            history.intelligence_score = (
                result.evaluation.score
            )

        # --------------------------------------------------
        # Catalyst
        # --------------------------------------------------

        history.catalyst_score = (
            result.catalyst_score
        )

        # --------------------------------------------------
        # Market Reaction
        # --------------------------------------------------

        history.reaction = self.reaction_builder.build(
            result.evidence.company.ticker,
            result.evidence.published_at
        )

        return history