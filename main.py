"My personal finance tracker"

def finance ():

    print("Welcome to my finance tracker!")

    startingBal = float(input("Enter your balance: "))
    income = float(input("Enter your monthly income: "))

    expenses = {}
    
    while True:
        category = str(input("Enter expense category (or 'done' to finish): "))
        if category != 'done':
            expense = float(input("Expense: "))
            expenses[category] = expense
        else:
            break

    print(expenses)
    total = sum(expenses.values())
    endBal = startingBal + income - total

    print(f"Starting Balance: ${startingBal}")
    print(f"Income: ${income}")

    for category, amount in expenses.items():
        print(f"{category}: ${amount}")

    print(f"Ending Balance: ${endBal}")

finance()