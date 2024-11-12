class Car:
    def __init__(self, prop1, prop2, prop3 = 0, prop4 = 0):
        self.registration_number = prop1
        self.maximum_speed = prop2
        self.current_speed = prop3
        self.travelled_distance = prop4

    def displayDetails(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.maximum_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Travelled Distance: {self.travelled_distance} km")
        print()

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
            #print("You can't exceed the maximum speed")
            #print()
        elif self.current_speed < 0:
            self.current_speed = 0
            #print("Current speed is zero")
            #print()
        #print("Current Speed: " + str(self.current_speed) + "km/h")

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours
        #print(f"Travelled Distance: {self.travelled_distance} km")
