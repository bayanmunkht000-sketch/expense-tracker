import json
from datetime import date
from datetime import datetime

def load_expenses():
    try:
        with open('expenses.json',"r") as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError:
        expenses = []
        return expenses
    except json.JSONDecodeError:
        print("Expense data is corrupted.")
        return []

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

    search_date = input("Enter date to search: ").strip()
    search_date = normalize_date(search_date)

    if search_date is None:
        print("Date can't be empty")
        return

    for expense in expenses:
        expense_date = normalize_date(expense.get("date",""))
        if expense_date == search_date:
            print(expense["name"],
                  expense["category"],
                  expense["amount"],
                  expense.get["date","Unknown"]
            )
            found = True

    if not found:
        print("No expense found")
    else:
        print("is this what u searched?",)

def search_by_date(expenses):
    found = False
    search_date = input("Enter expense date: ").strip()
    for expense in expenses:
        if expense.get("date","") == search_date:
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
        print("is this what u searched?",)

def show_statistics(expenses):
    amounts = []
    for expense in expenses:
        amounts.append(expense["amount"])

        if not expenses:
            print("No expenses found")
            return

    total = sum(amounts)
    average = total / len(amounts)
    count = len(amounts)
    highest = max(amounts)
    lowest = min(amounts)
    print("===== STATISTICS =====")
    print("Your total is:", total)
    print("Your average is:", average)
    print("Your count is:", count)
    print("Your highest is:", highest)
    print("Your lowest is:", lowest)

def spending_by_category(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount
    for category, total in category_totals.items():
        print("===== Spending by category =====")
        print(category, total)

def monthly_spending(expenses):
    total = 0
    found = False

    search_month = input("Enter month to search: ").strip()

    for expense in expenses:
        date = expense.get("date","")

        if date.startswith(search_month):
            total += expense["amount"]
            print(expense["name"], expense["category"], expense["amount"], expense["date"])
            found = True
    if not found:
        print("month not found")
        return
    else:
        print(f"Your total is in {search_month} is:", total)

def daily_spending(expenses):
    daily_total = {}

    for expense in expenses:
        raw_date = expense.get("date","")
        date = normalize_date(raw_date)

        if date is None:
            continue

        amount = expense["amount"]

        if date not in daily_total:
            daily_total[date] = 0

        daily_total[date] += amount

    for date, total in daily_total.items():
            print(date, total)

def normalize_date(date_text):
    try:
        date = datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        try :
            date = datetime.strptime(date_text, "%Y/%m/%d")
        except ValueError:
            return None

    return date.strftime("%Y-%m-%d")

def positive_number(prompt):
    while True:
        try:
            print("Please enter a positive number.")
            positive = float(input(prompt))
            if positive <= 0:
                print("Negative number not accepted.")
                continue
            return positive
        except ValueError:
            print("Please enter a positive number.")
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
        print("5. Search by category")
        print("6. Search by amount")
        print("7. Search by date")
        print("8. Search by name")
        print("9. Show statistics")
        print("10. Spending by category")
        print("11. Search by Month")
        print("12. Daily Spending")
        print("13. Normalize date")
        print("14. Exit")
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
            search_by_category(expenses)
        elif choice == 6:
            search_by_amount(expenses)
        elif choice == 7:
            search_by_date(expenses)
        elif choice == 8:
            search_by_name(expenses)
        elif choice == 9:
            show_statistics(expenses)
        elif choice == 10:
            spending_by_category(expenses)
        elif choice == 11:
            monthly_spending(expenses)
        elif choice == 12:
            daily_spending(expenses)
        elif choice == 13:
            normalized = normalize_date(input("Enter a date: "))

            if normalized is None:
                print("No normalized date")
            else:
                print("Your normalized date is:", normalized)
        elif choice == 14:
            break
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()