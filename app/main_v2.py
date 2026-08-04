from app.database.connection import test_connection

test_connection()

from app.database.connection import test_connection
from app.database.schema import create_tables
from app.database.company_repository import (
    get_all_companies
)

from app.history.price_history_importer import (
    PriceHistoryImporter
)
from app.history.history_resolver import (
    HistoryResolver
)

from app.services.market_import_service import (
    MarketImportService
)

from app.services.scanner_service import (
    ScannerService
)


def main():

    print("=" * 80)
    print("CATALYST SCANNER")
    print("=" * 80)

    # --------------------------------------------------
    # Database
    # --------------------------------------------------

    test_connection()
    create_tables()

    # --------------------------------------------------
    # Companies
    # --------------------------------------------------

    importer = MarketImportService()
    importer.import_defaults()

    # --------------------------------------------------
    # Price history
    # --------------------------------------------------

    price_importer = PriceHistoryImporter()

    for company in get_all_companies():

        print(f"Updating prices: {company.ticker}")

        price_importer.import_history(
            company.ticker
        )

    # --------------------------------------------------
    # Scan news
    # --------------------------------------------------

    print()
    print("=" * 80)
    print("SCANNING NEWS")
    print("=" * 80)

    scanner = ScannerService()
    scanner.run()

    # --------------------------------------------------
    # Resolve historical reactions
    # --------------------------------------------------

    print()
    print("=" * 80)
    print("UPDATING HISTORY")
    print("=" * 80)

    resolver = HistoryResolver()
    resolver.resolve()

    print()
    print("=" * 80)
    print("DONE")
    print("=" * 80)


if __name__ == "__main__":

    main()