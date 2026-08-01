from app.database.company_repository import (
    add_company
)


class MarketImportService:

    def import_defaults(self):

        companies = [

            ("NVDA", "NVIDIA", "NASDAQ"),
            ("MSFT", "Microsoft", "NASDAQ"),
            ("AAPL", "Apple", "NASDAQ"),
            ("AMZN", "Amazon", "NASDAQ"),
            ("META", "Meta Platforms", "NASDAQ"),
            ("GOOGL", "Alphabet", "NASDAQ"),
            ("TSLA", "Tesla", "NASDAQ"),
            ("AMD", "Advanced Micro Devices", "NASDAQ"),
            ("AVGO", "Broadcom", "NASDAQ"),
            ("TSM", "Taiwan Semiconductor", "NYSE"),

        ]

        for ticker, name, exchange in companies:

            add_company(
                ticker,
                name,
                exchange
            )