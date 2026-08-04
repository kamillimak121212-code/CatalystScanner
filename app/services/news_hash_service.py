from app.utils.news_hash import create_news_hash


class NewsHashService:

    def create(
        self,
        evidence
    ):

        return create_news_hash(

            evidence.company,

            evidence.title,

            evidence.description

        )