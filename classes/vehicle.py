class Vehicle:
    def __init__(self, manufacturer, model, max_capacity, wheels):
        self.manufacturer = manufacturer
        self.model = model
        self.max_capacity = max_capacity
        self.wheels = wheels
        self.current_speed = 0

    def speed_up(self, rate):
        self.current_speed += rate 

    def slow_down(self, rate):
        self.current_speed -= rate

    def display_speed(self):
        print(f"Current speed is {self.current_speed} mph")