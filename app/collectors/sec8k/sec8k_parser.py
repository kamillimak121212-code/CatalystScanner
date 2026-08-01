import re

from bs4 import BeautifulSoup

from app.models.sec_filing import (
    SecFiling
)


def parse_8k(company, html, filing_date, accession, document):

    soup = BeautifulSoup(html, "html.parser")

    title = ""

    if soup.title:
        title = soup.title.get_text(" ", strip=True)

    text = soup.get_text(
        "\n",
        strip=True
    )

    start = text.find("Item ")

    if start != -1:
        description = text[start:start + 5000]
    else:
        description = text[:5000]

    item = ""

    match = re.search(
        r"Item\s+\d+\.\d+",
        description
    )

    if match:
        item = match.group(0)

    filing = SecFiling()

    filing.filing_type = "8-K"
    filing.item = item
    filing.title = title
    filing.description = description
    filing.accession = accession
    filing.document = document
    filing.published_at = filing_date

    return filing