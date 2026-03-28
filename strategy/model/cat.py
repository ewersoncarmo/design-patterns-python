from .pet import Pet
from ..behavior.meow_sound import MeowSound

class Cat(Pet):

    def __init__(self, name: str) -> None:
        super().__init__(name, MeowSound())