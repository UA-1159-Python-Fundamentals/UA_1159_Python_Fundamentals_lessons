from expense import Expense
import csv
import os
from typing import List

# Standart categories
expense_categories = [
    "Food",
    "Home", 
    "Transport", 
    "Job", 
    "Fun", 
    "Subscriptions"
]

# Save user's information about expense
def save_user_expense(expense, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense.name, expense.category, expense.amount, expense.date])

# Read file with expenses for summary        
def read_expenses(expense_file_path):
    print("💲 Reading Expenses from File")
    expenses = []

    with open(expense_file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, category, amount, date = row
            amount = float(amount)
            expense = Expense(name=name, category=category, amount=amount, date=date)
            expenses.append(expense)

    return expenses

def get_total_amount_for_category(category, expense_file_path):
    print(f"💲 Getting Total Amount for Category: {category}")
    total_amount = 0

    expenses: List[Expense] = read_expenses(expense_file_path)

    for expense in expenses:
        if expense.category == category:
            total_amount += expense.amount

    return total_amount

def clear_expense_data(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"🛀 Data in {filename} cleared successfully!")
        else:
            print(f"{filename} does not exist. No data to clear.")
    except Exception as e:
        print(f"An error occurred while clearing data: {e}")
