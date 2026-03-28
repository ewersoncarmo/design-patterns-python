from dataclasses import dataclass, field
from typing import List

from chain_of_responsibility_template_method.model.item import Item


@dataclass
class Budget:
    items: List[Item] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def value(self) -> float:
        return round(sum(item.value for item in self.items), 2)