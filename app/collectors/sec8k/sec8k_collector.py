from app.collectors.sec.sec_client import (
    get_json,
    get_content
)

from app.collectors.sec.cik_mapper import (
    get_cik
)

from app.collectors.sec8k.sec8k_parser import (
    parse_8k
)

from app.collectors.sec8k.sec8k_evidence import (
    build
)


BASE_URL = "https://data.sec.gov/submissions/"
ARCHIVE_URL = "https://www.sec.gov/Archives/edgar/data/"


def collect(company):

    print(f"Collecting 8-K filings for {company.ticker}...")

    cik = get_cik(company.ticker)

    if cik is None:
        print("CIK not found.")
        return []

    cik = cik.zfill(10)

    data = get_json(
        f"{BASE_URL}CIK{cik}.json"
    )

    recent = data["filings"]["recent"]

    evidence_list = []

    checked = 0

    for form, filing_date, accession, primary_document in zip(
        recent["form"],
        recent["filingDate"],
        recent["accessionNumber"],
        recent["primaryDocument"]
    ):

        if form != "8-K":
            continue

        checked += 1

        accession_clean = accession.replace("-", "")

        url = (
            f"{ARCHIVE_URL}"
            f"{int(cik)}/"
            f"{accession_clean}/"
            f"{primary_document}"
        )

        print(f"\n8-K #{checked}")
        print(url)

        try:

            html = get_content(url)

            if isinstance(html, bytes):
                html = html.decode(
                    "utf-8",
                    errors="ignore"
                )

        except Exception as e:

            print(e)
            continue

        filing = parse_8k(
            company,
            html,
            filing_date,
            accession,
            primary_document
        )

        filing.url = url

        evidence = build(
            company,
            filing
        )

        evidence_list.append(evidence)

        print(evidence)

    return evidence_list