from app.database.connection import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # --------------------------------------------------
    # Companies
    # --------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS companies (

            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

            ticker VARCHAR(10) UNIQUE NOT NULL,

            name VARCHAR(200) NOT NULL,

            exchange VARCHAR(50),

            is_active BOOLEAN DEFAULT TRUE,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        );
    """)

    # --------------------------------------------------
    # News
    # --------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (

            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

            title VARCHAR(500) NOT NULL,

            summary TEXT,

            url VARCHAR(1000) UNIQUE NOT NULL,

            source VARCHAR(100),

            published_at TIMESTAMP,

            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        );
    """)

    # --------------------------------------------------
    # Price History
    # --------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (

            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

            ticker VARCHAR(10) NOT NULL,

            trading_day DATE NOT NULL,

            open NUMERIC(12,4),

            high NUMERIC(12,4),

            low NUMERIC(12,4),

            close NUMERIC(12,4),

            volume BIGINT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(ticker, trading_day)

        );
    """)

    # --------------------------------------------------
    # History Events
    # --------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history_events (

            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

            ticker VARCHAR(10) NOT NULL,

            news_id INTEGER,

            event_type VARCHAR(100),

            event_date DATE NOT NULL,

            sentiment VARCHAR(20),

            importance VARCHAR(20),

            confidence INTEGER,

            relevance_score INTEGER,

            main_company VARCHAR(200),

            products TEXT,

            related_companies TEXT,

            catalyst_score INTEGER,

            decision_score INTEGER,

            decision VARCHAR(20),

            price_at_event NUMERIC(12,4),

            matches TEXT,

            return_1d NUMERIC(8,2),

            return_3d NUMERIC(8,2),

            return_5d NUMERIC(8,2),

            return_10d NUMERIC(8,2),

            return_30d NUMERIC(8,2),

            resolved BOOLEAN DEFAULT FALSE,

            resolved_at TIMESTAMP,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        );
    """)

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Database schema is ready!")