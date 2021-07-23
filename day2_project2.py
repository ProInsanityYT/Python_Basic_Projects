
# Day 2 project 2 bonus challenge. This program takes an year as input and checks if it is a leap year
def check_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
        

userYear=int(input("Enter year to check if leap: "))
if check_leap_year(userYear):
  print (str(userYear) + " is a leap year!")
else:
  print(str(userYear) + " is not a leap year!")
  