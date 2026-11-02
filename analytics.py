from validation import normalize_date

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
        date = expense.get("date", "")

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
        raw_date = expense.get("date", "")
        date = normalize_date(raw_date)

        if date is None:
            continue

        amount = expense["amount"]

        if date not in daily_total:
            daily_total[date] = 0

        daily_total[date] += amount

    for date, total in daily_total.items():
        print(date, total)