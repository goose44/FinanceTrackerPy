"My personal finance tracker"

def finance ():

    print("Welcome to my finance tracker!")

    startingBal = float(input("Enter your balance: "))
    income = float(input("Enter your monthly income: "))

    expenses = []
    categories = ["Food", "Gas", "Living"]

    for i in categories:
        expense = float(input(f"Enter your monthly {i} expense: "))
        expenses.append(expense)

    total = sum(expenses)
    endBal = startingBal + income - total

    print("Starting Balance:", startingBal)
    print("Income:", income)
    print("Total Expense:", total)
    print("Remaining Balance:", endBal)

finance()