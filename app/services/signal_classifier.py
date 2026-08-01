BULLISH_CATEGORIES = {
    "Customer",
    "Partner",
    "Product",
    "Technology",
    "Catalyst"
}

BEARISH_CATEGORIES = {
    "Competitor"
}


def classify_signals(signals):

    bullish = []
    bearish = []

    for signal in signals:

        if signal.signal_type in BULLISH_CATEGORIES:
            bullish.append(signal)

        elif signal.signal_type in BEARISH_CATEGORIES:
            bearish.append(signal)

    return bullish, bearish