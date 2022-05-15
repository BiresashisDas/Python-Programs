# Author :- Biresashis Das

#Here I will show how to use a Built-in Datatypes.
#Note :- I will also use the type function to chech what is the data type of a variable

name = input("What is your name : ")
print(type(name)) #type() function
string = len(name)
print("The number of characters in your name is : ",string)

#if we want to take a integer we should use int() function.
num1 = int(input("Enter the first inetger : "))   #uses int()
num2 = int(input("Enter the second integer : "))  #uses int()

print("Type of num1 : ", type(num1))
print("Type of num2 : ", type(num2))
result = num1 + num2
print(f"The addition of {num1} and {num2} is : {result}")   #uses f string

#if we want to take a floating point values we should use float() datatype.
num1 = float(input("Enter the first inetger : "))   #uses float()
num2 = float(input("Enter the second integer : "))  #uses float()

print("Type of num1 : ", type(num1))
print("Type of num2 : ", type(num2))
result = num1 + num2
print(f"The addition of {num1} and {num2} is : {result}")   #uses f string



