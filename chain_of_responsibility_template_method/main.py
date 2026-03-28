from chain_of_responsibility_template_method.discount_calculator import *
from chain_of_responsibility_template_method.model.budget import Budget
from chain_of_responsibility_template_method.model.item import Item

budget = Budget()
budget.add_item(Item('Pen', 250))
budget.add_item(Item('Pencil', 250))
budget.add_item(Item('Eraser', 250))
budget.add_item(Item('Notebook', 250))
budget.add_item(Item('Pencil sharpner', 250))

print(calculate(budget))