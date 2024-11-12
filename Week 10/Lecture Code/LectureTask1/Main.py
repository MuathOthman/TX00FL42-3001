import random
from Car import Car

# Create a list to hold the car objects
carList = []
running = True

# Generate 10 Car objects and add them to the carList
for i in range(10):
    registration_number = f"ABC-{i+1}"
    max_speed = random.randint(100, 200)
    carFactory = Car(registration_number, max_speed)
    carList.append(carFactory)

# Simulate the race
round_number = 1
while running:
    print(f"\nRound {round_number}:")
    round_number += 1
    for car in carList:
        # Accelerate each car randomly and drive it for 1 hour
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

    # Print the status of each car after each round
    for car in carList:
        print(f"{car.registration_number}: {car.travelled_distance} km")

    # Check if any car has travelled more than 200 km
    for car in carList:
        if car.travelled_distance > 200:
            running = False
            break

# Display final details of each car
print("\nFinal details of each car:")
for car in carList:
    car.displayDetails()
