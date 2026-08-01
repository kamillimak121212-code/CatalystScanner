from app.models.evidence import EvidenceImportance

from app.company_intelligence.ai_rule_engine import (
    apply_ai_rules
)


def calculate_importance(understanding, evaluation):

    if understanding is None:
        return EvidenceImportance.LOW

    # Artykuł nie dotyczy analizowanej spółki
    if not understanding.is_relevant:
        return EvidenceImportance.LOW

    score = 0

    # ---------- Company Intelligence ----------

    if evaluation is not None:
        score += evaluation.score

    # ---------- AI Rule Engine ----------

    ai_score, _ = apply_ai_rules(
        understanding
    )

    score += ai_score

    # ---------- Relevance ----------

    score += understanding.relevance_score

    # ---------- Confidence ----------

    confidence = understanding.confidence

    if confidence >= 95:
        score += 20

    elif confidence >= 90:
        score += 10

    elif confidence < 70:
        score -= 10

    # ---------- Event Type Bonus ----------

    major_events = {

        "PARTNERSHIP",
        "CONTRACT",
        "ACQUISITION",
        "MERGER",
        "EARNINGS",
        "GUIDANCE",
        "PRODUCT_LAUNCH",
        "FDA_APPROVAL"

    }

    if understanding.event_type in major_events:
        score += 30

    # ---------- Final ----------

    if score >= 250:
        return EvidenceImportance.CRITICAL

    if score >= 170:
        return EvidenceImportance.HIGH

    if score >= 90:
        return EvidenceImportance.MEDIUM

    return EvidenceImportance.LOW