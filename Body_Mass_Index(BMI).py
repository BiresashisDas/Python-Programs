#How to calculate a Body mass index.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

#The BMI is calculated by dividing a person's weight(in kg) by the square of their height(in m).
BMI = weight / (height**2)
print(round(BMI))


