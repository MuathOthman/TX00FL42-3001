from Car import Car

car1 = Car("ABC-123", 142)

print(f"Car 1 \nRegistration: {car1.registration_number}\n"
      f"Maximum Speed: {car1.maximum_speed}\n"
      f"Current Speed: {car1.current_speed}\n"
      f"Travelled Distance: {car1.travelled_distance}")

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

car1.drive(3)

ca2 = Car("ABC-322", 200, 60, 2000)
ca2.drive(1.5)
#car1.accelerate(1230)