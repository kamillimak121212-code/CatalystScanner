import requests

from app.models.evidence import (
    Evidence,
    EvidenceSource
)

from app.logger.logger import logger


IMPORTANT_FORMS = {
    "8-K",
    "10-Q",
    "10-K",
    "13D",
    "SC TO",
    "S-1"
}


class SECCollector:

    def collect(
        self,
        company
    ):

        logger.info(
            f"SEC -> {company.ticker}"
        )

        if not company.cik:

            logger.warning(
                f"{company.ticker} has no CIK"
            )

            return []

        cik = str(
            company.cik
        ).zfill(10)

        submissions_url = (
            f"https://data.sec.gov/submissions/"
            f"CIK{cik}.json"
        )

        headers = {

            "User-Agent": (
                "CatalystScanner "
                "(development)"
            )

        }

        try:

            response = requests.get(
                submissions_url,
                headers=headers,
                timeout=20
            )

            logger.info(
                f"{company.ticker} -> {response.status_code}"
            )

            if response.status_code != 200:
                return []

            data = response.json()

        except Exception as e:

            logger.error(
                f"SEC request failed: {e}"
            )

            return []

        recent = (
            data
            .get("filings", {})
            .get("recent", {})
        )

        forms = recent.get(
            "form",
            []
        )

        dates = recent.get(
            "filingDate",
            []
        )

        accession_numbers = recent.get(
            "accessionNumber",
            []
        )

        primary_documents = recent.get(
            "primaryDocument",
            []
        )

        evidences = []

        for (
            form,
            date,
            accession,
            document
        ) in zip(

            forms,
            dates,
            accession_numbers,
            primary_documents

        ):

            if form not in IMPORTANT_FORMS:
                continue

            accession_no_dash = (
                accession.replace(
                    "-",
                    ""
                )
            )

            filing_url = (
                "https://www.sec.gov/Archives/edgar/data/"
                f"{int(company.cik)}/"
                f"{accession_no_dash}/"
                f"{document}"
            )

            evidence = Evidence(

                company=company,

                source=EvidenceSource.SEC,

                category="SEC",

                title=f"{form} filing",

                description=(
                    f"{company.ticker} "
                    f"filed {form}"
                ),

                relevance=100,

                importance=None,

                url=filing_url,

                published_at=date

            )

            evidences.append(
                evidence
            )

        logger.info(
            f"{company.ticker} SEC evidence: {len(evidences)}"
        )

        return evidences