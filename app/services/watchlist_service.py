from app.database.company_repository import (
    get_all_companies
)


class WatchlistService:

    def get_companies(self):

        companies = get_all_companies()

        return [

            company

            for company in companies

            if company.is_active

        ]