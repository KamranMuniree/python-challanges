#!/usr/bin/env python
year = input("Please enter a year")

if (year % 4) == 0:
    if (year % 100) == 0:
        print("{0} is a leap year".format(year))
else:
    if (year % 400) != 0:
        print("{0} is not a leap year".format(year))
