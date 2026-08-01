from abc import ABC
from abc import abstractmethod


class BaseRisk(ABC):

    @abstractmethod
    def apply(
        self,
        result,
        risk
    ):
        pass