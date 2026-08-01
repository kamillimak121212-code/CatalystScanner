from app.intelligence.profile_loader import ProfileLoader

from app.services.ai_service import (
    analyze_article
)


class AIStage:

    def process(self, result):

        evidence = result.evidence

        if evidence.source.name != "RSS":
            return result

        result.profile = ProfileLoader.load(
            evidence.company
        )

        title = evidence.title.lower()
        description = evidence.description.lower()

        text = f"{title} {description}"

        company = evidence.company

        keywords = [
            company.ticker.lower(),
            company.name.lower()
        ]

        if (
            company.ticker.lower() not in text
            and company.name.lower() not in text
        ):

            result.understanding = None

            return result

        result.understanding = analyze_article(
            company,
            evidence.title,
            evidence.description,
            result.profile
        )

        return result