from abc import ABC, abstractmethod


class BaseCollector(ABC):

    name = "BaseCollector"

    priority = 0

    enabled = True

    interval_minutes = 60

    asset_types = []

    sources = []

    @abstractmethod
    def collect(self):

        """
        Powinien zwrócić listę Evidence.
        """

        pass

    def __str__(self):

        return (
            f"{self.name} "
            f"(priority={self.priority})"
        )