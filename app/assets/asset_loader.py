class AssetLoader:

    def __init__(self):

        self._profiles = {}

    def register(
        self,
        symbol,
        profile
    ):

        self._profiles[
            symbol.upper()
        ] = profile

    def load(
        self,
        symbol
    ):

        return self._profiles.get(
            symbol.upper()
        )

    def exists(
        self,
        symbol
    ):

        return (
            symbol.upper()
            in self._profiles
        )

    def all_symbols(self):

        return sorted(
            self._profiles.keys()
        )