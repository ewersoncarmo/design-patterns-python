from .discount import Discount
from .no_discount import NoDiscount
from ..model.budget import Budget


class DiscountForMoreThanFiveHundredReais(Discount):

    def __init__(self):
        super().__init__(NoDiscount())

    def can_apply(self, budget: Budget) -> bool:
        print('Checking discount for more than five hundred reais')
        return budget.value() > 500.0

    def apply(self, budget: Budget) -> float:
        print('Applying discount for more than five hundred reais')
        return round(budget.value() * 0.07, 2)