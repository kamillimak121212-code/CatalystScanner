import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from app.collectors.rss.rss_collector import (
    RSSCollector
)

from app.pipeline.evidence_pipeline import (
    EvidencePipeline
)

from app.history.history_builder import (
    HistoryBuilder
)

from app.history.history_repository import (
    HistoryRepository
)

from app.services.watchlist_service import (
    WatchlistService
)

from app.logger.logger import logger


class ScannerService:

    def __init__(self):

        self.watchlist = WatchlistService()

        self.rss = RSSCollector()

        self.history_builder = HistoryBuilder()

        self.history_repository = HistoryRepository()

    def process_evidence(
        self,
        evidence
    ):

        start = time.perf_counter()

        pipeline = EvidencePipeline()

        result = pipeline.process(
            evidence
        )

        elapsed = (
            time.perf_counter() - start
        )

        return result, elapsed

    def run(self):

        companies = self.watchlist.get_companies()

        logger.info(
            f"Loaded {len(companies)} active companies"
        )

        for company in companies:

            print()
            print("=" * 100)
            print(
                f"SCANNING {company.ticker} - {company.name}"
            )
            print("=" * 100)

            evidences = self.rss.collect(
                company
            )

            print(
                f"Evidence found: {len(evidences)}"
            )

            futures = []

            with ThreadPoolExecutor(
                max_workers=5
            ) as executor:

                for evidence in evidences:

                    futures.append(

                        executor.submit(
                            self.process_evidence,
                            evidence
                        )

                    )

                for future in as_completed(
                    futures
                ):

                    try:

                        result, elapsed = (
                            future.result()
                        )

                        print(
                            f"\nPipeline time: {elapsed:.2f}s"
                        )

                        self.print_report(
                            result
                        )

                    except Exception as e:

                        print(
                            f"Pipeline error: {e}"
                        )

    def print_report(
        self,
        result
    ):

        print()
        print("=" * 100)
        print("FINAL ANALYSIS REPORT")
        print("=" * 100)

        print(
            f"Title: {result.evidence.title}"
        )
        print()

        print("AI UNDERSTANDING")
        print("-" * 100)
        print(result.understanding)
        print()

        print("EVENT")
        print("-" * 100)
        print(result.event)
        print()

        print("COMPANY INTELLIGENCE")
        print("-" * 100)
        print(result.evaluation)
        print()

        print("IMPORTANCE")
        print("-" * 100)
        print(result.importance)
        print()

        print("CATALYST SCORE")
        print("-" * 100)
        print(result.catalyst_score)
        print()

        print("PREDICTION")
        print("-" * 100)
        print(result.prediction)
        print()

        print("RISK")
        print("-" * 100)
        print(result.risk)
        print()

        print("DECISION")
        print("-" * 100)
        print(result.decision)
        print()

        print("NOTIFICATION")
        print("-" * 100)
        print(result.should_notify)

        print("=" * 100)
        print()