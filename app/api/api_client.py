import time
import requests


class ApiClient:

    def __init__(
        self,
        base_url,
        timeout=30,
        retries=3
    ):

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = retries

    def get(
        self,
        endpoint,
        params=None,
        headers=None
    ):

        if params is None:
            params = {}

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        last_exception = None

        for attempt in range(self.retries):

            try:

                response = requests.get(
                    url,
                    params=params,
                    headers=headers,
                    timeout=self.timeout
                )

                response.raise_for_status()

                return response.json()

            except requests.RequestException as e:

                last_exception = e

                if attempt < self.retries - 1:

                    time.sleep(1)

        raise last_exception

    def post(
        self,
        endpoint,
        json=None,
        headers=None
    ):

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        last_exception = None

        for attempt in range(self.retries):

            try:

                response = requests.post(
                    url,
                    json=json,
                    headers=headers,
                    timeout=self.timeout
                )

                response.raise_for_status()

                return response.json()

            except requests.RequestException as e:

                last_exception = e

                if attempt < self.retries - 1:

                    time.sleep(1)

        raise last_exception