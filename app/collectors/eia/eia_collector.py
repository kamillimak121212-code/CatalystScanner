from datetime import datetime

from app.collectors.base.base_collector import (
    BaseCollector
)

from app.collectors.eia.eia_client import (
    EIAClient
)

from app.models.evidence import (
    Evidence,
    EvidenceSource
)


class EIACollector(BaseCollector):

    name = "EIA"

    priority = 90

    interval_minutes = 60

    asset_types = [
        "COMMODITY"
    ]

    def __init__(self):

        self.client = EIAClient()

    def collect(self):

        evidences = []

        try:

            data = self.client.get(
                "petroleum/stoc/wstk/data",
                {
                    "frequency": "weekly",
                    "sort[0][column]": "period",
                    "sort[0][direction]": "desc",
                    "length": 1
                }
            )

            records = (
                data.get("response", {})
                .get("data", [])
            )

            if not records:
                return evidences

            record = records[0]

            evidence = Evidence(

                company=None,

                source=EvidenceSource.MACRO,

                category="CRUDE_OIL_INVENTORY",

                title="US Crude Oil Inventories",

                description=str(record),

                relevance=100,

                importance=None,

                url="https://www.eia.gov/",

                published_at=datetime.now()

            )

            evidence.data = record

            evidences.append(
                evidence
            )

        except Exception as e:

            print(
                f"EIA Collector error: {e}"
            )

        return evidences