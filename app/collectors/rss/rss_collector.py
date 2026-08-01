from email.utils import parsedate_to_datetime
import re

import feedparser

from app.models.news import News

from app.models.evidence import (
    Evidence,
    EvidenceSource
)


class RSSCollector:

    def collect(self, company):

        rss_url = (
            f"https://feeds.finance.yahoo.com/rss/2.0/headline?"
            f"s={company.ticker}&region=US&lang=en-US"
        )

        feed = feedparser.parse(rss_url)

        evidences = []

        seen_titles = set()

        for entry in feed.entries:

            title = entry.get(
                "title",
                ""
            ).strip()

            if not title:
                continue

            normalized_title = self._normalize_title(
                title
            )

            if normalized_title in seen_titles:
                continue

            seen_titles.add(
                normalized_title
            )

            published_at = parsedate_to_datetime(
                entry.published
            ).date()

            news = News(

                title=title,

                summary=entry.get(
                    "summary",
                    ""
                ),

                url=entry.link,

                source=(
                    f"Yahoo Finance: "
                    f"{company.ticker} News"
                ),

                published_at=published_at

            )

            evidence = Evidence(

                company=company,

                source=EvidenceSource.RSS,

                category="NEWS",

                title=news.title,

                description=news.summary,

                relevance=0,

                importance=None,

                url=news.url,

                published_at=news.published_at

            )

            evidences.append(
                evidence
            )

        return evidences

    def _normalize_title(
        self,
        title
    ):

        title = title.lower()

        title = re.sub(
            r"[^a-z0-9 ]",
            " ",
            title
        )

        title = " ".join(
            title.split()
        )

        return title