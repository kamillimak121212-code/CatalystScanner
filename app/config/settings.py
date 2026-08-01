import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    # --------------------------------------------------
    # OpenAI
    # --------------------------------------------------

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

    # --------------------------------------------------
    # Finnhub
    # --------------------------------------------------

    FINNHUB_API_KEY = os.getenv(
        "FINNHUB_API_KEY"
    )

    # --------------------------------------------------
    # PostgreSQL
    # --------------------------------------------------

    POSTGRES_HOST = os.getenv(
        "POSTGRES_HOST"
    )

    POSTGRES_PORT = int(
        os.getenv(
            "POSTGRES_PORT",
            5432
        )
    )

    POSTGRES_DATABASE = os.getenv(
        "POSTGRES_DATABASE"
    )

    POSTGRES_USER = os.getenv(
        "POSTGRES_USER"
    )

    POSTGRES_PASSWORD = os.getenv(
        "POSTGRES_PASSWORD"
    )

    # --------------------------------------------------
    # Telegram
    # --------------------------------------------------

    TELEGRAM_BOT_TOKEN = os.getenv(
        "TELEGRAM_BOT_TOKEN"
    )

    TELEGRAM_CHAT_ID = os.getenv(
        "TELEGRAM_CHAT_ID"
    )

    # --------------------------------------------------
    # External APIs
    # --------------------------------------------------

    FRED_API_KEY = os.getenv(
        "FRED_API_KEY"
    )

    EIA_API_KEY = os.getenv(
        "EIA_API_KEY"
    )

    FDA_API_KEY = os.getenv(
        "FDA_API_KEY"
    )


settings = Settings()