from app.utils.news_hash import create_news_hash


class NewsHashService:

    def create(
        self,
        news
    ):

        return create_news_hash(

            news.title,

            news.summary,

            news.url

        )