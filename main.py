import tkinter as tk
from tkinter import ttk
import tkinter.font as font

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Salary Breakdown")
    
    font.nametofont("TkDefaultFont").configure(size=15)
    
    gross_salary_input = tk.IntVar()
    gross_salary_output = tk.IntVar(value=0)
    si_output = tk.IntVar(value=0)
    taxes_output = tk.IntVar(value=0)
    net_salary_output = tk.IntVar(value=0)
    
    root.columnconfigure(0, weight=1)
    
    main_frame = ttk.Frame(root, padding=(30,15))
    main_frame.grid()
    
    input_label = ttk.Label(main_frame, text="Enter your Gross Salary:")
    user_input = ttk.Entry(main_frame, width=10, textvariable=gross_salary_input, font=("Segoe UI",15))
    gross_salary_label = ttk.Label(main_frame, text="Gross Salary:")
    si_label = ttk.Label(main_frame, text="Social Insurance :")
    taxes_label = ttk.Label(main_frame, text="Taxes:")
    net_salary_label = ttk.Label(main_frame, text="Net Salary:")
    
    input_label.grid(column=0,row=0,sticky="W")
    user_input.grid(column=1,row=0,sticky="W")
    gross_salary_label.grid(column=0,row=1,sticky="W")
    si_label.grid(column=0,row=2,sticky="W")
    taxes_label.grid(column=0,row=3,sticky="W")
    net_salary_label.grid(column=0,row=4,sticky="W")
    
    
    
    
    root.mainloop()
    pass