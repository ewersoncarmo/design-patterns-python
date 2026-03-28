from decorator.appointment import Appointment
from decorator.extra.shower import Shower
from decorator.extra.vaccine import Vaccine

pet_service = Vaccine(
    Shower(
        Appointment()))

print(pet_service.description() + ', ' + str(pet_service.cost()))