#!/usr/bin/env python3

"""
Name: CurrencyConverter.py
Desc: A progrm to convert between USD and GBP
Auth: Isaac Basque-Rice
Date: 18/05/2022
"""

# As of writing 
# 1 GBP = 1.25 USD
# 1 USD = 0.80 GBP

def select_currency(currency_choice):
    match currency_choice: # thank u Python 3.10
        case 1:
            return "GBP"
        case 2:
            return "USD"
        
    print("Invalid, exiting")
    quit()

print("Welcome to izbr's currency converter")

print("What is your starting currency?")
print("1: GBP")
print("2: USD")

currency_choice = int(input())

starting_currency = select_currency(currency_choice)

cash = float(input("How much would you like to convert?: "))

if starting_currency != "Invalid":
    if starting_currency == "GBP":
        result = cash * 1.25
        other_currency = "USD"
    else:
        result = cash * 0.80
        other_currency = "GBP"

print(str(cash) + " " + starting_currency + " is " + str(result) + " " + other_currency)
