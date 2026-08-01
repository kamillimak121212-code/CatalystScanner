from app.services.catalyst_detector import detect_catalysts
from app.models.narrative import Narrative


THEME_TITLES = {
    "AI Infrastructure": "AI Infrastructure Expansion",
    "Earnings": "Strong Earnings Momentum",
    "M&A": "Strategic Acquisition",
    "Share Buyback": "Capital Return Program",
    "Insider Buying": "Management Buying Shares",
    "China Export": "China Export Restrictions",
    "General": "General Market News"
}


def build_narrative(event):

    narrative = Narrative()

    catalysts = []

    for evidence in event.evidence:
        catalysts.extend(
            detect_catalysts(evidence)
        )

    narrative.title = THEME_TITLES.get(
        event.theme,
        event.theme
    )

    narrative.companies.append(
        event.company.ticker
    )

    narrative.confidence = (
        event.analysis.confidence
        if event.analysis
        else 0
    )

    for evidence in event.evidence:

        if evidence.relevance >= 70:
            narrative.drivers.append(
                evidence.title
            )

    if catalysts:

        categories = sorted({
            item.category
            for item in catalysts
            if item.category
        })

        narrative.summary = (
            "Detected: "
            + ", ".join(categories)
        )

    else:

        narrative.summary = (
            "No catalysts detected."
        )

    return narrative