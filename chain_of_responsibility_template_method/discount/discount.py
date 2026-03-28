from abc import ABC, abstractmethod

from chain_of_responsibility_template_method.model.budget import Budget


class Discount(ABC):

    def __init__(self, next_discount: "Discount"):
        self._next_discount = next_discount

    def calculate(self, budget: Budget) -> float:
        if self.can_apply(budget):
            return self.apply(budget)

        return self._next_discount.calculate(budget)

    @abstractmethod
    def can_apply(self, budget: Budget) -> bool:
        pass

    @abstractmethod
    def apply(self, budget: Budget) -> float:
        pass