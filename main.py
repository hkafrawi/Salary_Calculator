import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames import GrossSalary,NetSalary

class SalaryCalc(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.title("Salary Calculator")
        
        font.nametofont("TkDefaultFont").configure(size=15)
        
        container = ttk.Frame(self)
        container.pack(expand=True)
        #container.columnconfigure(0, weight=1)
        
        gross_salary = GrossSalary(container, lambda: self.show_frame(NetSalary))
        gross_salary.grid(row=0,column=0,sticky="nsew")
        
        net_salary = NetSalary(container, lambda: self.show_frame(GrossSalary))
        net_salary.grid(row=0,column=0,sticky="nsew")
        
        self.frames = dict()
        self.frames[GrossSalary] = gross_salary
        self.frames[NetSalary] = net_salary
        
        self.show_frame(GrossSalary)
        
    def show_frame(self,container):
        frame = self.frames[container]
        frame.tkraise()

app = SalaryCalc()
app.mainloop()
    