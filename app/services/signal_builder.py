from app.models.signal import Signal
from app.company_intelligence.profile_manager import (
    ProfileManager
)


def build_signals(evidence):

    profile = ProfileManager.get_profile(
        evidence.company.ticker
    )

    if profile is None:
        return []

    evaluation = profile.evaluate(evidence)

    signals = []

    for match in evaluation.matches:

        item = match["item"]

        signals.append(
            Signal(
                signal_type=item.category,
                value=item.name,
                source="Company Intelligence",
                importance=item.importance,
                confidence=100,
                reason=item.reason
            )
        )

    return signals