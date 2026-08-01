from app.models.catalyst_event import CatalystEvent
from app.services.theme_detector import detect_theme
from app.services.event_matcher import is_same_event
from app.services.event_repository import get_or_create_event


def build_event(evidence):

    theme = detect_theme(evidence)

    candidate = CatalystEvent(
        company=evidence.company,
        title=evidence.title,
        category=evidence.category,
        theme=theme
    )

    event = get_or_create_event(
        candidate,
        is_same_event
    )

    event.add_evidence(evidence)

    return event