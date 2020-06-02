#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:37:23 2020

@author: Jade
"""

#user input
annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the portion of your salary to be saved:'))
total_cost = float(input('Enter the cost of your dream home:'))
                      
#Non user input fixed information
portion_down_payment = 0.25
r = 0.04/12
monthly_salary = annual_salary/12
down_payment = total_cost * portion_down_payment
monthly_savings = monthly_salary * portion_saved

#Set current savings to 0 
current_savings = 0.0

#Set months to 0 
months = 0

#Calculate months to reach down payment

while current_savings < down_payment:
    current_savings *= 1 + r
    current_savings += monthly_savings
    months += 1
else: 
    print('It will take ' + str(months) + ' months to save for the down payment.')
    

