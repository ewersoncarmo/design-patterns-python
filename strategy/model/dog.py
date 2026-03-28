from .pet import Pet
from ..behavior.bark_sound import BarkSound

class Dog(Pet):
    
    def __init__(self, name: str) -> None:
        super().__init__(name, BarkSound())