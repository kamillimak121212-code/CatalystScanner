from app.models.evidence import (
    Evidence,
    EvidenceSource,
    EvidenceImportance
)


def build(company, filing):

    if filing.item == "Item 2.02":
        category = "EARNINGS"
    else:
        category = "SEC"

    return Evidence(
        company=company,
        source=EvidenceSource.SEC,
        category=category,
        title=filing.title,
        description=filing.description,
        relevance=0,
        importance=EvidenceImportance.LOW,
        url=filing.url,
        published_at=filing.published_at
    )