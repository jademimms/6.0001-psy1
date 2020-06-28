#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:23:06 2020

@author: Jade
"""
# User Input
annual_salary = float(input('Enter your annual salary:'))

# Initialize variables
semi_annual_raise = .07
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
total_cost = 1000000.0
down_payment = total_cost * 0.25
months = 36
current_savings = 0.0

# Bounds for search
epsilon = 100
initial_high = 10000
high = initial_high
low = 0
portion_saved = (high+low) // 2
steps = 0

while abs(current_savings - down_payment) > epsilon:
    steps += 1
    current_savings = 0.0
    monthly_salary = annual_salary / 12
    monthly_deposit = monthly_salary * (portion_saved / 10000)
    for month in range(1, months + 1):
        current_savings *= 1 + monthly_rate_of_return
        current_savings += monthly_deposit
        if month % 6 == 0:
            annual_salary *= 1 + semi_annual_raise
            monthly_salary = annual_salary / 12
            monthly_deposit = monthly_salary * (portion_saved / 10000)
    prev_portion_saved = portion_saved
    if current_savings > down_payment:
        high = portion_saved
    else:
        low = portion_saved
    portion_saved = int(round((high + low) / 2))
    if prev_portion_saved == portion_saved:
        break
    
if prev_portion_saved == portion_saved and portion_saved == initial_high:
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate:', portion_saved / 10000)
    print('Steps:', steps)
