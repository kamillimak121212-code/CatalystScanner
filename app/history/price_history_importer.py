from app.database.connection import get_connection
from app.history.price_downloader import PriceDownloader


class PriceHistoryImporter:

    def __init__(self):

        self.downloader = PriceDownloader()

    def import_history(self, ticker):

        print(f"Downloading history for {ticker}...")

        history = self.downloader.download(ticker)

        print(f"Downloaded {len(history)} candles")

        conn = get_connection()
        cursor = conn.cursor()

        inserted = 0

        try:

            for date, row in history.iterrows():

                cursor.execute(
                    """
                    INSERT INTO price_history
                    (
                        ticker,
                        trading_day,
                        open,
                        high,
                        low,
                        close,
                        volume
                    )
                    VALUES
                    (
                        %s,%s,%s,%s,%s,%s,%s
                    )
                    ON CONFLICT (ticker, trading_day)
                    DO NOTHING
                    """,
                    (
                        ticker,
                        date.date(),
                        None if row["Open"] != row["Open"] else float(row["Open"]),
                        None if row["High"] != row["High"] else float(row["High"]),
                        None if row["Low"] != row["Low"] else float(row["Low"]),
                        None if row["Close"] != row["Close"] else float(row["Close"]),
                        None if row["Volume"] != row["Volume"] else int(row["Volume"]),
                    )
                )

                inserted += 1

            conn.commit()

            print(f"✅ Imported {inserted} candles for {ticker}")

        except Exception as e:

            conn.rollback()

            print("❌ Import failed")
            print(e)

            raise

        finally:

            cursor.close()
            conn.close()