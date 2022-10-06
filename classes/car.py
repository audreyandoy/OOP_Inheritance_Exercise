from .vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, manufacturer, model, year, top_speed):
        super().__init__(manufacturer, model, max_capacity=5, wheels=4)
        self.year = year
        self.top_speed = top_speed

    
    def car_horn(self):
        print("meep meep")

        