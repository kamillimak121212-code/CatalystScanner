from app.collectors.sec8k.sec8k_collector import (
    collect
)

from app.database.company_repository import (
    get_all_companies
)


companies = get_all_companies()

for company in companies:
    collect(company)

from app.collectors.insider.insider_collector import (
    collect as collect_insiders
)

from app.services.narrative_updater import (
    update_narrative
)
from app.services.narrative_engine import build_narrative
from app.services.narrative_matcher import (
    find_matching_narrative
)
from app.services.narrative_repository import (
    get_narratives,
    add_narrative
)

from app.services.report_builder import build_report
from app.services.event_analyzer import analyze_event
from app.services.event_builder import build_event
from app.services.event_ranking import rank_events
from app.services.event_repository import get_events

from app.database.connection import test_connection
from app.database.schema import create_tables
from app.database.company_repository import (
    add_company,
    get_all_companies
)

from app.services.scanner_service import ScannerService

from app.collectors.sec.sec_collector import collect
from app.collectors.rss.rss_collector import get_latest_news
from app.collectors.rss.rss_evidence import build_evidence

from app.logger.logger import logger


def main():

    print("===================================")
    print("      CATALYST SCANNER")
    print("===================================\n")

    logger.info("Catalyst Scanner started")

    test_connection()
    create_tables()

    add_company("NVDA", "NVIDIA", "NASDAQ")

    companies = get_all_companies()

    company = companies[0]

    collect(company)

    scanner = ScannerService()
    scanner.run()

    # ---------- Insider Collector ----------
    collect_insiders(company)

    # ---------- RSS ----------
    news = get_latest_news(company.ticker)

    if news:

        for article in news[:5]:

            print("\n-----------------------------")
            print("ARTICLE")
            print(article.title)

            evidence = build_evidence(article, company)

            print("Evidence:", evidence)

            if evidence is None:
                print("AI rejected article.")
                continue

            print("\nAI UNDERSTANDING")
            print("--------------------------")
            print("Summary:", evidence.understanding.summary)
            print("Main Company:", evidence.understanding.main_company)
            print("Event:", evidence.understanding.event)
            print("Reason:", evidence.understanding.reason)
            print("Relevant:", evidence.understanding.is_relevant)
            print("Relevance Score:", evidence.understanding.relevance_score)
            print("Confidence:", evidence.understanding.confidence)
            print("Evidence Importance:", evidence.importance.name)

            event = build_event(evidence)

            print("Event:", event)

            analysis = analyze_event(event)
            event.analysis = analysis

            narrative = find_matching_narrative(
                evidence.understanding,
                get_narratives()
            )

            if narrative is None:

                narrative = build_narrative(event)

                update_narrative(
                    narrative,
                    evidence
                )

                add_narrative(narrative)

                print("Created Narrative:", narrative.title)

            else:

                update_narrative(
                    narrative,
                    evidence
                )

                print("Updated Narrative:", narrative.title)

    print("\nEvents in repository:", len(get_events()))
    print("Narratives:", len(get_narratives()))

    ranked_events = rank_events(get_events())

    print("Ranked events:", len(ranked_events))

    print()
    print("=" * 60)
    print("CATALYST REPORTS")
    print("=" * 60)

    for event in ranked_events:

        narrative = build_narrative(event)

        report = build_report(
            event,
            narrative
        )

        print()
        print(report)
        print()

    logger.info("Scan finished successfully")

    print("=" * 60)
    print("Scan finished successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()

    from app.telegram.telegram_sender import (
    send
)

send("🚀 Catalyst Scanner działa!")