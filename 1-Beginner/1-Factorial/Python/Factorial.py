#!/usr/bin/env python3

"""
Name: Factorial.py
Desc: A program to calculate the factorial of a given number
Auth: Isaac Basque-Rice
Date: 17/05/2022
"""

print("Enter a number to be factorialised!")

num = int(input())
fact = 1

for i in range(1, num+1):
    fact = fact * i

print(str(num) + " factorial is " + str(fact))
