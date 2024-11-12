import random


class Race:
    def __init__(self, name, km, Carlist):
        self.name = name
        self.distance = km
        self.cars = Carlist

    def hour_passes(self, hours):
        for i in range(hours):
            for car in self.cars:
                car.accelerate(random.randint(-10, 15))
                car.drive(1)

    def print_status(self):
        for car in self.cars:
            car.displayDetails()

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance > self.distance:
                return True