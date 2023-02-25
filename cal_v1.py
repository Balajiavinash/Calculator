# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:15:05 2023

@author: konak
"""

while True:
    # Take input from the user
    expression = input("Enter an arithmetic expression or 'q' to quit: ")

    # Quit the program if the user enters 'q'
    if expression == 'q':
        break

    # Evaluate the expression and output the result
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except:
        print("Invalid expression")
