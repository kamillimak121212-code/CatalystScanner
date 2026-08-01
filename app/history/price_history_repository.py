from app.database.connection import get_connection


class PriceHistoryRepository:

    def get_price(
        self,
        ticker,
        trading_day
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT close
            FROM price_history
            WHERE ticker = %s
            AND trading_day = %s
            """,
            (
                ticker,
                trading_day
            )
        )

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row is None:
            return None

        return float(row[0])

    def get_next_prices(
        self,
        ticker,
        trading_day,
        limit=31
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                trading_day,
                close,
                volume
            FROM price_history
            WHERE ticker = %s
            AND trading_day >= %s
            ORDER BY trading_day
            LIMIT %s
            """,
            (
                ticker,
                trading_day,
                limit
            )
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows

    def get_history(
        self,
        ticker,
        days=30
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                trading_day,
                open,
                high,
                low,
                close,
                volume
            FROM price_history
            WHERE ticker = %s
            ORDER BY trading_day DESC
            LIMIT %s
            """,
            (
                ticker,
                days
            )
        )

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return list(reversed(rows))