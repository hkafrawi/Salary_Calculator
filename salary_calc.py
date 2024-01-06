tax_table_2023 = {0:[0,30_000],
                  .10:[30_000,45_000],
                  .15:[45_000,60_000],
                  .20:[60_000,200_000],
                  .225:[200_000,400_000],
                  .25:[400_000,]}

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

        