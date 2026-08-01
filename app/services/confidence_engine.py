def update_confidence(
    narrative,
    evidence
):

    score = evidence.relevance

    if evidence.importance.name == "MEDIUM":
        score += 10

    elif evidence.importance.name == "HIGH":
        score += 20

    elif evidence.importance.name == "CRITICAL":
        score += 30

    narrative.confidence = min(
        100,
        narrative.confidence + score // 5
    )

    narrative.add_evidence(
        evidence
    )

    narrative.add_history(
        evidence.title
    )

    return narrative.confidence