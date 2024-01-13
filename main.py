import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames import GrossSalary,NetSalary

class SalaryCalc(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.title("Salary Calculator")
        
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)
        
        gross_salary = GrossSalary(container)
        gross_salary.grid(row=0,column=0,sticky="NESW")
        
        net_salary = NetSalary(container)
        net_salary.grid(row=0,column=0,sticky="NESW")
        
        self.frames = dict()
        self.frames[GrossSalary] = gross_salary
        self.frames[NetSalary] = net_salary
        
        self.show_frame(NetSalary)
        
    def show_frame(self,container):
        frame = self.frames[container]
        frame.tkraise()

app = SalaryCalc()
app.mainloop()
    