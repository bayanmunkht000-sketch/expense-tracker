import json
from datetime import date

def load_expenses():
    try:
        with open('expenses.json',"r") as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError:
        expenses = []
        return expenses

def save_expenses(expenses):
    with open('expenses.json','w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    while True:
        name = input("Enter expense name: ")
        name = name.strip()
        if name == "":
            print("Enter expense name")
            continue
        break
    while True:
        category = input("Enter expense category: ")
        category = category.strip()
        if category == "":
            print("Enter expense category")
            continue
        break

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number.")

    today = date.today().isoformat()
    expense = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": today
    }

    expenses.append(expense)
    save_expenses(expenses)

def show_expenses(expenses):
    total = 0
    if not expenses:
        print("No expenses found")
        return
    for expense in expenses:
        name = expense["name"]
        category = expense["category"]
        amount = expense["amount"]
        date = expense["date"]

        total += amount
        print(name, category, amount, date)

    print("Your Total is:", total)

def delete_expense(expenses):
    if not expenses:
        print("No expenses found")
        return
    for index, expense in enumerate(expenses, start=1):
        print(index, expense["name"], expense["category"], expense["amount"], expense["date"])
    while True:
        try:
            expense = int(input("which expense would you like to delete: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= expense <= len(expenses):
            expenses.pop(expense - 1)
            save_expenses(expenses)
            break
        else:
            print("Please enter a valid number.")

def edit_expense(expenses):
    if not expenses:
        print("No expenses found")
        return
    for index, expense in enumerate(expenses, start=1):
        print(index, expense["name"],
              expense["category"],
              expense["amount"],
              expense.get("date","Unknown"))

    while True:
        try:
            choice = int(input("which expense would you like to edit: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= choice <= len(expenses):
            selected_expense = expenses[choice - 1]
            break
        else:
            print("Please enter a valid number.")
    while True:
        new_name = input("Enter new expense name: ").strip()

        if not new_name:
            print("Expense name can't be empty")
            continue
        break
    while True:
        new_category = input("Enter new expense category: ").strip()

        if not new_category:
            print("Expense category can't be empty")
            continue
        break

    while True:
        try:
            new_amount = float(input("Enter new amount: ").strip())
            if new_amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a number.")

    new_date = input("Enter new date: ").strip()

    selected_expense["name"] = new_name
    selected_expense["category"] = new_category
    selected_expense["amount"] = new_amount
    selected_expense["date"] = new_date

    save_expenses(expenses)

def main():
    expenses = load_expenses()
    while True:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Welcome to the Baynaa's Expense Tracker!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("What would you like to do?")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Delete expense")
        print("4. Edit expense")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("please enter a valid number.")
            continue
        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            show_expenses(expenses)
        elif choice == 3:
            delete_expense(expenses)
        elif choice == 4:
            edit_expense(expenses)
        elif choice == 5:
            break
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()