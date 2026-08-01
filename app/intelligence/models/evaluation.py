class CompanyEvaluation:

    def __init__(self):

        self.score = 0

        self.matches = []

        self.reason = ""

        self.company_score = 0
        self.keyword_score = 0
        self.product_score = 0
        self.people_score = 0
        self.customer_score = 0
        self.supplier_score = 0
        self.competitor_score = 0
        self.technology_score = 0

    def add(
        self,
        category,
        name,
        importance,
        weight=1.0
    ):

        value = importance * weight

        self.score += value

        self.matches.append(
            {
                "category": category,
                "name": name,
                "score": value
            }
        )

        if category == "company":

            self.company_score += value

        elif category == "keyword":

            self.keyword_score += value

        elif category == "product":

            self.product_score += value

        elif category == "technology":

            self.technology_score += value

        elif category == "person":

            self.people_score += value

        elif category == "customer":

            self.customer_score += value

        elif category == "supplier":

            self.supplier_score += value

        elif category == "competitor":

            self.competitor_score += value

    def finalize(self):

        self.score = int(min(self.score, 100))

        names = []

        for match in self.matches:

            if match["name"] not in names:

                names.append(
                    match["name"]
                )

        self.reason = ", ".join(names)

    def __str__(self):

        matches = "\n".join(

            f"- {match['category']}: "
            f"{match['name']} "
            f"({match['score']:.1f})"

            for match in self.matches

        )

        if not matches:

            matches = "None"

        return (

            f"Score            : {self.score}\n"
            f"Company Score    : {self.company_score:.1f}\n"
            f"Keyword Score    : {self.keyword_score:.1f}\n"
            f"Product Score    : {self.product_score:.1f}\n"
            f"Technology Score : {self.technology_score:.1f}\n"
            f"People Score     : {self.people_score:.1f}\n"
            f"Customer Score   : {self.customer_score:.1f}\n"
            f"Supplier Score   : {self.supplier_score:.1f}\n"
            f"Competitor Score : {self.competitor_score:.1f}\n"
            f"Reason           : {self.reason}\n"
            f"Matches:\n{matches}"

        )