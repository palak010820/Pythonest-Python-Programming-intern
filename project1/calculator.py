import tkinter as tk
from tkinter import messagebox

def on_button_click(char):
    if char == 'C':
        entry_var.set('')
    elif char == '=':
        try:
            expression = entry_var.get()
            result = eval(expression)
            entry_var.set(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            entry_var.set('')
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            entry_var.set('')
    else:
        current_text = entry_var.get()
        entry_var.set(current_text + char)

def create_calculator_ui():
    root = tk.Tk()
    root.title("Simple Calculator")

    global entry_var
    entry_var = tk.StringVar()

    entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 18), bd=10, insertwidth=4, width=14, borderwidth=4)
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        action = lambda x=button: on_button_click(x)
        if button == 'C':
            tk.Button(root, text=button, padx=20, pady=20, bd=8, fg='red', font=('Arial', 18), command=action).grid(row=row_val, column=col_val, columnspan=4)
        else:
            tk.Button(root, text=button, padx=20, pady=20, bd=8, fg='black', font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
        
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    root.mainloop()

if __name__ == "__main__":
    create_calculator_ui()
