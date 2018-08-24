#!/usr/local/bin/python3

class palindrome():
    string=input("Enter a string ")
    if(string==string[::-1]):
        print("The string is a palindrome")
    else:
        print("This string is not a palindrome")
        