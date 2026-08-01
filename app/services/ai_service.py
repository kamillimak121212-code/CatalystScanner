import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.models.evidence_understanding import (
    EvidenceUnderstanding
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_article(
    company,
    title,
    description,
    profile
):

    prompt = f"""
You are a senior equity research analyst.

You are analyzing news for:

Company:
{company.name} ({company.ticker})

The following Company Profile is BACKGROUND KNOWLEDGE ONLY.

{profile}

Analyze the article.

Determine:

1. Is the article materially relevant?
2. Event type
3. Sentiment
4. Summary
5. Confidence (integer from 0 to 100)

Confidence rules:

- Return ONLY an integer.
- Minimum = 0
- Maximum = 100.
- Never return decimals.
- Never return values between 0 and 1.
- 100 means extremely confident.
- 50 means uncertain.
- 0 means no confidence.

Return ONLY valid JSON.

{{
    "summary": "",
    "main_company": "",
    "event": "",
    "event_type": "",
    "sentiment": "",
    "reason": "",
    "related_companies": [],
    "products": [],
    "impact": "",
    "is_relevant": true,
    "relevance_reason": "",
    "relevance_score": 0,
    "confidence": 100
}}

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
        input=f"""
Title:
{title}

Description:
{description}

{prompt}
""",
        text={
            "format": {
                "type": "json_object"
            }
        }
    )

    data = json.loads(response.output_text)

    # --------------------------------------------------
    # Normalize confidence to 0-100
    # --------------------------------------------------

    confidence = data.get("confidence", 0)

    try:

        confidence = float(confidence)

        if confidence <= 1:
            confidence *= 100

        elif confidence <= 10:
            confidence *= 10

        confidence = int(round(confidence))

    except Exception:

        confidence = 0

    confidence = max(0, min(confidence, 100))

    # --------------------------------------------------
    # Normalize irrelevant articles
    # --------------------------------------------------

    if not data.get("is_relevant", False):

        data["main_company"] = ""

        data["products"] = []

        data["related_companies"] = []

        data["event"] = ""

        data["impact"] = ""

        data["relevance_score"] = 0

    return EvidenceUnderstanding(

        summary=data.get("summary", ""),
        main_company=data.get("main_company", ""),
        event=data.get("event", ""),
        event_type=data.get("event_type", "UNKNOWN"),
        sentiment=data.get("sentiment", "NEUTRAL"),
        reason=data.get("reason", ""),
        related_companies=data.get("related_companies", []),
        products=data.get("products", []),
        impact=data.get("impact", "Neutral"),
        is_relevant=data.get("is_relevant", False),
        relevance_reason=data.get("relevance_reason", ""),
        relevance_score=data.get("relevance_score", 0),
        confidence=confidence

    )


def analyze_evidence(evidence):

    print(evidence)

    return None