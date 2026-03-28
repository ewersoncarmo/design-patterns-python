from abc import ABC, abstractmethod


class PetService(ABC):

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass