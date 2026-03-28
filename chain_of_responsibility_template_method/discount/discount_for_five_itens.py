from .discount import Discount
from .discount_for_more_than_five_hundred_reais import DiscountForMoreThanFiveHundredReais
from ..model.budget import Budget


class DiscountForFiveItens(Discount):

    def __init__(self):
        super().__init__(DiscountForMoreThanFiveHundredReais())

    def can_apply(self, budget: Budget) -> bool:
        print('Cheking discount for five itens')
        return len(budget.items) >= 5

    def apply(self, budget: Budget) -> float:
        print('Applyiing discount for five itens')
        return round(budget.value() * 0.1, 2)