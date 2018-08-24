#!/usr/bin/env python
year = input("Please enter a year")
var = isleapyear(year)
print var

def isleapyear(year):
    if (((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0)):
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
