from dataclasses import dataclass

@dataclass
class Item:
    name: str
    _value: float

    @property
    def value(self) -> float:
        return self._value