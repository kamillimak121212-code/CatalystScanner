import re

from bs4 import BeautifulSoup


class SECFilingParser:

    def parse(
        self,
        html
    ):

        if not html:
            return ""

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        text = soup.get_text(
            separator=" "
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()