import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.models.event_type import EventType

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


class EventClassifier:

    @staticmethod
    def classify(evidence):

        company = evidence.company

        prompt = f"""
You are a senior equity research analyst.

Your task is to determine whether the following article is materially relevant
to the specified company.

Company:
{company.name} ({company.ticker})

Article title:
{evidence.title}

Article description:
{evidence.description}

If the article is NOT materially related to this company, return:

{{
    "relevant": false
}}

If it IS relevant, return ONLY valid JSON in this format:

{{
    "relevant": true,
    "event_type": "",
    "sentiment": "",
    "confidence": 0,
    "summary": ""
}}

Rules:

- Ignore articles about other companies.
- Ignore ETF articles.
- Ignore market commentary unless it directly affects this company.
- Ignore clickbait comparisons.
- Ignore generic AI articles unless this company is a main subject.
- Only classify events that can realistically influence this company's value.

event_type must be one of:

UNKNOWN
PRODUCT_LAUNCH
PRODUCT_DELAY
PRODUCT_RECALL
PARTNERSHIP
CONTRACT
ACQUISITION
MERGER
EARNINGS
GUIDANCE
CEO_CHANGE
EXECUTIVE_CHANGE
ANALYST_UPGRADE
ANALYST_DOWNGRADE
INSIDER_BUY
INSIDER_SELL
FDA_APPROVAL
REGULATION
LAWSUIT
SECURITY_INCIDENT
MACRO

sentiment must be one of:

POSITIVE
NEGATIVE
NEUTRAL
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

        print("\nEVENT CLASSIFIER")
        print(data)

        if not data.get("relevant", True):

            return {
                "event_type": EventType.UNKNOWN,
                "sentiment": "NEUTRAL",
                "confidence": 1.0,
                "summary": "Article not relevant"
            }

        return {
            "event_type": EventType(data["event_type"]),
            "sentiment": data["sentiment"],
            "confidence": data["confidence"],
            "summary": data["summary"]
        }