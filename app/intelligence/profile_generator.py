import json

from openai import OpenAI

from app.config.settings import settings
from app.intelligence.profile_mapper import ProfileMapper

print("PROFILE GENERATOR LOADED")

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


class ProfileGenerator:

    @staticmethod
    def generate(company):

        prompt = f"""
You are an experienced equity research analyst.

Create a detailed investment intelligence profile for the company below.

Ticker:
{company.ticker}

Company:
{company.name}

Rules:

- Return ONLY valid JSON.
- Do not include markdown.
- Do not explain anything.
- Use official names.
- Include aliases whenever they are commonly used.
- mportance must be one of:

CORE
HIGH
MEDIUM
LOW

Meaning:

CORE = essential for the company
HIGH = very important
MEDIUM = important
LOW = supporting.
- Focus on information useful for investors.

Return exactly this structure:

{{
    "sector": "",
    "industry": "",
    "description": "",

    "products": [
        {{
            "name": "",
            "aliases": [],
            "importance": 90
        }}
    ],

    "customers": [
        {{
            "company": "",
            "aliases": [],
            "relation": "customer",
            "importance": 70
        }}
    ],

    "suppliers": [
        {{
            "company": "",
            "aliases": [],
            "relation": "supplier",
            "importance": 70
        }}
    ],

    "competitors": [
        {{
            "company": "",
            "aliases": [],
            "relation": "competitor",
            "importance": 60
        }}
    ],

    "technologies": [
        {{
            "name": "",
            "aliases": [],
            "importance": 70
        }}
    ],

    "people": [
        {{
            "name": "",
            "aliases": [],
            "importance": 90
        }}
    ],

    "keywords": [
        {{
            "value": "",
            "importance": 50
        }}
    ]
}}

Requirements:

- Include 5-15 major products.
- Include major technologies.
- Include CEO and key executives.
- Include largest suppliers.
- Include largest customers.
- Include strongest competitors.
- Include the most important investment keywords.
- Prefer specific product names instead of generic terms.
- Prefer company names instead of industries.
- Include abbreviations as aliases (for example TSMC, AWS, GB200, CUDA).
"""

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            text={
                "format": {
                    "type": "json_object"
                }
            }
        )

        data = json.loads(response.output_text)

        profile = ProfileMapper.from_json(
            company,
            data
        )

        print(f"\n{'=' * 60}")
        print(f"Profile generated for {company.ticker}")
        print(f"{'=' * 60}")

        print(f"Sector: {profile.sector}")
        print(f"Industry: {profile.industry}")
        print(f"Products: {len(profile.products)}")
        print(f"People: {len(profile.people)}")
        print(f"Keywords: {len(profile.keywords)}")

        print("\nProducts:")
        for product in profile.products[:10]:
            print(f" - {product.name}")

        print("\nPeople:")
        for person in profile.people[:10]:
            print(f" - {person.name}")

        print("=" * 60)

        return profile