import re

from app.collectors.sec.sec_client import (
    get_json,
    get_content
)

from app.collectors.sec.cik_mapper import (
    get_cik
)

from app.collectors.insider.insider_parser import (
    parse_form4
)

from app.collectors.insider.evidence_builder import (
    build
)


BASE_URL = "https://data.sec.gov/submissions/"
ARCHIVE_URL = "https://www.sec.gov/Archives/edgar/data/"


def collect(company):

    print(f"Collecting insider filings for {company.ticker}...")

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

    for form, filing_date, accession in zip(
        recent["form"],
        recent["filingDate"],
        recent["accessionNumber"]
    ):

        if form != "4":
            continue

        checked += 1

        if checked > 3:
            break

        accession_clean = accession.replace("-", "")

        filing_url = (
            f"{ARCHIVE_URL}"
            f"{int(cik)}/"
            f"{accession_clean}/"
            f"{accession}.txt"
        )

        try:

            filing = get_content(filing_url)

            if isinstance(filing, bytes):
                filing = filing.decode("utf-8", errors="ignore")

        except Exception as e:

            print(e)
            continue

        match = re.search(
            r"<XML>(.*?)</XML>",
            filing,
            re.DOTALL | re.IGNORECASE
        )

        if match is None:
            continue

        try:

            transaction = parse_form4(
                company,
                match.group(1).strip()
            )

        except Exception as e:

            print(e)
            continue

        if transaction is None:
            continue

        transaction.filing_url = filing_url
        transaction.filing_date = filing_date

        evidence = build(
            company,
            transaction
        )

        evidence_list.append(evidence)

    return evidence_list