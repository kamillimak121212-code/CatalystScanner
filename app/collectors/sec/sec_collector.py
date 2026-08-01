import requests


def collect(company):

    cik = "0001045810"

    url = (
        f"https://data.sec.gov/submissions/CIK{cik}.json"
    )

    headers = {
    "User-Agent": "CatalystScanner (development)"
}

    response = requests.get(url, headers=headers)

    print(response.status_code)