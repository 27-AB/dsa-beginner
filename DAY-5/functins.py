# problem given year determie wether is a leap year. If it is a lea year, return the Boolean true, otherwise return False.

def is_leap(year):
    leap = False

    if(year % 4 == 0):
        leap = True
    

    return leap
year = int(input())
print(is_leap(year))
