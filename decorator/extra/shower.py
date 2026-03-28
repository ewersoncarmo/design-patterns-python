from dataclasses import dataclass

from decorator.extra.extra_service import ExtraService
from decorator.pet_service import PetService


@dataclass
class Shower(ExtraService):
    _pet_service: PetService

    def description(self) -> str:
        return self.pet_service.description() + ', Shower'

    def cost(self) -> float:
        return self.pet_service.cost() + 35.0