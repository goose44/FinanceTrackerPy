"My personal finance tracker"

def get_starting_info():

    starting_balance = float(input("Enter your balance: "))
    income = float(input("Enter your monthly income: "))

    return starting_balance, income

def get_expenses():

    expenses = {}

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

def display_summary(starting_balance, income, expenses, total, ending_balance):

    print("\n------ Summary ------")

    print(f"Starting Balance: ${starting_balance}")
    print(f"Income: ${income}")

    print("\nExpenses:")

    for category, amount in expenses.items():
        print(f"{category}: ${amount}")

    print(f"\nTotal Expenses: ${total}")
    print(f"Remaining Balance: ${ending_balance}")

def finance ():

    print("Welcome to my finance tracker!")

    starting_balance, income = get_starting_info()

    expenses = get_expenses()

    total, ending_balance = calculate_balance(starting_balance, income, expenses)

    display_summary(starting_balance, income, expenses, total, ending_balance)

finance()