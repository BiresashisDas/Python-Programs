'''Below are the points of how to check whether a year is a leap year or not.
    --- on every year that is evenly divisible by 4 
    --- except every year that is evenly divisible by 100 
    --- unless the year is also evenly divisible by 400  
    
            eg :- The year 2000:
            2000 ÷ 4 = 500 (Leap)
            2000 ÷ 100 = 20 (Not Leap)
            2000 ÷ 400 = 5 (Leap!)
            So the year 2000 is a leap year. '''

year = int(input("Enter the year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
    
    
    
