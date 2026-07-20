# My personal finance tracker
# !!!! Reminder to add comments to each of the fcns soon !!!!!

import json
import os
import sqlite3

def create_database():
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_expense_db(category, amount):
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO expenses (category, amount)
        VALUES (?, ?)
    """, (category, amount))
    connection.commit()
    connection.close()

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    return {}

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def menu():
    print("\n===== Personal Finance Tracker =====")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. View Summary")
    print("6. Save & Exit")
    return input("Choose an option: ")

def get_starting_info():
    starting_balance = get_float("Enter your balance: ")
    income = get_float("Enter your monthly income: ")
    return starting_balance, income

def get_expenses(expenses):
    while True:
        category = str(input("Enter expense category (or 'done' to finish): "))
        if category != 'done':
            expense = float(input("Expense: "))
            expenses[category] = expense
        else:
            break

    return expenses

def calculate_balance(starting_balance, income, expenses):
    total = sum(expenses.values())
    ending_balance = starting_balance + income - total

    return total, ending_balance

def display_expenses(expenses):
    print("\n------ Expenses ------")

    if not expenses:
        print("No expenses recorded.")
        return

    for category, amount in expenses.items():
        print(f"{category}: ${amount}")

def delete_expense(expenses):
    display_expenses(expenses)
    category = input("Enter expense to delete: ")
    if category in expenses:
        del expenses[category]
        print("Expense deleted successfully.")
    else:
        print("Expense not found.")
    return expenses

def edit_expense(expenses):
    category = input("Enter the expense you wish to edit: ")
    if category in expenses:
        new_expense = get_float("Enter the new amount: ")
        expenses[category] = new_expense
        print(f"{category} updated sucessfully!")
    else:
        print("Expense category not found.")
    return expenses

def display_summary(starting_balance, income, expenses, total, ending_balance):
    print("\n------ Summary ------")

    print(f"Starting Balance: ${starting_balance}")
    print(f"Income: ${income}")
    print(f"\nTotal Expenses: ${total}")
    print(f"Remaining Balance: ${ending_balance}")

def finance ():
    print("Welcome to my finance tracker!")
    create_database()

    starting_balance, income = get_starting_info()
    expenses = load_expenses()
    "expenses = get_expenses(expenses)"
    while True:
        choice = menu()

        if choice == "1":
            display_expenses(expenses)

        elif choice == "2":
            expenses = get_expenses(expenses)
        
        elif choice == "3":
            expenses = edit_expense(expenses)

        elif choice == "4":
            expenses = delete_expense(expenses)

        elif choice == "5":
            total, ending_balance = calculate_balance(starting_balance, income, expenses)
            display_summary(starting_balance, income, expenses, total, ending_balance)
            
        elif choice == "6":
            save_expenses(expenses)
            print("Expenses saved successfully!")
            break
        else:
            print("Invalid option. Please try again.")
finance()