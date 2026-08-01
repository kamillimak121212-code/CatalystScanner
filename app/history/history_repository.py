from app.database.connection import get_connection

from app.history.history_event import HistoryEvent
from app.history.history_reaction import HistoryReaction


class HistoryRepository:

    def add(self, history):

        conn = get_connection()
        cursor = conn.cursor()

        reaction = history.reaction

        cursor.execute(
            """
            INSERT INTO history_events
            (
                ticker,
                event_type,
                event_date,
                sentiment,
                importance,
                confidence,
                relevance_score,
                main_company,
                products,
                related_companies,
                catalyst_score,
                decision_score,
                decision,
                matches,
                return_1d,
                return_3d,
                return_5d,
                return_10d,
                return_30d
            )
            VALUES
            (
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s
            )
            """,
            (
                history.company.ticker,
                history.event_type,
                history.date.date(),
                history.sentiment,
                history.importance,
                history.confidence,
                history.relevance_score,
                history.main_company,
                ",".join(history.products),
                ",".join(history.related_companies),
                history.catalyst_score,
                history.decision_score,
                history.decision,
                ",".join(history.matches),

                reaction.change_1d if reaction else None,
                reaction.change_3d if reaction else None,
                reaction.change_5d if reaction else None,
                reaction.change_10d if reaction else None,
                reaction.change_30d if reaction else None,
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    def find_similar(
        self,
        current
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                event_type,
                importance,
                confidence,
                relevance_score,
                main_company,
                products,
                related_companies,
                catalyst_score,
                decision,
                matches,
                return_1d,
                return_3d,
                return_5d,
                return_10d,
                return_30d
            FROM history_events
            """
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        similar = []

        for row in rows:

            history = HistoryEvent()

            history.event_type = row[0]
            history.importance = row[1]
            history.confidence = row[2]
            history.relevance_score = row[3]
            history.main_company = row[4]
            history.products = row[5].split(",") if row[5] else []
            history.related_companies = row[6].split(",") if row[6] else []
            history.catalyst_score = row[7]
            history.decision = row[8]
            history.matches = row[9].split(",") if row[9] else []

            reaction = HistoryReaction()

            reaction.change_1d = row[10]
            reaction.change_3d = row[11]
            reaction.change_5d = row[12]
            reaction.change_10d = row[13]
            reaction.change_30d = row[14]

            history.reaction = reaction

            similarity = current.compare(history)

            history.similarity = similarity.score
            history.match_level = similarity.level
            history.similarity_reasons = similarity.reasons

            # Tymczasowo dodajemy wszystkie rekordy,
            # żeby sprawdzić wyniki compare()
            similar.append(history)

        similar.sort(
            key=lambda x: x.similarity,
            reverse=True
        )

        return similar[:30]