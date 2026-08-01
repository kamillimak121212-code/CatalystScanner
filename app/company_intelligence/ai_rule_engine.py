from app.company_intelligence.ai_rules import AI_RULES


def apply_ai_rules(understanding):

    if understanding is None:
        return 0, []

    if not understanding.is_relevant:
        return 0, []

    score = 0
    matched = []

    text = " ".join([
        understanding.summary,
        understanding.reason,
        understanding.event,
        understanding.event_type,
        understanding.sentiment,
        understanding.relevance_reason
    ]).lower()

    for rule in AI_RULES:

        if any(
            keyword.lower() in text
            for keyword in rule["keywords"]
        ):

            score += rule["importance"]

            matched.append({
                "name": rule["catalyst"],
                "score": rule["importance"]
            })

    score = min(score, 100)

    return score, matched