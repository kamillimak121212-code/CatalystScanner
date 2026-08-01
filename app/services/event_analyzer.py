from app.models.event_analysis import EventAnalysis
from app.models.evidence import EvidenceImportance


def analyze_event(event):

    analysis = EventAnalysis()

    analysis.evidence_count = event.evidence_count()

    relevance_sum = 0
    importance_sum = 0

    for evidence in event.evidence:

        relevance_sum += evidence.relevance
        importance_sum += evidence.importance.value

        # Event Score
        analysis.score += evidence.relevance

        if evidence.importance == EvidenceImportance.HIGH:
            analysis.high_importance += 1
            analysis.score += 25

        elif evidence.importance == EvidenceImportance.CRITICAL:
            analysis.critical_importance += 1
            analysis.score += 50

    if analysis.evidence_count > 0:

        analysis.average_relevance = round(
            relevance_sum / analysis.evidence_count
        )

        analysis.average_importance = round(
            importance_sum / analysis.evidence_count,
            2
        )

    # Confidence

    if analysis.score == 0:
        analysis.confidence = 0
    else:
        confidence = 0

        confidence += analysis.average_relevance * 0.4
        confidence += min(analysis.evidence_count * 10, 30)
        confidence += analysis.high_importance * 10
        confidence += analysis.critical_importance * 20

        analysis.confidence = min(round(confidence), 100)
    return analysis