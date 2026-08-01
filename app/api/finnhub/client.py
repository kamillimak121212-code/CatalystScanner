import requests

from app.config.settings import settings


class FinnhubClient:

    BASE_URL = "https://finnhub.io/api/v1"

    def __init__(self):

        self.api_key = settings.FINNHUB_API_KEY

    def get_company_news(
        self,
        ticker,
        from_date,
        to_date
    ):

        url = (
            f"{self.BASE_URL}/company-news"
        )

        params = {

            "symbol": ticker,
            "from": from_date,
            "to": to_date,
            "token": self.api_key

        }

        response = requests.get(
            url,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()