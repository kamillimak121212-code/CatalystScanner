from app.logger.logger import logger


class AIGateStage:

    MIN_TITLE_LENGTH = 20
    MIN_DESCRIPTION_LENGTH = 100

    def process(
        self,
        result
    ):

        evidence = result.evidence

        # SEC zawsze przepuszczamy.
        # Później dodamy osobne reguły dla SEC.
        if evidence.source.name == "SEC":
            return result

        title = (
            evidence.title or ""
        ).strip()

        description = (
            evidence.description or ""
        ).strip()

        if len(title) < self.MIN_TITLE_LENGTH:

            logger.info(
                f"AI Gate -> SKIP {evidence.company.ticker} | title too short"
            )

            result.should_skip_ai = True

            return result

        if len(description) < self.MIN_DESCRIPTION_LENGTH:

            logger.info(
                f"AI Gate -> SKIP {evidence.company.ticker} | description too short"
            )

            result.should_skip_ai = True

            return result

        text = (
            f"{title} {description}"
        ).lower()

        company = evidence.company

        if (
            company.ticker.lower() not in text
            and company.name.lower() not in text
        ):

            logger.info(
                f"AI Gate -> SKIP {company.ticker} | company not found"
            )

            result.should_skip_ai = True

            return result

        logger.info(
            f"AI Gate -> PASS {company.ticker}"
        )

        result.should_skip_ai = False

        return result