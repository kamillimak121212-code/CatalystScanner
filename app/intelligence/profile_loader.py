from app.intelligence.profile_generator import (
    ProfileGenerator
)
from app.intelligence.profile_repository import (
    ProfileRepository
)


class ProfileLoader:

    @staticmethod
    def load(asset):

        profile = ProfileRepository.get(
            asset.ticker
        )

        if profile is not None:

            print(
                f"Profile loaded from cache: {asset.ticker}"
            )

            return profile

        print(
            f"Generating profile for {asset.ticker}..."
        )

        profile = ProfileGenerator.generate(
            asset
        )

        ProfileRepository.save(
            asset.ticker,
            profile
        )

        return profile