from app.database.company_repository import (
    add_company
)


class MarketImportService:

    def import_defaults(self):

        companies = [

            (
                "NVDA",
                "NVIDIA",
                "NASDAQ",
                "1045810"
            ),

            (
                "MSFT",
                "Microsoft",
                "NASDAQ",
                "789019"
            ),

            (
                "AAPL",
                "Apple",
                "NASDAQ",
                "320193"
            ),

            (
                "AMZN",
                "Amazon",
                "NASDAQ",
                "1018724"
            ),

            (
                "META",
                "Meta Platforms",
                "NASDAQ",
                "1326801"
            ),

            (
                "GOOGL",
                "Alphabet",
                "NASDAQ",
                "1652044"
            ),

            (
                "TSLA",
                "Tesla",
                "NASDAQ",
                "1318605"
            ),

            (
                "AMD",
                "Advanced Micro Devices",
                "NASDAQ",
                "2488"
            ),

            (
                "AVGO",
                "Broadcom",
                "NASDAQ",
                "1730168"
            ),

            (
                "TSM",
                "Taiwan Semiconductor",
                "NYSE",
                "1046179"
            ),

        ]

        for (
            ticker,
            name,
            exchange,
            cik
        ) in companies:

            add_company(
                ticker=ticker,
                name=name,
                exchange=exchange,
                cik=cik
            )