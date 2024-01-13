import tkinter as tk
from tkinter import ttk
from calc import salary_breakdown,find_gross_salary

class NetSalary(ttk.Frame):
    def __init__(self,parent,change_page_func):
        super().__init__(parent)
        
        self.net_salary_input = tk.StringVar()
        
        self.gross_salary_value=tk.StringVar()
        self.si_value=tk.StringVar()
        self.taxes_value=tk.StringVar()
        self.net_salary_value = tk.StringVar()
        
        # Items Setup
        input_label = ttk.Label(self, text="Enter your Net Salary:")
        user_input = ttk.Entry(self, width=10, textvariable=self.net_salary_input, font=("Segoe UI",15))
        
        gross_salary_label = ttk.Label(self, text="Gross Salary:")
        gross_salary_display = ttk.Label(self, textvariable=self.gross_salary_value)
            
        si_label = ttk.Label(self, text="Social Insurance :")
        si_output = ttk.Label(self,textvariable=self.si_value)
        
        taxes_label = ttk.Label(self, text="Taxes:")
        taxes_display = ttk.Label(self, textvariable=self.taxes_value)
        
        net_salary_label = ttk.Label(self, text="Net Salary:")
        net_salary_display = ttk.Label(self, textvariable=self.net_salary_value)
        
        calc_button = ttk.Button(self, text="Run", command=self.run_button)
        
        chg_button = ttk.Button(self,text="Change Input", command=change_page_func)

        
        # Grid Setup
        input_label.grid(column=0,row=0,sticky="W")
        user_input.grid(column=1,row=0,sticky="W")
        
        gross_salary_label.grid(column=0,row=1,sticky="W")
        gross_salary_display.grid(column=1,row=1,sticky="E")
        
        si_label.grid(column=0,row=2,sticky="W")
        si_output.grid(column=1,row=2,sticky="E")
        
        taxes_label.grid(column=0,row=3,sticky="W")
        taxes_display.grid(column=1,row=3,sticky="E")
        
        net_salary_label.grid(column=0,row=4,sticky="W")
        net_salary_display.grid(column=1,row=4,sticky="E")
        calc_button.grid(column=1,row=5,sticky="E")
        chg_button.grid(column=0,row=5,sticky="E")
        
    def run_button(self):
        a = float(self.net_salary_input.get())
        
        gross_salary,employee_shr,_,taxes,net_salary = salary_breakdown(find_gross_salary(a))
        
        self.gross_salary_value.set(f"{gross_salary:,.2f}")
    
        self.si_value.set(f"{employee_shr:,.2f}")
    
        self.taxes_value.set(f"{taxes:,.2f}")
    
        self.net_salary_value.set(f"{net_salary:,.2f}")
        
        