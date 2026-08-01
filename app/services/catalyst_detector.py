from app.company_intelligence.profile_manager import (
    ProfileManager
)


def detect_catalysts(evidence):

    profile = ProfileManager.get_profile(
        evidence.company.ticker
    )

    if profile is None:
        return []

    evaluation = profile.evaluate(
        evidence
    )

    found = []

    for match in evaluation.matches:

        found.append(
            match["item"]
        )

    return found