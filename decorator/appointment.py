from decorator.pet_service import PetService


class Appointment(PetService):

    def description(self) -> str:
        return 'Appointment'

    def cost(self) -> float:
        return 90.0