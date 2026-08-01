from datetime import date

from app.api.finnhub.client import FinnhubClient

from app.models.evidence import (
    Evidence,
    EvidenceSource
)


class HistoricalNewsCollector:

    def __init__(self):

        self.client = FinnhubClient()

    def collect(
        self,
        company,
        from_date,
        to_date
    ):

        articles = self.client.get_company_news(
            ticker=company.ticker,
            from_date=from_date.isoformat(),
            to_date=to_date.isoformat()
        )

        evidences = []

        for article in articles:

            evidence = Evidence(

                company=company,

                source=EvidenceSource.RSS,

                category="NEWS",

                title=article.get(
                    "headline",
                    ""
                ),

                description=article.get(
                    "summary",
                    ""
                ),

                relevance=0,

                importance=None,

                url=article.get(
                    "url",
                    ""
                ),

                published_at=date.fromtimestamp(
                    article["datetime"]
                )

            )

            evidences.append(
                evidence
            )

        return evidences