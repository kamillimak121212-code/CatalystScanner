import requests

from app.models.evidence import (
    Evidence,
    EvidenceSource
)


class SECCollector:

    def collect(
        self,
        company
    ):

        if not company.cik:
            return []

        cik = str(
            company.cik
        ).zfill(10)

        url = (
            f"https://data.sec.gov/submissions/"
            f"CIK{cik}.json"
        )

        headers = {

            "User-Agent": (
                "CatalystScanner (development)"
            )

        }

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=20
            )

            if response.status_code != 200:

                print(
                    f"SEC error "
                    f"{company.ticker}: "
                    f"{response.status_code}"
                )

                return []

            data = response.json()

        except Exception as e:

            print(
                f"SEC request failed: {e}"
            )

            return []

        filings = (
            data
            .get("filings", {})
            .get("recent", {})
        )

        forms = filings.get(
            "form",
            []
        )

        dates = filings.get(
            "filingDate",
            []
        )

        evidences = []

        for form, date in zip(
            forms,
            dates
        ):

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

                url=url,

                published_at=date

            )

            evidences.append(
                evidence
            )

        return evidences