import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from salary_calc import salary_breakdown


def run_button():
    a = float(gross_salary_input.get())
    gross_salary_value.set(f"{a:,.2f}")
    
    gross_salary,employee_shr,owner_shr,taxes,net_salary = salary_breakdown(a)
    
    si_value.set(f"{employee_shr:,.2f}")
    
    taxes_value.set(f"{taxes:,.2f}")
    
    net_salary_value.set(f"{net_salary:,.2f}")
    


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
    