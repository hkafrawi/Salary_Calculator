from salary_law import tax_table_2023,social_insurance_frame_2023
import numpy as np

def calc_tax(n):
    tax = 0
    keys = [key for key in tax_table_2023.keys()]
    for x in keys[:-1]:
        tax_level = tax_table_2023[x][1]-tax_table_2023[x][0]
        if n > tax_level:
            tax = tax + (x*tax_level)
            n = n - tax_level
        else:
            tax = tax + (x*n)
            n = n - n    
            break
    if n > 0:
        tax = tax +(keys[-1]*n)
                
    return tax

def calc_si(n, salary_frame:list, employee_owner_share= [0.11,0.1875]):
    if (n>salary_frame[0]) & (n<=salary_frame[1]):
        n = n*.80
        employee_share = n*employee_owner_share[0]
        owner_share = n*employee_owner_share[1]
        
    elif n<=salary_frame[0]:
        n=salary_frame[0]
        n = n*.80
        employee_share = n*employee_owner_share[0]
        owner_share = n*employee_owner_share[1]
        
    elif n>salary_frame[1]:
        n=salary_frame[1]
        n = n*.80 
        employee_share = n*employee_owner_share[0]
        owner_share = n*employee_owner_share[1]
        
    return employee_share, owner_share
    
def salary_breakdown(gross_salary):
    employee_shr, owner_shr = calc_si(gross_salary,social_insurance_frame_2023)
    taxes = calc_tax(gross_salary-employee_shr)
    net_salary = gross_salary-(taxes+employee_shr)
    
    return gross_salary,employee_shr,owner_shr,taxes,net_salary

def find_gross_salary(net_salary):
    # Assuming gross salary is at least the social insurance frame lower limit
    gross_salary_guess = net_salary + social_insurance_frame_2023[0]

    while True:
        # Calculate breakdown using the guessed gross salary
        breakdown = salary_breakdown(gross_salary_guess)
        _, employee_share, _, taxes, net_salary_guess = breakdown

        # If the guessed net salary is close enough to the actual net salary, break the loop
        if abs(net_salary_guess - net_salary) < 1:
            break

        # Adjust the guessed gross salary based on the difference between the actual and guessed net salary
        gross_salary_guess += (net_salary - net_salary_guess)

    return gross_salary_guess




