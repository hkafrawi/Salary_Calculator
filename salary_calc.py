from salary_law import tax_table_2023,social_insurance_frame_2023

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
        
    elif n<salary_frame[0]:
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



        
calc_tax(7000)
calc_si(7000,social_insurance_frame_2023)