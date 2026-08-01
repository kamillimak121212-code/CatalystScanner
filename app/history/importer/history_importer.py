from app.collectors.newsapi.historical_news_collector import (
    HistoricalNewsCollector
)

from app.pipeline.evidence_pipeline import (
    EvidencePipeline
)

from app.services.watchlist_service import (
    WatchlistService
)


class HistoryImporter:

    def __init__(self):

        self.watchlist = WatchlistService()

        self.collector = HistoricalNewsCollector()

        self.pipeline = EvidencePipeline()

    def import_history(
        self,
        from_date,
        to_date
    ):

        companies = self.watchlist.get_companies()

        for company in companies:

            print()
            print("=" * 80)
            print(f"IMPORTING {company.ticker}")
            print("=" * 80)

            evidences = self.collector.collect(
                company,
                from_date,
                to_date
            )

            print(
                f"Downloaded {len(evidences)} news"
            )

            for evidence in evidences:

                print(
                    f"{evidence.published_at} | {evidence.title}"
                )

                self.pipeline.process(
                    evidence
                )