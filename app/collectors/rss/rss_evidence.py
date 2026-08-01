from app.services.ai_service import (
    analyze_article
)

from app.services.signal_builder import (
    build_signals
)

from app.services.importance_engine import (
    calculate_importance
)

from app.intelligence.profile_loader import (
    ProfileLoader
)

from app.models.evidence import (
    Evidence,
    EvidenceSource
)


def build_evidence(news, company):

    understanding = analyze_article(
        company,
        news.title,
        news.summary
    )

    # AI uznało artykuł za nieistotny
    if not understanding.is_relevant:
        return None

    profile = ProfileLoader.load(company)

    # Company Intelligence analizuje artykuł
    evaluation = profile.evaluate(news)

    # Importance liczone z Company Intelligence
    importance = calculate_importance(
        understanding,
        evaluation
    )

    evidence = Evidence(
        company=company,
        source=EvidenceSource.RSS,
        category=understanding.event,
        title=news.title,
        description=news.summary,
        relevance=understanding.relevance_score,
        importance=importance,
        url=news.url,
        published_at=news.published_at
    )

    evidence.understanding = understanding
    evidence.evaluation = evaluation
    evidence.signals = build_signals(evidence)

    return evidence