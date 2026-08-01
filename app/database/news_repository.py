from app.database.connection import get_connection


def save_news(news):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO news (
            title,
            summary,
            url,
            source,
            published_at
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (url) DO NOTHING;
        """,
        (
            news.title,
            news.summary,
            news.url,
            news.source,
            news.published_at
        )
    )

    conn.commit()

    saved = cursor.rowcount > 0

    cursor.close()
    conn.close()

    return saved