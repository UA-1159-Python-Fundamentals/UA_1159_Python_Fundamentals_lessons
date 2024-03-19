import json
from datetime import datetime
import tkinter as tk
import matplotlib.pyplot as plt



def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'expenses': []}

def save_expenses(data):
    with open('expenses.json', 'w') as file:
        json.dump(data, file, indent=2)

def add_expense():
    label_category.pack()
    entry_category.pack()
    label_amount.pack()
    entry_amount.pack()
    label_currency.pack()
    entry_currency.pack()
    category = entry_category.get()
    amount = float(entry_amount.get())
    currency = entry_currency.get()

    expenses_data = load_expenses()
    expenses = expenses_data['expenses']

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    expense = {
        'timestamp': timestamp,
        'category': category,
        'amount': amount,
        'currency': currency
    }

    expenses.append(expense)
    expenses_data['expenses'] = expenses
    save_expenses(expenses_data)
    label = tk.Label(root, text="Витрата успішно додана!")
    label.pack()


def view_expenses():
    expenses_data = load_expenses()
    expenses = expenses_data['expenses']

    if not expenses:
        label = tk.Label(root, text="Витрат немає")
        label.pack()

    else:
        label = tk.Label(root, text="***Історія витрат***")
        label.pack()
        for i, expense in enumerate(expenses):
            label = tk.Label(root, text=f"{i + 1}. {expense['timestamp']} - {expense['category']}: {expense['amount']} {expense['currency']}")
            label.pack()

def delete_expense():
    delete_window = tk.Toplevel()
    delete_window.title("Видалення витрати")

    label_index = tk.Label(delete_window, text="Введіть індекс витрати для видалення:")
    label_index.pack()

    entry_index = tk.Entry(delete_window)
    entry_index.pack()

    def confirm_delete():
        index = int(entry_index.get()) - 1
        delete_expense_by_index(index)
        delete_window.destroy()

    button_confirm = tk.Button(delete_window, text="Підтвердити видалення", command=confirm_delete)
    button_confirm.pack()

def delete_expense_by_index(index):
    expenses_data = load_expenses()
    expenses = expenses_data['expenses']

    if 0 <= index < len(expenses):
        deleted_expense = expenses.pop(index)
        expenses_data['expenses'] = expenses
        save_expenses(expenses_data)
        print(f"Витрата видалена: {deleted_expense}")
    else:
        print("Невірний індекс витрати. Спробуйте ще раз.")

def diagram():
    expenses_data = load_expenses()
    expenses = expenses_data['expenses']
    categories = {}
    total_expense = 0

    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        total_expense += amount
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    labels_ = categories.keys()
    sizes = [amount / total_expense for amount in categories.values()]

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels_, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Доля витрат за категоріями')
    plt.show()


def authenticate():
    login_data = load_registration_data()
    entered_login = entry_login.get()
    entered_password = entry_password.get()

    for user in login_data:
        if user['login'] == entered_login and user['password'] == entered_password:
            label_auth_status.config(text="Ви увійшли!", fg="green")
            label_login.grid_forget()
            entry_login.grid_forget()
            label_password.grid_forget()
            entry_password.grid_forget()
            button_register.pack_forget()
            button_enter.pack_forget()
            label_authentification.pack_forget()
            button_add.pack()
            button_delete.pack()
            button_view.pack()
            button_diagram.pack()
            button_exit.pack()
            return
    label_auth_status.config(text="Пароль або логін не вірний!", fg="red")


def load_registration_data():
    try:
        with open('registration.json', 'r') as file:
            data = json.load(file)
            return data.get('registration', [])
    except FileNotFoundError:
        return []

def save_registration_data(data):
    with open('registration.json', 'w') as file:
        json.dump({'registration': data}, file, indent=2)


def registration():
    register_data = load_registration_data()
    login = entry_login.get()
    password = entry_password.get()

    registration = {
        'login': login,
        'password': password,
    }

    register_data.append(registration)

    save_registration_data(register_data)
    label = tk.Label(root, text="Ви успішно зареєструвалися!", fg="green")
    label.pack()




root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x600")

label_title = tk.Label(root, text="Expense Tracker", font=("Helvetica", 16))
label_title.pack(pady=10)

label_authentification = tk.Label(root,text="Authentification",font=("Helvetica", 16))
label_authentification.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

label_login = tk.Label(frame_input, text="Ваш логін:")
label_login.grid(row=0, column=0, padx=5, pady=5)

entry_login = tk.Entry(frame_input)
entry_login.grid(row=0, column=1, padx=5, pady=5)

label_password = tk.Label(frame_input, text="Ваш пароль:")
label_password.grid(row=1, column=0, padx=5, pady=5)

entry_password = tk.Entry(frame_input)
entry_password.grid(row=1, column=1, padx=5, pady=5)

button_enter = tk.Button(root, text="Увійти", command=authenticate)
button_enter.pack()

button_register = tk.Button(root, text="Зареєструватися", command=registration)
button_register.pack()

label_auth_status = tk.Label(root, text="")
label_auth_status.pack(pady=10)

label_category = tk.Label(frame_input, text="Категорія витрати:")
entry_category = tk.Entry(frame_input)
label_amount = tk.Label(frame_input, text="Сума витрати:")
entry_amount = tk.Entry(frame_input)
label_currency = tk.Label(frame_input, text="Валюта:")
entry_currency = tk.Entry(frame_input)

button_add = tk.Button(root, text="Додати витрату", command=add_expense)
button_delete = tk.Button(root, text="Видалити витрату", command=delete_expense)
button_view = tk.Button(root, text="Переглянути витрати", command=view_expenses)
button_diagram = tk.Button(root, text="Діаграма витрат", command=diagram)
button_exit = tk.Button(root, text="Вийти", command=root.quit)

root.mainloop()
