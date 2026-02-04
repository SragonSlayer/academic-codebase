# Lucas Swanson
import random

# Define the class for all of my cars
class Car:
    def __init__(self, EngineType, CarColor):
        self.EngineType = EngineType
        self.CarColor = CarColor

    def render(self):
        # Empty
        pass

# Make a random number from 11 to 19 to determine how many cars I have (Or want to have)
num_Cars = random.randint(11, 19)

# Initialize my list of MyCars
MyCars = []
# Loop through all the cars and give them random properties
for car in range(num_Cars):
    EngineType = "V" + str(random.randint(2,8))
    CarColor = "Red"                                    # I only buy red cars
    ThisCar = Car(EngineType, CarColor)
    MyCars.append(ThisCar)
    
odd_even = "odd" if num_Cars % 2 else "even"
print(f"There are an {odd_even} number of objects in the list.")

#End file with one blank line
