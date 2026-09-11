import numpy as np
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import Tk, messagebox



def process_values():
    try:
        # 1. Read input strings and convert to float
        Theta = float(entry_val1.get())
        w = float(entry_val2.get())

        # 2. Perform your calculations or main script logic here
        result = Theta * w  # Example operation

        # 3. Output result to screen
        lbl_result.config(text=f"Result: {result}")

    except ValueError:
        # Handles empty fields, letters, or invalid numbers
        messagebox.showerror(
            "Input Error", "Please enter valid floating-point numbers!"
        )


# --- UI Setup ---
root = tk.Tk()
root.title("Float Input GUI")
root.geometry("1920x1200")
root.attributes("-fullscreen", True)

# Input 1
tk.Label(root, text="Hoek:").pack(pady=(10, 0))
entry_val1 = tk.Entry(root)
entry_val1.pack()

# Input 2
tk.Label(root, text="Hoeksnelheid:").pack(pady=(10, 0))
entry_val2 = tk.Entry(root)
entry_val2.pack()



# Submit Button
btn_submit = tk.Button(root, text="Calculate", command=process_values)
btn_submit.pack(pady=15)

# Result Label
lbl_result = tk.Label(root, text="Result: -", font=("Arial", 11, "bold"))
lbl_result.pack()

#exit button
btn_exit = tk.Button(root, text="Exit", command=root.destroy)
btn_exit.pack(pady=15)

# Start GUI event loop
root.mainloop()