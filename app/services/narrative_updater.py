from app.services.confidence_engine import (
    update_confidence
)


def update_narrative(
    narrative,
    evidence
):

    update_confidence(
        narrative,
        evidence
    )

    if evidence.title not in narrative.drivers:

        narrative.drivers.append(
            evidence.title
        )

    if evidence.company.ticker not in narrative.companies:

        narrative.companies.append(
            evidence.company.ticker
        )

    narrative.summary = (
        f"{len(narrative.evidence)} supporting evidence collected."
    )

    return narrative