tax_table_2023 = {0:[0,30_000],
                  .10:[30_001,45_000],
                  .15:[45_001,60_000],
                  .20:[60_001,200_000],
                  .225:[200_001,400_000],
                  .25:400_001}

def calc_tax(n):
    tax = 0
    for x in tax_table_2023.keys():
        if n > tax_table_2023[x][1]-tax_table_2023[x][0]:
            tax = tax + (tax_table_2023[x]*tax_table_2023[x][1])
            n = n - tax_table_2023[x][1]
        else:
            tax = tax + (tax_table_2023[x]*n)    
            break
        
    return tax

        