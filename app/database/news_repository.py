from app.database.connection import get_connection

from app.services.news_hash_service import (
    NewsHashService
)


hash_service = NewsHashService()


def save_news(news):

    news_hash = hash_service.create(
        news
    )

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO news (

            title,
            summary,
            url,
            source,
            published_at,
            news_hash

        )
        VALUES (%s, %s, %s, %s, %s, %s)

        ON CONFLICT (news_hash)
        DO NOTHING;
        """,
        (
            news.title,
            news.summary,
            news.url,
            news.source,
            news.published_at,
            news_hash
        )
    )

    conn.commit()

    saved = (
        cursor.rowcount > 0
    )

    if saved:

        print(
            f"NEW: {news.title}"
        )

    else:

        print(
            f"DUPLICATE: {news.title}"
        )

    cursor.close()
    conn.close()

    return saved