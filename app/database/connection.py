from app.config.settings import settings

import psycopg


def get_connection():

    return psycopg.connect(

        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        dbname=settings.POSTGRES_DATABASE,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD

    )


def test_connection():

    print("Connecting to PostgreSQL...")

    try:

        conn = get_connection()

        with conn.cursor() as cur:

            cur.execute("""
                SELECT
                    current_database(),
                    current_schema(),
                    current_user,
                    version();
            """)

            print(cur.fetchone())

            cur.execute("""
                SELECT table_schema, table_name
                FROM information_schema.tables
                WHERE table_name = 'sec_filings';
            """)

            print(cur.fetchall())

        conn.close()

    except Exception as e:

        print(e)