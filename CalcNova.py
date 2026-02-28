import tkinter as tk
import math

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def sin():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def cos():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def tan():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def log():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")


# Main Window
root = tk.Tk()
root.title("CalcNova Lite - Scientific")
root.geometry("420x550")
root.configure(bg="#222831")

# Display
entry = tk.Entry(root, font=("Arial", 22), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(pady=15, padx=10, fill="both")

# Frame
frame = tk.Frame(root, bg="#222831")
frame.pack()

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        action = calculate
    else:
        action = lambda x=button: click(x)

    tk.Button(frame, text=button, width=6, height=2,
              font=("Arial", 16),
              command=action).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Scientific Buttons
tk.Button(root, text="√", font=("Arial", 14), command=sqrt).pack(fill="both", padx=20, pady=5)
tk.Button(root, text="sin", font=("Arial", 14), command=sin).pack(fill="both", padx=20, pady=5)
tk.Button(root, text="cos", font=("Arial", 14), command=cos).pack(fill="both", padx=20, pady=5)
tk.Button(root, text="tan", font=("Arial", 14), command=tan).pack(fill="both", padx=20, pady=5)
tk.Button(root, text="log", font=("Arial", 14), command=log).pack(fill="both", padx=20, pady=5)
tk.Button(root, text="Clear", font=("Arial", 14), command=clear).pack(fill="both", padx=20, pady=5)

root.mainloop()