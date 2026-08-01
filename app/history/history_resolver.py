from datetime import date, timedelta

from app.database.connection import get_connection

from app.history.history_reaction_builder import (
    HistoryReactionBuilder
)


class HistoryResolver:

    def __init__(self):

        self.builder = HistoryReactionBuilder()

    def resolve(self):

        conn = get_connection()
        cursor = conn.cursor()

        # Liczymy tylko wydarzenia,
        # które mają już minimum 30 dni historii.

        cutoff = date.today() - timedelta(days=30)

        cursor.execute(
            """
            SELECT
                id,
                ticker,
                event_date
            FROM history_events
            WHERE
                resolved = FALSE
                AND event_date <= %s
            """,
            (cutoff,)
        )

        rows = cursor.fetchall()

        updated = 0

        for history_id, ticker, event_date in rows:

            reaction = self.builder.build(
                ticker,
                event_date
            )

            if reaction is None:
                continue

            cursor.execute(
                """
                UPDATE history_events
                SET
                    return_1d=%s,
                    return_3d=%s,
                    return_5d=%s,
                    return_10d=%s,
                    return_30d=%s,
                    resolved=TRUE,
                    resolved_at=NOW()
                WHERE id=%s
                """,
                (
                    reaction.change_1d,
                    reaction.change_3d,
                    reaction.change_5d,
                    reaction.change_10d,
                    reaction.change_30d,
                    history_id
                )
            )

            updated += 1

        conn.commit()

        cursor.close()
        conn.close()

        print(
            f"History Resolver updated {updated} events."
        )