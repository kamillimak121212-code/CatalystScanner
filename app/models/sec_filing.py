class SecFiling:

    def __init__(
        self,
        filing_type="",
        item="",
        title="",
        description="",
        accession="",
        document="",
        url="",
        published_at=""
    ):

        self.filing_type = filing_type
        self.item = item

        self.title = title
        self.description = description

        self.accession = accession
        self.document = document

        self.url = url
        self.published_at = published_at

    def __str__(self):

        return (
            f"{self.filing_type}\n"
            f"{self.item}\n"
            f"{self.title}\n"
            f"{self.published_at}\n"
            f"{self.url}"
        )