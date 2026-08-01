def build_thesis(event, narrative):

    if event.theme == "AI Infrastructure":

        return (
            "Increasing AI infrastructure investments may "
            "strengthen long-term demand for NVIDIA GPUs."
        )

    if event.theme == "Earnings":

        return (
            "Recent financial results may materially affect "
            "future valuation and investor sentiment."
        )

    if event.theme == "M&A":

        return (
            "The announced transaction could significantly "
            "change the company's future growth prospects."
        )

    return (
        "Current evidence should be monitored for additional "
        "confirmation."
    )