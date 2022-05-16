# Author :- Biresashis Das

import calendar

month = int(input("Enter the number of month : "))
year = int(input("Enter the Year : "))
date = int(input("Enter the Date : "))

result = int(input("Select a number. 0 for printing whole year, 1 for printing month, 2 for printing week and 3 for printing if a year is leap or not. : "))

if result == 0:
    # To print the calendar of the entire year
    print(calendar.calendar(year))

elif result == 1:
    # To print particular month
    print(calendar.month(year, month)

elif result == 2:
    # To print the weekday
    print(f"The Weekday is : {calendar.weekday(year, month, date)}")

elif result == 3:
    # To print if the year is a leap year or not.
    calendar.isleap(year)

else:
    print("Wrong Input. Select the number from the above line.")
    print("Start again")
    
    
    
#     SAMPLE OUTPUT


#     Enter the number of month : 3
#     Enter the Year : 2022
#     Enter the Date : 22
#      Select a number. 0 for printing whole year, 1 for printing month, 2 for printing week and 3 for printing if a year is leap or not. : 1
          
#         March 2022
#      Mo Tu We Th Fr Sa Su
#          1  2  3  4  5  6
#       7  8  9 10 11 12 13
#      14 15 16 17 18 19 20
#      21 22 23 24 25 26 27
#      28 29 30 31

          
          
          
          
