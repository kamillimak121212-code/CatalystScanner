from datetime import date

from app.history.importer.history_importer import (
    HistoryImporter
)


def main():

    importer = HistoryImporter()

    importer.import_history(

        from_date=date(2025, 6, 1),

        to_date=date(2025, 6, 30)

    )


if __name__ == "__main__":

    main()