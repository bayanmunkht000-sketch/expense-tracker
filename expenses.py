from datetime import date
from storage import save_expenses
from validation import positive_number
from validation import normalize_date

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

    amount = positive_number("Enter amount: ")

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
              expense.get("date", "Unknown"))

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

    new_amount = positive_number("Enter new amount: ")

    while True:
        new_date = input("Enter new date: ").strip()
        normalized_date = normalize_date(new_date)

        if normalized_date is None:
            print("Date can't be empty")
            continue
        new_date = normalized_date
        break

    selected_expense["name"] = new_name
    selected_expense["category"] = new_category
    selected_expense["amount"] = new_amount
    selected_expense["date"] = new_date

    save_expenses(expenses)


def search_by_category(expenses):
    total = 0
    found = False
    search_category = input("Enter expense category to search: ").strip()
    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            print(expense["name"], expense["category"], expense["amount"], expense["date"])
            total += expense["amount"]
            found = True
    if not found:
        print("No category found")
    else:
        print("Your total is:", total)


def search_by_amount(expenses):
    found = False

    search_amount = positive_number("Enter amount to search: ")

    for expense in expenses:
        if expense["amount"] == search_amount:
            print(expense["name"],
                  expense["category"],
                  expense["amount"],
                  expense.get("date", "Unknown")
                  )
            found = True

    if not found:
        print("No expense found")
    else:
        print("is this what u searched?", )


def search_by_date(expenses):
    found = False
    search_date = input("Enter expense date: ").strip()
    for expense in expenses:
        if expense.get("date", "") == search_date:
            print(expense["name"], expense["category"], expense["amount"], expense["date"])
            found = True
    if not found:
        print("date not found")
    else:
        print("is this what u searched?")


def search_by_name(expenses):
    found = False
    search_name = input("Enter expense name: ").strip()
    for expense in expenses:
        if expense["name"].lower() == search_name.lower():
            print(expense["name"], expense["category"], expense["amount"], expense["date"])
            found = True
    if not found:
        print("name not found")
    else:
        print("is this what u searched?", )