import requests

from app.models.evidence import (
    Evidence,
    EvidenceSource
)


class FredCollector:

    BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

    def __init__(self, api_key):

        self.api_key = api_key

    def collect(self, series_id):

        response = requests.get(

            self.BASE_URL,

            params={

                "series_id": series_id,
                "api_key": self.api_key,
                "file_type": "json",
                "sort_order": "desc",
                "limit": 1

            }

        )

        response.raise_for_status()

        data = response.json()

        observations = data.get(
            "observations",
            []
        )

        if not observations:
            return None

        observation = observations[-1]

        evidence = Evidence(

            company=None,

            source=EvidenceSource.MACRO,

            category="MACRO",

            title=series_id,

            description=(
                f"{series_id}: "
                f"{observation['value']}"
            ),

            relevance=100,

            importance=None,

            url="https://fred.stlouisfed.org/",

            published_at=observation["date"]

        )

        evidence.value = observation["value"]
        evidence.series = series_id

        return evidence