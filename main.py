# My personal finance tracker
# !!!! Reminder to add comments to each of the fcns soon !!!!!

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

# dtabase testing to see if it works or no
def view_database():
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    print("\n------ Database ------")
    for row in rows:
        print(row)
    connection.close()

def display_expenses():
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, category, amount
        FROM expenses
    """)
    rows = cursor.fetchall()
    print("\n------ Expenses ------")

    if not rows:
        print("No expenses found.")
    else:
        for expense_id, category, amount in rows:
            print(f"{expense_id}. {category}: ${amount}")
    connection.close()

def add_expense():
    category = input("Enter expense category: ")
    amount = get_float("Expense: ")
    add_expense_db(category, amount)
    print("Expense added successfully!")

#def save_expenses(expenses):
    #with open("expenses.json", "w") as file:
        #json.dump(expenses, file, indent=4)

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

def calculate_balance():
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
    """)
    total = cursor.fetchone()[0]
    connection.close()
    return total or 0

def delete_expense():
    display_expenses()
    expense_id = int(input("\nEnter expense ID to delete: "))
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )
    connection.commit()
    connection.close()
    print("Expense deleted successfully!")

def edit_expense():
    display_expenses()
    expense_id = int(input("\nEnter expense ID to edit: "))
    amount = get_float("Enter the new amount: ")
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE expenses SET amount = ? WHERE id = ?",
        (amount, expense_id)
    )
    connection.commit()
    connection.close()
    print("Expense updated successfully!")

def display_summary(starting_balance, income):
    total = calculate_balance()
    ending_balance = starting_balance + income - total

    print("\n------ Summary ------")
    print(f"Starting Balance: ${starting_balance}")
    print(f"Income: ${income}")
    print(f"Total Expenses: ${total}")
    print(f"Remaining Balance: ${ending_balance}")

def finance ():
    print("Welcome to my finance tracker!")
    create_database()

    starting_balance, income = get_starting_info()
    while True:
        choice = menu()

        if choice == "1":
            display_expenses()

        elif choice == "2":
            add_expense()
        
        elif choice == "3":
            edit_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            display_summary(starting_balance, income)
            
        elif choice == "6":
            view_database()
            print("Expenses saved successfully!")
            break
        else:
            print("Invalid option. Please try again.")
finance()