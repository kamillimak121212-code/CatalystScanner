from app.database.connection import get_connection


class SECFilingRepository:

    def exists(
        self,
        accession_number
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM sec_filings
            WHERE accession_number = %s
            """,
            (
                accession_number,
            )
        )

        exists = (
            cursor.fetchone() is not None
        )

        cursor.close()
        conn.close()

        return exists

    def save(

        self,

        company,

        accession_number,

        form,

        filing_date

    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO sec_filings (

                company_id,

                accession_number,

                form,

                filing_date

            )
            VALUES (%s, %s, %s, %s)

            ON CONFLICT (
                accession_number
            )
            DO NOTHING
            """,
            (
                company.id,
                accession_number,
                form,
                filing_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()