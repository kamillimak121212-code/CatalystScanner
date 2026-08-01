class InsiderTransaction:

    def __init__(
        self,
        ticker="",
        insider="",
        role="",
        transaction_code="",
        transaction_type="",
        transaction_date="",
        shares=0,
        price=0.0,
        transaction_value=0.0,
        shares_after=0,
        ownership="",
        footnote="",
        filing_date="",
        filing_url=""
    ):

        self.ticker = ticker
        self.insider = insider

        self.role = role

        self.transaction_code = transaction_code
        self.transaction_type = transaction_type

        self.transaction_date = transaction_date

        self.shares = shares
        self.price = price
        self.transaction_value = transaction_value

        self.shares_after = shares_after
        self.ownership = ownership

        self.footnote = footnote

        self.filing_date = filing_date
        self.filing_url = filing_url

    def __str__(self):

        return (
            f"{self.ticker} | "
            f"{self.insider} | "
            f"{self.transaction_code} | "
            f"{self.shares:,.0f} shares | "
            f"${self.transaction_value:,.0f}"
        )