# Author :- Biresashis Das

# Here I will show you how to create a Inheritance Class.
# Inheritance :- It is a class that inherits the property of another class.

class Car:

    def __init__(self):
        self.num_of_tires = 4

    def run(self):
        print("Normal Cars needs petrol/deisel to run on roads.")

class EV_Cars(Car):

    def __init__(self):
        super().__init__()

    def run(self):
        super().run()
        print("Electric vehicals cars need charge to run on roads.")

    def car_type(self):
        print("Avinya is a electric type of car.")

car = EV_Cars()
car.run()
print(f"Total number of Tires a car have = {car.num_of_tires} tires")
car.car_type()




