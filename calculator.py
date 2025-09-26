import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Ошибка", "Деление на ноль!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Ошибка", "Выберите операцию!")
            return
        
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

tk.Label(root, text="Число 1:").pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Число 2:").pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack()

operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/"]
tk.Label(root, text="Операция:").pack(pady=10)
for op in operations:
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).pack()

tk.Button(root, text="Вычислить", command=calculate).pack(pady=20)

result_label = tk.Label(root, text="Результат: ")
result_label.pack(pady=20)

root.mainloop()