from .discount import Discount
from ..model.budget import Budget


class NoDiscount(Discount):

    def __init__(self):
        super().__init__(None)

    def can_apply(self, budget: Budget) -> bool:
        return True

    def apply(self, budget: Budget) -> float:
        print('No discount')
        return 0