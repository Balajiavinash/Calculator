# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:45:18 2023

@author: navee
"""

while True:
    
    num1=int(input('enter  first number\n'))
    
    num2=int(input('enter second number\n'))
    print("1.addition 2.subtraction 3.multiplication 4.division")
    opt =int(input("enter the operation (number) you want to do \n"))
    if opt ==1:
        print(num1+num2)
    elif opt==2:
        print(num1-num2)
    elif opt==3:
        print(num1*num2)
        
    elif opt==4:
        print(num1//num2)
    break