class Company:

    def __init__(
        self,
        company_id,
        ticker,
        name,
        exchange,
        cik=None,
        is_active=True
    ):

        self.id = company_id
        self.ticker = ticker
        self.name = name
        self.exchange = exchange
        self.cik = cik

        self.is_active = is_active

    def __str__(self):

        return (
            f"{self.ticker} | "
            f"{self.name} | "
            f"{self.exchange}"
        )