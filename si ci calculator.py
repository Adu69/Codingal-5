import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())
        
        simple_interest = (principal * time * rate) / 100
        compound_interest = principal * (1 + rate / 100) ** time - principal
        
        messagebox.showinfo("Results", 
            f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x400")

tk.Label(root, text="Principal Amount:").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack(pady=5)

tk.Label(root, text="Time Period (years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)

tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack(pady=20)

root.mainloop()