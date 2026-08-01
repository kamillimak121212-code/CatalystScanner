from app.collectors.rss.rss_collector import (
    collect as collect_rss
)

from app.collectors.insider.insider_collector import (
    collect as collect_insider
)

from app.collectors.sec8k.sec8k_collector import (
    collect as collect_sec
)


def collect_all(company):

    evidence = []

    evidence.extend(
        collect_rss(company)
    )

    evidence.extend(
        collect_insider(company)
    )

    evidence.extend(
        collect_sec(company)
    )

    return evidence