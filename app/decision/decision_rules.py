from app.models.event_type import EventType
from app.models.evidence import EvidenceImportance


# --------------------------------------------------
# Event Type
# --------------------------------------------------

EVENT_SCORES = {

    EventType.UNKNOWN: 0,

    EventType.PRODUCT_LAUNCH: 20,
    EventType.PRODUCT_DELAY: -15,
    EventType.PRODUCT_RECALL: -20,

    EventType.PARTNERSHIP: 18,
    EventType.CONTRACT: 18,

    EventType.ACQUISITION: 20,
    EventType.MERGER: 20,

    EventType.EARNINGS: 20,
    EventType.GUIDANCE: 18,

    EventType.CEO_CHANGE: 8,
    EventType.EXECUTIVE_CHANGE: 5,

    EventType.ANALYST_UPGRADE: 10,
    EventType.ANALYST_DOWNGRADE: -10,

    EventType.INSIDER_BUY: 18,
    EventType.INSIDER_SELL: -15,

    EventType.FDA_APPROVAL: 20,

    EventType.REGULATION: 10,

    EventType.LAWSUIT: -20,

    EventType.SECURITY_INCIDENT: -20,

    EventType.MACRO: 5
}


# --------------------------------------------------
# Importance
# --------------------------------------------------

IMPORTANCE_SCORES = {

    EvidenceImportance.LOW: 2,

    EvidenceImportance.MEDIUM: 8,

    EvidenceImportance.HIGH: 15,

    EvidenceImportance.CRITICAL: 20
}