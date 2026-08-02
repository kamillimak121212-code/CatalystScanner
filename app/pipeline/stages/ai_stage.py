from app.intelligence.profile_loader import ProfileLoader

from app.services.ai_service import (
    analyze_article
)

from app.logger.logger import logger


class AIStage:

    def process(self, result):

        evidence = result.evidence

        if evidence.source.name not in (
            "RSS",
            "SEC"
        ):
            return result

        result.profile = ProfileLoader.load(
            evidence.company
        )

        if evidence.source.name == "SEC":

            text = (
                evidence.document_text
                if evidence.document_text
                else evidence.description
            )

            logger.info(
                f"SEC AI -> {evidence.company.ticker} | text length: {len(text)}"
            )

            try:

                result.understanding = analyze_article(
                    evidence.company,
                    evidence.title,
                    text,
                    result.profile
                )

                logger.info(
                    f"SEC AI OK -> {evidence.company.ticker}"
                )

            except Exception as e:

                logger.exception(
                    f"SEC AI FAILED -> {evidence.company.ticker}: {e}"
                )

                result.understanding = None

            return result

        title = evidence.title.lower()
        description = evidence.description.lower()

        text = f"{title} {description}"

        company = evidence.company

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