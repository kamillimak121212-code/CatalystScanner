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

        print("✅ Connected successfully!")

        conn.close()

    except Exception as e:

        print(f"❌ Connection failed: {e}")