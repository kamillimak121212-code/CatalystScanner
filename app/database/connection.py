import psycopg


def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="catalyst_scanner",
        user="postgres",
        password="kamil221"
    )


def test_connection():
    print("Connecting to PostgreSQL...")

    try:
        conn = get_connection()

        print("✅ Connected successfully!")

        conn.close()

    except Exception as e:
        print(f"❌ Connection failed: {e}")