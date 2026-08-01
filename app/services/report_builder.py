from app.services.thesis_builder import build_thesis
from app.services.signal_classifier import classify_signals


def build_report(event, narrative):

    analysis = event.analysis

    thesis = build_thesis(event, narrative)

    signals = []

    for evidence in event.evidence:
        signals.extend(evidence.signals)

    bullish, bearish = classify_signals(signals)

    # Usuwanie duplikatów
    bullish = list({
        (s.signal_type, s.value): s
        for s in bullish
    }.values())

    bearish = list({
        (s.signal_type, s.value): s
        for s in bearish
    }.values())

    # Recommendation
    if analysis.confidence >= 80:
        recommendation = "🟢 STRONG BUY WATCH"

    elif analysis.confidence >= 60:
        recommendation = "🟡 WATCH"

    else:
        recommendation = "⚪ IGNORE"

    lines = []

    lines.append("")
    lines.append("╔════════════════════════════════════════════════════════════╗")
    lines.append("                     CATALYST REPORT")
    lines.append("╚════════════════════════════════════════════════════════════╝")
    lines.append("")

    lines.append(f"Ticker              : {event.company.ticker}")
    lines.append(f"Narrative           : {narrative.title}")
    lines.append(f"Recommendation      : {recommendation}")
    lines.append(f"Confidence          : {analysis.confidence}%")
    lines.append("")

    lines.append("────────────────────────────────────────────────────────────")
    lines.append("INVESTMENT THESIS")
    lines.append("────────────────────────────────────────────────────────────")
    lines.append(thesis)
    lines.append("")

    lines.append("────────────────────────────────────────────────────────────")
    lines.append("SUMMARY")
    lines.append("────────────────────────────────────────────────────────────")
    lines.append(narrative.summary)
    lines.append("")

    lines.append("────────────────────────────────────────────────────────────")
    lines.append("BULLISH SIGNALS")
    lines.append("────────────────────────────────────────────────────────────")

    if bullish:

        for signal in bullish:

            lines.append(
                f"✓ {signal.value:<20} {signal.signal_type}"
            )

    else:

        lines.append("None")

    lines.append("")

    lines.append("────────────────────────────────────────────────────────────")
    lines.append("BEARISH SIGNALS")
    lines.append("────────────────────────────────────────────────────────────")

    if bearish:

        for signal in bearish:

            lines.append(
                f"⚠ {signal.value:<20} {signal.signal_type}"
            )

    else:

        lines.append("None")

    lines.append("")

    lines.append("────────────────────────────────────────────────────────────")
    lines.append("SUPPORTING EVIDENCE")
    lines.append("────────────────────────────────────────────────────────────")

    for i, evidence in enumerate(event.evidence, start=1):

        lines.append(
            f"{i}. {evidence.title}"
        )

    lines.append("")

    lines.append("────────────────────────────────────────────────────────────")
    lines.append("STATISTICS")
    lines.append("────────────────────────────────────────────────────────────")
    lines.append(f"Evidence Count      : {analysis.evidence_count}")
    lines.append(f"Average Relevance   : {analysis.average_relevance}%")
    lines.append(f"Score               : {analysis.score}")
    lines.append(f"Confidence          : {analysis.confidence}%")

    lines.append("")

    lines.append("────────────────────────────────────────────────────────────")
    lines.append("WHY THIS MATTERS")
    lines.append("────────────────────────────────────────────────────────────")

    if bullish:

        lines.append(
            f"This narrative is supported by "
            f"{len(bullish)} bullish signal(s) "
            f"from Company Intelligence."
        )

    else:

        lines.append(
            "There is currently not enough evidence "
            "to support a strong investment thesis."
        )

    lines.append("")

    return "\n".join(lines)