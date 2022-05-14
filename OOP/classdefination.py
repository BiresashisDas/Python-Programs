# Author :- Biresashis Das

# Here I will show you how to create a Class.

class myfirstclass:

    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

person = myfirstclass("Abhishek", 22)

print(f"Name of the person : {person.name}")
print(f"Age of the person : {person.age}")



