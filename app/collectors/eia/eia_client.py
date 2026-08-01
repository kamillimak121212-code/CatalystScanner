from app.api.api_client import ApiClient
from app.config.settings import settings


class EIAClient(ApiClient):

    def __init__(self):

        super().__init__(
            base_url="https://api.eia.gov/v2"
        )

        self.api_key = settings.EIA_API_KEY

    def get(
        self,
        endpoint,
        params=None
    ):

        if params is None:
            params = {}

        params["api_key"] = self.api_key

        return super().get(
            endpoint,
            params=params
        )