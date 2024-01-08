import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from salary_calc import calc_tax,calc_si
from salary_law import social_insurance_frame_2023

def run_button():
    a = float(gross_salary_input.get())
    gross_salary_value.set(f"{a:,.2f}")
    
    x = calc_si(a,social_insurance_frame_2023)[0]
    si_value.set(f"{x:,.2f}")
    
    salary_after_si = a-x
    y=calc_tax(salary_after_si)
    taxes_value.set(f"{y:,.2f}")
    
    salary_after_taxes = salary_after_si-y
    net_salary_value.set(f"{salary_after_taxes:,.2f}")
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Salary Breakdown")
    
    font.nametofont("TkDefaultFont").configure(size=15)
    
    gross_salary_input = tk.StringVar()
    
    gross_salary_value=tk.StringVar()
    si_value=tk.StringVar()
    taxes_value=tk.StringVar()
    net_salary_value = tk.StringVar()
    
    
    root.columnconfigure(0, weight=1)
    
    main_frame = ttk.Frame(root, padding=(30,15))
    main_frame.grid()
    
    # Items Setup
    input_label = ttk.Label(main_frame, text="Enter your Gross Salary:")
    user_input = ttk.Entry(main_frame, width=10, textvariable=gross_salary_input, font=("Segoe UI",15))
    
    gross_salary_label = ttk.Label(main_frame, text="Gross Salary:")
    gross_salary_display = ttk.Label(main_frame, textvariable=gross_salary_value)
        
    si_label = ttk.Label(main_frame, text="Social Insurance :")
    si_output = ttk.Label(main_frame,textvariable=si_value)
    
    taxes_label = ttk.Label(main_frame, text="Taxes:")
    taxes_display = ttk.Label(main_frame, textvariable=taxes_value)
    
    net_salary_label = ttk.Label(main_frame, text="Net Salary:")
    net_salary_display = ttk.Label(main_frame, textvariable=net_salary_value)
    
    calc_button = ttk.Button(main_frame, text="Run", command=run_button)
    
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
    
    
    
    
    root.mainloop()
    