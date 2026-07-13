from database.connection import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            ticker VARCHAR(10) NOT NULL,
            name VARCHAR(200) NOT NULL,
            exchange VARCHAR(50) NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Table 'companies' created successfully!")