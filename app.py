import tkinter as tk

def add_digit(digit):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + digit)

def add_operation(operation):
    current = display.get()
    if current:
        display.delete(0, tk.END)
        display.insert(0, current + operation)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        clear()
        display.insert(0, "Error")

def clear():
    display.delete(0, tk.END)


root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, width=20, font=("Arial", 24))
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('=', 4, 2),
    ('C', 4, 0)
]

for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, command=clear, height=2, width=4)
    elif text == '=':
        button = tk.Button(root, text=text, command=calculate, height=2, width=4)
    elif text in '+-*/':
        button = tk.Button(root, text=text, command=lambda t=text: add_operation(t), height=2, width=4)
    else:
        button = tk.Button(root, text=text, command=lambda t=text: add_digit(t), height=2, width=4)
    button.grid(row=row, column=col)

root.mainloop()
