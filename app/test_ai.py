from app.test_articles import TEST_ARTICLES
from app.services.ai_service import analyze_article

for article in TEST_ARTICLES:

    result = analyze_article(
        article["title"],
        article["description"]
    )

    print("=" * 60)
    print(article["title"])
    print()

    print("Relevant :", result.is_relevant)
    print("Relevance Score :", result.relevance_score)
    print("Confidence :", result.confidence)
    print("Event :", result.event)
    print("Reason :", result.reason)