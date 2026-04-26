import tkinter as tk

def reverse_bits():
    num = int(entry.get())
    
    # Convert to binary (remove '0b')
    binary = bin(num)[2:]
    
    # Reverse the binary string
    reversed_binary = binary[::-1]
    
    # Convert reversed binary back to decimal
    reversed_decimal = int(reversed_binary, 2)
    
    # Display result
    output_text = f"Enter your original number: {num} ({binary})\n"
    output_text += f"Reversed Number : {reversed_decimal} ({reversed_binary})"
    
    result_label.config(text=output_text)

# Create window
root = tk.Tk()
root.title("Bit Reversal")
root.geometry("400x400")

# Input label
label = tk.Label(root, text="Enter a number:")
label.pack(pady=10)

# Input box
entry = tk.Entry(root)
entry.pack(pady=10)

# Button
button = tk.Button(root, text="Reverse Bits", command=reverse_bits)
button.pack(pady=10)

# Output label
result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=20)

# Run app
root.mainloop()