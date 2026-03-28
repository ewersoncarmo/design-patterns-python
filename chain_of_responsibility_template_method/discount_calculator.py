from chain_of_responsibility_template_method.discount.discount_for_five_itens import DiscountForFiveItens
from chain_of_responsibility_template_method.discount.discount_for_more_than_five_hundred_reais import \
    DiscountForMoreThanFiveHundredReais
from chain_of_responsibility_template_method.discount.no_discount import NoDiscount
from chain_of_responsibility_template_method.model.budget import Budget


def calculate(budget: Budget) -> float:
    print(f'Budget details: value {budget.value()}, items {len(budget.items)}')
    print('--------------')

    discount = DiscountForFiveItens()

    return discount.calculate(budget)