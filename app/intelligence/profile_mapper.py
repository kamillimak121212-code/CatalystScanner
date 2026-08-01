from app.intelligence.profile import CompanyProfile

from app.intelligence.models.keyword import Keyword
from app.intelligence.models.person import Person
from app.intelligence.models.product import Product
from app.intelligence.models.relation import CompanyRelation


class ProfileMapper:

    @staticmethod
    def _importance(value):

        if isinstance(value, (int, float)):
            return int(value)

        mapping = {

            "CORE": 10,
            "HIGH": 7,
            "MEDIUM": 4,
            "LOW": 2

        }

        return mapping.get(
            str(value).upper(),
            5
        )

    @staticmethod
    def from_json(company, data):

        profile = CompanyProfile()

        profile.ticker = company.ticker
        profile.name = company.name

        profile.sector = data.get("sector", "")
        profile.industry = data.get("industry", "")
        profile.description = data.get("description", "")

        # Products
        profile.products = [
            Product(
                name=item.get("name", ""),
                aliases=item.get("aliases", []),
                importance=ProfileMapper._importance(
                    item.get("importance", "MEDIUM")
                )
            )
            for item in data.get("products", [])
        ]

        # People
        profile.people = [
            Person(
                name=item.get("name", ""),
                aliases=item.get("aliases", []),
                importance=ProfileMapper._importance(
                    item.get("importance", "MEDIUM")
                )
            )
            for item in data.get("people", [])
        ]

        # Customers
        profile.customers = [
            CompanyRelation(
                company=item.get("company", ""),
                relation="customer",
                aliases=item.get("aliases", []),
                importance=ProfileMapper._importance(
                    item.get("importance", "MEDIUM")
                )
            )
            for item in data.get("customers", [])
        ]

        # Suppliers
        profile.suppliers = [
            CompanyRelation(
                company=item.get("company", ""),
                relation="supplier",
                aliases=item.get("aliases", []),
                importance=ProfileMapper._importance(
                    item.get("importance", "MEDIUM")
                )
            )
            for item in data.get("suppliers", [])
        ]

        # Competitors
        profile.competitors = [
            CompanyRelation(
                company=item.get("company", ""),
                relation="competitor",
                aliases=item.get("aliases", []),
                importance=ProfileMapper._importance(
                    item.get("importance", "MEDIUM")
                )
            )
            for item in data.get("competitors", [])
        ]

        # Technologies
        profile.technologies = [
            Product(
                name=item.get("name", ""),
                aliases=item.get("aliases", []),
                importance=ProfileMapper._importance(
                    item.get("importance", "MEDIUM")
                )
            )
            for item in data.get("technologies", [])
        ]

        # Keywords
        profile.keywords = [
            Keyword(
                value=item.get("value", ""),
                importance=ProfileMapper._importance(
                    item.get("importance", "MEDIUM")
                )
            )
            for item in data.get("keywords", [])
        ]

        return profile