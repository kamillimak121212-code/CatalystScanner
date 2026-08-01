class AssetProfile:

    def __init__(self):

        self.symbol = ""
        self.name = ""

        self.asset_type = ""

        self.sector = ""
        self.industry = ""

        self.people = []
        self.products = []

        self.customers = []
        self.suppliers = []

        self.related_assets = []

        self.keywords = []

        self.catalysts = []

    def evaluate(self, evidence):

        raise NotImplementedError()