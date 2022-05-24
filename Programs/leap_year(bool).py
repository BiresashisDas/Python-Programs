# Author :- Biresashis Das

# This program is to find whether a year is a leap year or not.
# NOTE :- If the program will print "True" it means it's a leap year and if it print "False" it means it's not a leap year.

def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

year = int(input("Enter the year you want : "))
print (is_leap(year))



