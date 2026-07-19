"My personal finance tracker"

import json
import os

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    if os.path.exists("expenses.json"):

        with open("expenses.json", "r") as file:
            return json.load(file)
    return {}

def menu():
    print("\n===== Personal Finance Tracker =====")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Save & Exit")

    choice = input("Choose an option: ")

    return choice

def get_starting_info():
    starting_balance = float(input("Enter your balance: "))
    income = float(input("Enter your monthly income: "))

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

def display_summary(starting_balance, income, expenses, total, ending_balance):
    print("\n------ Summary ------")

    print(f"Starting Balance: ${starting_balance}")
    print(f"Income: ${income}")
    print(f"\nTotal Expenses: ${total}")
    print(f"Remaining Balance: ${ending_balance}")

def finance ():
    print("Welcome to my finance tracker!")

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
            total, ending_balance = calculate_balance(starting_balance, income, expenses)
            display_summary(starting_balance, income, expenses, total, ending_balance)
            
        elif choice == "4":
            save_expenses(expenses)
            print("Expenses saved successfully!")
            break
        else:
            print("Invalid option. Please try again.")
finance()