from .vehicle import Vehicle


class Airplane(Vehicle):
    def __init__(self, manufacturer, model, max_weight, max_capacity):
        super().__init__(manufacturer=manufacturer, model=model, max_capacity=max_capacity, wheels=6)
        self.top_speed = 650 #650mph aka mach 0.85
        self.max_weight = max_weight
        self.max_altitiude = 42000 #max altitude of commercial flights

    
    def take_off(self):
        print("Please buckle your seat belts for take off")
        self.speed_up(180) #takeoff speed
        self.display_speed()

    
    def landing(self):
        print("Now arriving in Atlanta")
    

        