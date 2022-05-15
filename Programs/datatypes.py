# Author :- Biresashis Das

# Note :- We can get the data type of any object using the type() function

x = "HelloWorld"
print(f"The type of {x} is  {type(x)}")
x = 23
print(f"The type of {x} is  {type(x)}")
x = 32.4
print(f"The type of {x} is  {type(x)}")
x = 3j
print(f"The type of {x} is  {type(x)}")
x = ["apple", "mango", "orange"]
print(f"The type of {x} is  {type(x)}")
x = ("apple", "mango", "orange")
print(f"The type of {x} is  {type(x)}")
x = {"name" : "Rohit", "age" : 26}
print(f"The type of {x} is  {type(x)}")
x = {"apple", "mango", "orange"}
print(f"The type of {x} is  {type(x)}")
x = True
y = False
print(f"The type of {x} and {y} is  {type(x)} and {type(y)}")


# Expected Output
# The type of HelloWorld is  <class 'str'>
# The type of 23 is  <class 'int'>
# The type of 32.4 is  <class 'float'>
# The type of ['apple', 'mango', 'orange'] is  <class 'list'>
# The type of ('apple', 'mango', 'orange') is  <class 'tuple'>
# The type of {'name': 'Rohit', 'age': 26} is  <class 'dict'>
# The type of {'apple', 'orange', 'mango'} is  <class 'set'>
# The type of True and False is  <class 'bool'> and <class 'bool'>



