#!/usr/bin/env python3

"""
Name: TopDownTriangle.py
Desc: A program to print an inverted triangle where the top is a user-defined
size
Auth: Isaac Basque-Rice
Date: 18/05/2022
"""

size = int(input("How large would you like the triangle to be?: "))

stars = "*" * size

for i in range(size):
    stars = stars[:size-i]
    print(stars)
