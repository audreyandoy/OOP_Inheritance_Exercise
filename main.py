from classes.vehicle import Vehicle
from classes.car import Car
from classes.airplane import Airplane

car = Car("toyota", "camry", 2020, 200)
car.display_speed()

commercial_airplane = Airplane("Boeing", "747", 975000, 416)
commercial_airplane.take_off()

# max_capacity, wheels, name, manufacturer):