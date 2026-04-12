import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

num1 = simpledialog.askinteger("Input", "Enter first number:")
num2 = simpledialog.askinteger("Input", "Enter second number:")

product = num1 * num2
messagebox.showinfo("Result", f"Product: {product}")

root.destroy() 