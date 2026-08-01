from app.models.evidence import (
    Evidence,
    EvidenceSource,
    EvidenceImportance
)


def build(company, transaction):

    return Evidence(
        company=company,
        source=EvidenceSource.INSIDER,
        category=transaction.transaction_type,
        title=f"{transaction.insider} - {transaction.transaction_type}",
        description=transaction.footnote,
        relevance=0,
        importance=EvidenceImportance.LOW,
        url=transaction.filing_url,
        published_at=transaction.transaction_date
    )