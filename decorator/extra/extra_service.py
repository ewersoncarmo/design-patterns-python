from dataclasses import dataclass

from decorator.pet_service import PetService

@dataclass
class ExtraService(PetService):
    _pet_service: PetService

    def description(self) -> str:
        return self.description()

    def cost(self) -> float:
        return self.cost()

    @property
    def pet_service(self) -> PetService:
        return self._pet_service