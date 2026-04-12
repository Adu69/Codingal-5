import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        dob = datetime(year, month, day)
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        messagebox.showinfo("Age", f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

tk.Label(root, text="Date of Birth Calculator").pack(pady=10)

tk.Label(root, text="Day:").pack()
day_entry = tk.Entry(root, width=20)
day_entry.pack()

tk.Label(root, text="Month:").pack()
month_entry = tk.Entry(root, width=20)
month_entry.pack()

tk.Label(root, text="Year:").pack()
year_entry = tk.Entry(root, width=20)
year_entry.pack()

tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

root.mainloop()