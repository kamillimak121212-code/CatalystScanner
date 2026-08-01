from app.database.connection import get_connection
from app.models.company import Company


def add_company(ticker, name, exchange):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO companies (ticker, name, exchange)
        VALUES (%s, %s, %s)
        ON CONFLICT (ticker) DO NOTHING;
        """,
        (ticker, name, exchange)
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_all_companies():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, ticker, name, exchange
        FROM companies
        ORDER BY ticker;
    """)

    rows = cursor.fetchall()

    companies = []

    for row in rows:

        company = Company(
            company_id=row[0],
            ticker=row[1],
            name=row[2],
            exchange=row[3]
        )

        companies.append(company)

    cursor.close()
    conn.close()

    return companies

def get_company_by_ticker(ticker):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, ticker, name, exchange
        FROM companies
        WHERE ticker = %s;
        """,
        (ticker,)
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return None

    return Company(
        company_id=row[0],
        ticker=row[1],
        name=row[2],
        exchange=row[3]
    )