import requests


HEADERS = {
    "User-Agent": "CatalystScanner/1.0 kamil@example.com",
    "Accept-Encoding": "gzip, deflate",
}


def get_json(url):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def get_content(url):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    return response.content