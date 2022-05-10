#We will create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 100 years old.

age = int(input("What is your current age? "))

years_remaining = 100 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")


