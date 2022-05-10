# Author :- Biresashis Das

# How to calculate a Body mass index.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

#The BMI is calculated by dividing a person's weight(in kg) by the square of their height(in m).
BMI = weight / (height**2)
print(round(BMI))

if BMI < 18.5:
    print(f"Your BMi is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
